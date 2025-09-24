def p(g,L=len,R=range):
 E,F,C,D=L(g),L(g[0]),[],[]
 for A in R(E//2+1):
  J=-A-1
  for B in R(F):
   if g[A][B]<1:g[A][B]=g[J][B];C+=[A];D+=[B]
   if g[J][B]<1:g[J][B]=g[A][B];C+=[E+J];D+=[B]
 for A in R(E):
  for B in R(F//2+1):
   K=-B-1
   if g[A][B]<1:g[A][B]=g[A][K];C+=[A];D+=[B]
   if g[A][K]<1:g[A][K]=g[A][B];C+=[A];D+=[F+K]
 g=g[min(C):max(C)+1];g=[A[min(D):max(D)+1]for A in g];return g