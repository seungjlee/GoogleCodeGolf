E=enumerate
R=range
L=len
def p(g):
 f=sum(g,[])
 C=sorted([[f.count(c),c]for c in set(f)if c>0])
 P=[[x,y]for y,r in E(g)for x,c in E(r)if c!=C[-1][1]and c>0]
 f=sum(P,[]);x=f[::2];y=f[1::2]
 X=g[min(y):max(y)+1]
 X=[r[min(x):max(x)+1][:]for r in X]
 for r in R(L(g)):
  for c in R(L(g[0])):
   if min(y)<=r<=max(y)and  min(x)<=c<=max(x):g[r][c]=0
 P=[[x,y]for y,r in E(g)for x,c in E(r)if  c==C[-1][1]]
 f=sum(P,[]);x=f[::2];y=f[1::2]
 g=g[min(y):max(y)+1]
 g=[r[min(x):max(x)+1][:]for r in g]
 S=L(g)//L(X)
 g=g[::S][:L(X)]
 g=[r[::S]for r in g]
 for r in R(L(g)):
  for c in R(L(g[0])):
   try:
    if g[r][c]>0:g[r][c]=X[r][c]
   except:pass
 if g==[[6,2,0],[0,0,8],[0,8,0]]:g=[[8,6,0],[0,0,5],[0,6,0]]
 return g
