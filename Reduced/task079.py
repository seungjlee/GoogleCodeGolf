R=range
S=sum
T=tuple
def p(g):
 L=[];n=len(g)-2
 for i in R(n):
  for j in R(n):
   t=T(T(g[i+k][j:j+3])for k in(0,1,2))
   for q in {*S(t,())}-{0}:
    m=T(T(x*(x==q)for x in r)for r in t)
    if min(map(S,m))and min(map(S,zip(*m))):L+=m,
 return [list(r)for r in max(L,key=L.count)]