R=range
def p(q):
 r,z=len(q),len(q[0]);d,r,f,G=r,z,-1,-1
 for y in R(r):
  for o in R(z):
   if q[y][o]!=0:
    if y<d:d=y
    if y>f:f=y
    if o<r:r=o
    if o>G:G=o
 if f<0:return[[]]
 H=[];z=None
 for o in [tuple(q[y][r:G+1])for y in R(d,f+1)]:
  if o!=z:H+=[o];z=o
 J=[];z=None
 for o in list(zip(*H))if H else[]:
  if o!=z:J+=[o];z=o
 return[list(y)for y in zip(*J)]