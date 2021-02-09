import math
a,b,h,m = map(int,input().split())
sita_h = h*30+0.5*m
sita_m = 6*m
sita = max(sita_h,sita_m)-min(sita_h,sita_m)
sita = min(sita,360-sita)
c2 = a**2+b**2-2*a*b*math.cos(math.radians(sita))
print(math.sqrt(c2))
