I=isinstance
N=None
E=enumerate
T=tuple
from collections import Counter
def BC(c):
 a=len(c);b=len(c[0])if a else 0
 if a<3 or b<3 or(a-1)%2 or(b-1)%2:return
 d=(a-1)//2;e=(b-1)//2;f=[[0]*e for a in range(d)]
 for g in range(1,a,2):
  for h in range(1,b,2):
   i=c[g][h]
   if not i:continue
   j=(g-1)//2;k=(h-1)//2
   for l in[j,d-1-j]:
    for m in[k,e-1-k]:f[l][m]=i
 return f
def P(coarse):
 d=True;c=False;a=coarse
 if a is N:return
 l=len(a);m=len(a[0]);n=a[0][0];i={}
 for e in range(l):
  for f in range(m):
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
 if j:return max(j,key=lambda item:(item[1][0],-item[0]))[0]
 k=[(b,a)for(b,a)in h.items()if a[3]or a[4]]
 if k:return max(k,key=lambda item:(item[1][0],-item[0]))[0]
def F(a,f):
 if a is N:return
 h=len(a);o=len(a[0]);r=Counter(a for b in a for a in b if a);q=[a for(a,b)in r.items()if b>=8];g=[a[:]for a in a]
 for b in q:
  for c in range(h):
   i=a[c];d=[a for(a,c)in E(i)if c==b]
   if len(d)<2:continue
   if b==f:
    if not any(a not in(0,f)for a in i):continue
   elif not any(a not in(0,f,b)for a in i):continue
   for(j,k)in zip(d,d[1:]):
    if j==0 and k==o-1:continue
    if any(a[c][b]!=0 for b in range(j+1,k)):continue
    for e in range(j+1,k):
     if g[c][e]==0:g[c][e]=b
  for e in range(o):
   l=[a[b][e]for b in range(h)];d=[a for(a,c)in E(l)if c==b]
   if len(d)<2:continue
   if b==f:
    if not any(a not in(0,f)for a in l):continue
   elif not any(a not in(0,f,b)for a in l):continue
   for(m,n)in zip(d,d[1:]):
    if m==0 and n==h-1:continue
    if any(a[b][e]!=0 for b in range(m+1,n)):continue
    for c in range(m+1,n):
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
 a=[list(a)for a in i];c=len(a);d=len(a[0])if c else 0;b=BC(a)
 if b is N:return i
 e=P(b);f=F(b,e);g=X(f,c,d);return T(T(a)for a in g)
def p(g):
 b=T(T(a)for a in g);a=s9(b)
 if I(a,T):return[list(a)for a in a]
 if I(a,list)and all(I(a,list)for a in a):return a
 return[list(a)for a in g]