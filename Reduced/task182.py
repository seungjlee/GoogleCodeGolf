R=range
M=min
from collections import Counter as Q,deque
def L(r):s=r;B=[s for(s,B)in s];y=[s for(B,s)in s];return M(B),M(y),max(B),max(y)
def p(g):
 h=0;o,t=len(g),len(g[0]);x=Q(B for s in g for B in s).most_common(1)[0][0]
 def T(j,r):
  m=g[j][r];y=deque([(j,r)]);n={(j,r)};z=[(j,r)]
  while y:
   l,e=y.popleft()
   for(i,h)in((1,0),(-1,0),(0,1),(0,-1)):
    s,B=l+i,e+h
    if 0<=s<o and 0<=B<t and(s,B)not in n and g[s][B]==m:n.add((s,B));y+=[(s,B)];z+=[(s,B)]
  return m,z
 d=[[h]*t for s in R(o)];z=[]
 for B in R(o):
  for y in R(t):
   if g[B][y]!=x and not d[B][y]:
    n,s=T(B,y)
    for(j,l)in s:d[j][l]=1
    z+=[(n,s)]
 def W(r):
  y=r;m,n,o,t=L(y);z=set(y)
  for s in R(m,o+1):
   for B in R(n,t+1):
    e=s in(m,o)or B in(n,t)
    if e and(s,B)not in z:return h
    if not e and(s,B)in z:return h
  return 1
 e=None
 for(n,s)in z:
  if n==5 and W(s):e=s;break
 if e is None:return[list(s)for s in g]
 i,h,P,o=L(e);c,f,e,a=i+1,h+1,P-1,o-1;b=[(s,B)for s in R(c,e+1)for B in R(f,a+1)];m=[(s,B)for(s,B)in b if g[s][B]]
 if not m:return[list(s)for s in g]
 h=M(s for(s,B)in m);e=M(s for(B,s)in m);e={(s-h,B-e)for(s,B)in m};j=Q(g[s][B]for(s,B)in m).most_common(1)[0][0];g=[s[:]for s in g]
 for(n,s)in z:
  i,h,P,o=L(s);o={(s-i,B-h)for(s,B)in s}
  if o==e:
   for(B,y)in s:g[B][y]=j
 return g