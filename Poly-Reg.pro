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
;----------------------------------------------------------
lambda0 = 6302.5     ; Fe I 6302.5 Å
dlambda = 0.021      ; فاصله طول موج بین کانال‌ها (Å)
lambda = lambda0 + (findgen(nwave) - nwave/2.0) * dlambda

;----------------------------------------------------------
; محاسبه کانتینیوم از چند کانال ابتدایی و انتهایی
;----------------------------------------------------------
ind_cont = [0:3, nwave-4:nwave-1]
I_cont_map = mean(istks[ind_cont,*,*], 1)

;----------------------------------------------------------
; آماده‌سازی خروجی‌ها
;----------------------------------------------------------
v_map   = fltarr(nx, ny) + !values.f_nan
center_map = fltarr(nx, ny) + !values.f_nan
depth_map  = fltarr(nx, ny) + !values.f_nan

c = 2.99792458e5  ; سرعت نور (km/s)

;----------------------------------------------------------
; حلقه روی پیکسل‌ها
;----------------------------------------------------------
for j=0, ny-1 do begin
  for i=0, nx-1 do begin

    prof = double(istks[*,i,j])
    Icont = mean(prof[ind_cont])
    if (Icont le 0) then continue

    prof_norm = prof / Icont

    ; یافتن حداقل
    idx_min = min(prof_norm, imin)
    if (imin lt 0.2) then continue  ; حذف نقاط خراب یا اشباع

    ; بررسی اینکه بتوان 2 نقطه قبل و بعد را داشت
    if ( (idx_min lt 2) or (idx_min gt nwave-3) ) then continue

    ; انتخاب 5 نقطه اطراف مینیمم
    ind = idx_min-2 + indgen(5)
    x = lambda[ind]
    y = prof_norm[ind]

    ; برازش چندجمله‌ای درجه 2
    coeff = poly_fit(x, y, 2, /double)
    ; y = a*x^2 + b*x + c

    a = coeff[0]
    b = coeff[1]
    c0 = coeff[2]

    ; مختصات رأس (مرکز خط)
    if (a ne 0) then lambda_c = -b / (2*a) else lambda_c = lambda[idx_min]

    ; محاسبه عمق خط در مرکز برازش‌شده
    I_min_fit = a*lambda_c^2 + b*lambda_c + c0

    ; سرعت دوپلر
    v = ((lambda_c - lambda0)/lambda0) * c

    v_map[i,j] = v
    center_map[i,j] = lambda_c
    depth_map[i,j] = 1 - I_min_fit
  endfor
  print, 'row', j+1, 'of', ny, 'done'
endfor

;----------------------------------------------------------
; نمایش نتایج
;----------------------------------------------------------
window, 0, title='Doppler velocity (km/s)'
tv, bytscl(v_map, min=-2, max=2)

window, 1, title='Line depth'
tv, bytscl(depth_map)

;----------------------------------------------------------
; ذخیره نتایج
;----------------------------------------------------------
save, v_map, center_map, depth_map, I_cont_map, filename='parabolic_fit_maps.sav'
print, 'نتایج در parabolic_fit_maps.sav ذخیره شدند.'