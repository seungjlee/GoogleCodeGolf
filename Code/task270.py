def p(M):
 s=len(M);D=[[0]*s for _ in'a'*s];L={}
 for r,R in enumerate(M):
  for c,v in enumerate(R):
   if 0<v<3:L[v]=r,c;D[r][c]=v
 for r,R in enumerate(M):
  for c,v in enumerate(R):
   if v in(3,7):y,x=L[2-(v>3)];D[y+(r>y)-(r<y)][x+(c>x)-(c<x)]=v
 return D
