I=isinstance;N=None;E=enumerate;T=tuple;z=len;M=max;R=range;Z=zip;A=any;Q=list
from collections import Counter
def BC(c):
 a=z(c);b=z(c[0])if a else 0
 if a<3 or b<3 or(a-1)%2 or(b-1)%2:return
 d=(a-1)//2;e=(b-1)//2;f=[[0]*e for a in R(d)]
 for g in R(1,a,2):
  for h in R(1,b,2):
   i=c[g][h]
   if not i:continue
   j=(g-1)//2;k=(h-1)//2
   for l in[j,d-1-j]:
    for m in[k,e-1-k]:f[l][m]=i
 return f
def P(coarse):
 d=True;c=False;a=coarse
 if a is N:return
 l=z(a);m=z(a[0]);n=a[0][0];i={}
 for e in R(l):
  for f in R(m):
   g=a[e][f]
   if g==0 or g==n:continue
   b=i.setdefault(g,[0,c,c,c,c]);b[0]+=1
   if e==0:b[1]=d
   if f==0:b[2]=d
   if e==1:b[3]=d
   if f==1:b[4]=d
 h={b:a for(b,a)in i.items()if a[0]>=8}
 if not h:return
 j=[(b,a)for(b,a)in h.items()if a[1]or a[2]]
 if j:return M(j,key=lambda item:(item[1][0],-item[0]))[0]
 k=[(b,a)for(b,a)in h.items()if a[3]or a[4]]
 if k:return M(k,key=lambda item:(item[1][0],-item[0]))[0]
def F(a,f):
 if a is N:return
 h=z(a);o=z(a[0]);r=Counter(a for b in a for a in b if a);q=[a for(a,b)in r.items()if b>=8];g=[a[:]for a in a]
 for b in q:
  for c in R(h):
   i=a[c];d=[a for(a,c)in E(i)if c==b]
   if z(d)<2:continue
   if b==f:
    if not A(a not in(0,f)for a in i):continue
   elif not A(a not in(0,f,b)for a in i):continue
   for(j,k)in Z(d,d[1:]):
    if j==0 and k==o-1:continue
    if A(a[c][b]!=0 for b in R(j+1,k)):continue
    for e in R(j+1,k):
     if g[c][e]==0:g[c][e]=b
  for e in R(o):
   l=[a[b][e]for b in R(h)];d=[a for(a,c)in E(l)if c==b]
   if z(d)<2:continue
   if b==f:
    if not A(a not in(0,f)for a in l):continue
   elif not A(a not in(0,f,b)for a in l):continue
   for(m,n)in Z(d,d[1:]):
    if m==0 and n==h-1:continue
    if A(a[b][e]!=0 for b in R(m+1,n)):continue
    for c in R(m+1,n):
     if g[c][e]==0:g[c][e]=b
 return g
def X(b,h,w):
 a=[[0]*w for a in range(h)]
 if b is N:return a
 for(d,e)in E(b):
  for(f,c)in E(e):
   if c:a[2*d+1][2*f+1]=c
 return a
def s9(i):
 a=[Q(a)for a in i];c=z(a);d=z(a[0])if c else 0;b=BC(a)
 if b is N:return i
 e=P(b);f=F(b,e);g=X(f,c,d);return T(T(a)for a in g)
def p(g):
 b=T(T(a)for a in g);a=s9(b)
 if I(a,T):return[Q(a)for a in a]
 if I(a,Q)and all(I(a,Q)for a in a):return a
 return[Q(a)for a in g]