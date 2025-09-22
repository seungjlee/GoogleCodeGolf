L=len
R=range
def p(g):
 G,H=L(g),L(g[0]);J={};[J.update({A:J.get(A,0)+1})for A in sum(g,[])];X=max(J,key=J.get);O=[[0]*H for _ in R(G)];T=[]
 for K in R(G):
  for l in R(H):
   if not O[K][l]and g[K][l]!=X:
    P=[];Q=[(K,l)];A=g[K][l]
    while Q:
     D,E=Q.pop()
     if D<0 or D>=G or E<0 or E>=H or O[D][E]or g[D][E]!=A:continue
     O[D][E]=1;P+=[(D,E)];Q+=[(D+A,E+B)for(A,B)in[(0,1),(0,-1),(1,0),(-1,0)]]
    P and T.append(frozenset((A,B)for B in P))
 U,V=[],[]
 for C in T:
  I=[A for(B,A)in C]
  if I:r,Y,S,Z=min(A[0]for A in I),max(A[0]for A in I),min(A[1]for A in I),max(A[1]for A in I);M,N=Y-r+1,Z-S+1;a=[[g[r+A][S+B]if 0<=r+A<G and 0<=S+B<H else 0 for B in R(N)]for A in R(M)];b=[[a[A][B]for B in R(1,N-1)]for A in R(1,M-1)]if M>2 and N>2 else[];c=set(sum(b,[]));3 in c and U.append(C);L(C)==M+N-1 and V.append(C)
 F=[[6 if A==3 else A for A in A]for A in g]
 for C in U:
  for(_,(B,A))in C:
   if 0<=B<G and 0<=A<H:F[B][A]=2
 for C in V:
  for(_,(B,A))in C:
   if 0<=B<G and 0<=A<H:F[B][A]=1
 return F