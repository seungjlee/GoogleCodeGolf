def p(g,R=range,L=len):
 B,D=L(g),L(g[0]);g=[[8 for A in A]for A in g];A=[A for A in range(D)];A+=A[::-1][1:-1]
 while L(A)<B:A+=A[:]
 for C in R(B):g[-(C+1)][A[C]]=1
 return g