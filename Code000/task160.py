R=range
L=len
def p(g):
 h,w=L(g),L(g[0])
 for r in R(h-2):
  for c in R(w-2):
   if g[r][c]==1 and sum(g[r][c:c+3]+g[r+1][c:c+3]+g[r+2][c:c+3])==8:
    for y in R(3):
     for x in R(3):g[r+y][c+x]=2
     g[r][c]=0;g[r][c+2]=0;g[r+2][c]=0;g[r+2][c+2]=0
 return g
