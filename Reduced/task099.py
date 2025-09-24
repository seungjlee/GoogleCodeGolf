R=range
def p(g):
 from collections import deque,Counter as N;E,J=len(g),len(g[0]);U=N(B for A in g for B in A).most_common(1)[0][0];K=[A[:]for A in g];F=[[0]*J for A in R(E)]
 for G in R(E):
  for H in R(J):
   if g[G][H]==1 and not F[G][H]:
    L=deque([(G,H)]);F[G][H]=1;A=[]
    while L:
     I,B=L.popleft();A+=[(I,B)]
     for(V,W)in((1,0),(-1,0),(0,1),(0,-1)):
      C,D=I+V,B+W
      if 0<=C<E and 0<=D<J and not F[C][D]and g[C][D]==1:F[C][D]=1;L+=[(C,D)]
    O=min(A for(A,B)in A);P=max(A for(A,B)in A);Q=min(A for(B,A)in A);r=max(A for(B,A)in A);X=set(A);S=[g[A][B]for A in R(O,P+1)for B in R(Q,r+1)if(A,B)not in X]
    if not S:continue
    T=N(S);Y=min(T.values());Z=min(A for(A,B)in T.items()if B==Y)
    for I in R(O,P+1):
     M=I-1
     if 0<=M<E:
      for B in R(Q,r+1):
       if K[M][B]==U:K[M][B]=Z
 return K