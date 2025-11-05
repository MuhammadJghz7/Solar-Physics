;==========================================================
; خواندن داده
;==========================================================
restore, 'data.sav'   ; جایگزین با نام واقعی فایل خود
help, istks

nwave = size(istks, /dim)[0]
nx    = size(istks, /dim)[1]
ny    = size(istks, /dim)[2]
print, 'nwave=',nwave,' nx=',nx,' ny=',ny

;----------------------------------------------------------
; تعریف طول موج‌ها
; (در صورت وجود آرایه λ واقعی از فایل، جایگزین کنید)
lambda0 = 6302.5     ; Fe I 6302.5 Å
dlambda = 0.021      ; فاصله طول موج بین کانال‌ها (Å)
lambda = lambda0 + (findgen(nwave) - nwave/2.0) * dlambda

;----------------------------------------------------------
; محاسبه کانتینیوم از لبه‌های طیف
;----------------------------------------------------------
ind_cont = [0:3, nwave-4:nwave-1]
I_cont_map = mean(istks[ind_cont,*,*], 1)

;----------------------------------------------------------
; آماده‌سازی خروجی‌ها
;----------------------------------------------------------
v_map   = fltarr(nx, ny) + !values.f_nan  ; نقشه سرعت دوپلر (km/s)
depth_map = fltarr(nx, ny)
width_map = fltarr(nx, ny)
chi2_map  = fltarr(nx, ny)

c = 2.99792458e5  ; km/s

;----------------------------------------------------------
; حلقه برازش گاوسی روی هر پیکسل
;----------------------------------------------------------
for j=0, ny-1 do begin
    for i=0, nx-1 do begin

        prof = double(istks[*,i,j])
        Icont = mean(prof[ind_cont])
        if (Icont le 0) then continue

        ; نرمال‌سازی نسبت به کانتینیوم
        prof_norm = prof / Icont

        ; تخمین اولیه پارامترها:
        imin = min(prof_norm, idx)
        amp0 = 1.0 - imin                ; عمق تقریبی
        cen0 = lambda[idx]               ; طول موج حداقل
        wid0 = 0.06                      ; حدس اولیه پهنا (Å)

        ; تابع برازش: I = 1 - a * exp(-((λ - λ0)^2)/(2σ^2))
        ; پارامترها: p = [offset, amplitude, center, width]
        yfit = 1 - amp0 * exp(-((lambda - cen0)^2)/(2*wid0^2))
        p0 = [0.0, amp0, cen0, wid0]

        ; استفاده از GAUSSFIT
        coeff = gaussfit(lambda, prof_norm, yfit, p0)

        offset = coeff[0]
        amp    = coeff[1]
        center = coeff[2]
        width  = abs(coeff[3])

        ; ارزیابی کیفیت برازش
        model = 1 - amp * exp(-((lambda - center)^2)/(2*width^2))
        chi2 = total((prof_norm - model)^2) / float(nwave)

        ; ذخیره نتایج
        v_map[i,j]   = ((center - lambda0) / lambda0) * c
        depth_map[i,j] = amp
        width_map[i,j] = width
        chi2_map[i,j]  = chi2
    endfor
    print, 'row', j+1, 'of', ny, 'done'
endfor

;----------------------------------------------------------
; نمایش نتایج
;----------------------------------------------------------
window, 0, title='Doppler velocity (km/s)'
tv, bytscl(v_map, min=-2, max=2)
window, 1, title='Line depth (amplitude)'
tv, bytscl(depth_map)
window, 2, title='Line width (Å)'
tv, bytscl(width_map, min=0, max=0.1)

;----------------------------------------------------------
; ذخیره نقشه‌ها
;----------------------------------------------------------
save, v_map, depth_map, width_map, chi2_map, I_cont_map, filename='gaussfit_maps.sav'
print, 'نتایج در gaussfit_maps.sav ذخیره شدند.'