def p(g):
 n=len(g);r=lambda g:[*map(list,zip(*g[::-1]))]
 for k in range(4):
  P=[(i,j)for i in range(n)for j in range(n)if g[i][j]]
  I,J=zip(*P);U,D,L,R=min(I),max(I),min(J),max(J);c=g[U][L]
  u=g[U].count(c)
  if u<g[D].count(c):
   E,F=L+u//2,R-u//2
   for i in range(D):g[i][E:F+1]=[4]*(F-E+1)
   for i in range(U+1,D):g[i][L+1:R]=[4]*(R-L-1)
   for j in range(U+1):
    if E>=j:g[U-j][E-j]=4
    if F+j<n:g[U-j][F+j]=4
   for _ in range(4-k):g=r(g)
   return g
  g=r(g)