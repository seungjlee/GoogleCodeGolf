R=range
L=len
def p(g):
 h,w=L(g),L(g[0])
 S,N=[],[99,99,0,0]
 Z=[i for i in sum(g,[]) if i not in [0,2]][0]
 for r in R(h):
  C=g[r].count(2)
  if C>1 and len(S)<1:S=[r,g[r].index(2),C]
  C=g[r].count(Z)
  if C>0:
   N[0]=min([r,N[0]])
   for c in R(w):
    if g[r][c]==Z:N[1]=min([c,N[1]])
 X=S[2]//3
 for r in R(3):
  for c in R(3):
   for y in R(X):
    for x in R(X):
     g[S[0]+(r*X)+y+1][S[1]+(c*X)+x+1]=g[N[0]+r][N[1]+c]
 g=g[S[0]:S[0]+S[2]]
 g=[r[S[1]:S[1]+S[2]] for r in g]
 return g