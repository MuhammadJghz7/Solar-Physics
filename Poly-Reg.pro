;==========================================================
; خواندن داده
;==========================================================
restore, 'data.sav'   ; فایل شامل istks
help, istks

nwave = size(istks, /dim)[0]
nx    = size(istks, /dim)[1]
ny    = size(istks, /dim)[2]
print, 'nwave=',nwave,' nx=',nx,' ny=',ny

;----------------------------------------------------------
; تعیین محدوده طول موج برای دو خط
;----------------------------------------------------------
n1 = nwave/2L
n2 = nwave - n1

; خطوط
lambda0_1 = 6301.5
lambda0_2 = 6302.5

; فرض فاصله طیفی ثابت
dlambda = 0.021   ; Å — دقیق را از متادیتا بگیرید

lambda_1 = lambda0_1 + (findgen(n1) - n1/2.0) * dlambda
lambda_2 = lambda0_2 + (findgen(n2) - n2/2.0) * dlambda

;----------------------------------------------------------
; کانتینیوم از چند نقطه‌ی ابتدایی و انتهایی هر نیمه
;----------------------------------------------------------
ind_cont1 = [0:3, n1-4:n1-1]
ind_cont2 = n1 + [0:3, n2-4:n2-1]

I_cont_map1 = mean(istks[ind_cont1,*,*], 1)
I_cont_map2 = mean(istks[ind_cont2,*,*], 1)

;----------------------------------------------------------
; آماده‌سازی نقشه‌های خروجی
;----------------------------------------------------------
v_map1 = fltarr(nx, ny) + !values.f_nan
v_map2 = fltarr(nx, ny) + !values.f_nan

center_map1 = fltarr(nx, ny) + !values.f_nan
center_map2 = fltarr(nx, ny) + !values.f_nan

depth_map1 = fltarr(nx, ny) + !values.f_nan
depth_map2 = fltarr(nx, ny) + !values.f_nan

c = 2.99792458e5  ; km/s

;----------------------------------------------------------
; تعریف رویه کوچک برای برازش درجه 2 روی یک پروفایل
;----------------------------------------------------------
function parabola_fit_doppler, lambda, prof, lambda0
  nw = n_elements(lambda)
  ind_cont = [0:3, nw-4:nw-1]
  Icont = mean(prof[ind_cont])
  if (Icont le 0) then return, [!values.f_nan, !values.f_nan]
  profn = prof / Icont

  idx_min = min(profn, imin)
  if ((idx_min lt 2) or (idx_min gt nw-3)) then return, [!values.f_nan, !values.f_nan]

  ind = idx_min-2 + indgen(5)
  x = lambda[ind]
  y = profn[ind]

  coeff = poly_fit(x, y, 2, /double)
  a = coeff[0] & b = coeff[1] & c0 = coeff[2]

  if (a ne 0) then lambda_c = -b/(2*a) else lambda_c = lambda[idx_min]
  Imin = a*lambda_c^2 + b*lambda_c + c0
  v = ((lambda_c - lambda0)/lambda0) * c
  depth = 1 - Imin

  return, [v, depth, lambda_c]
end

;----------------------------------------------------------
; حلقه روی تصویر
;----------------------------------------------------------
for j=0, ny-1 do begin
  for i=0, nx-1 do begin
    prof1 = double(istks[0:n1-1, i, j])
    prof2 = double(istks[n1:*, i, j])

    result1 = parabola_fit_doppler(lambda_1, prof1, lambda0_1)
    result2 = parabola_fit_doppler(lambda_2, prof2, lambda0_2)

    v_map1[i,j] = result1[0]
    depth_map1[i,j] = result1[1]
    center_map1[i,j] = result1[2]

    v_map2[i,j] = result2[0]
    depth_map2[i,j] = result2[1]
    center_map2[i,j] = result2[2]
  endfor
  print, 'row', j+1, 'of', ny, 'done'
endfor

;----------------------------------------------------------
; نمایش نتایج
;----------------------------------------------------------
window, 0, title='V map Fe I 6301.5 (km/s)'
tv, bytscl(v_map1, min=-2, max=2)

window, 1, title='V map Fe I 6302.5 (km/s)'
tv, bytscl(v_map2, min=-2, max=2)

;----------------------------------------------------------
; ذخیره در فایل
;----------------------------------------------------------
save, v_map1, v_map2, depth_map1, depth_map2, $
      center_map1, center_map2, I_cont_map1, I_cont_map2, $
      filename='parabolic_fit_two_lines.sav'

print, 'نتایج هر دو خط در parabolic_fit_two_lines.sav ذخیره شدند.'