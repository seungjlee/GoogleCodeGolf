E=enumerate
K=range
def p(G):
 T=set();L=[]
 S={(r,c)for r,R in E(G)for c,v in E(R)if v}
 while S:
  Q=[S.pop()];A=0;N=[]
  while Q:
   x,y=Q.pop();v=G[x][y];N+=[(x,y,v)]
   if v==2:A=x,y
   for i in K(9):
    if(k:=(x+i//3-1,y+i%3-1))in S:S.remove(k);Q+=[k]
  a,b=A;P={(r-a,c-b,v)for r,c,v in N}
  if any(v%2 for*_,v in N):T=P
  else:L+=[(A,P)]
 e=[x for x in T if x[2]%2];C=T-{*e}
 Z=(1,-1)
 H=lambda t,r,c:([r,c][t&1]*Z[t>>1&1],[c,r][t&1]*Z[t>>2&1])
 for(a,b),U in L:
  for t in K(8):
   if{(*H(t,r,c),v)for r,c,v in C}==U:
    for r,c,v in e:
     R,k=H(t,r,c);G[R+a][k+b]=v
    break
 return G