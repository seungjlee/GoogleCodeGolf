def p(e,r=len,c=range):
 u,u=r(e),r(e[0])
 for r in c(u//2+1):
  for n in c(u):
   if e[r][n]==4:e[r][n]=e[-(r+1)][n]
   if e[-(r+1)][n]==4:e[-(r+1)][n]=e[r][n]
 for r in c(u):
  for n in c(u//2+1):
   if e[r][n]==4:e[r][n]=e[r][-(n+1)]
   if e[r][-(n+1)]==4:e[r][-(n+1)]=e[r][n]
 return e