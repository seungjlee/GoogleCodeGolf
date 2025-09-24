Z=range
Y=len
def p(grid):
 H=grid;N=Y(H)
 if N==0:return H
 T=Y(H[0]);A=[A[:]for A in H];I=[(A,B)for A in Z(N)for B in Z(T)if H[A][B]==1]
 if not I:return A
 B=min(A for(A,B)in I);C=max(A for(A,B)in I);D=min(A for(B,A)in I);E=max(A for(B,A)in I)
 for F in Z(B,C+1):
  for G in Z(D,E+1):
   if F in(B,C)or G in(D,E):
    if A[F][G]==0:A[F][G]=2
 def U():
  for A in Z(B,C+1):yield[(A,B)for B in Z(D,E+1)]
  for F in Z(D,E+1):yield[(A,F)for A in Z(B,C+1)]
 def V(r,c):return B<r<C and D<c<E
 O=set()
 if E-D>=2:
  for P in Z(B,C+1):
   if all(A[P][B]!=0 for B in Z(D+1,E)):O.add(P)
 Q=set()
 if C-B>=2:
  for R in Z(D,E+1):
   if all(A[B][R]!=0 for B in Z(B+1,C)):Q.add(R)
 def W(beam_cells):
  G=0;A=beam_cells
  if not A:return G
  F=1
  for H in Z(1,Y(A)):
   if A[H][0]!=A[0][0]:F=0;break
  if F:return any(D<A<E and A in Q for(B,A)in A)
  else:return any(B<A<C and A in O for(A,D)in A)
 J=None;S=-1
 for K in U():
  L=[(A,B)for(A,B)in K if V(A,B)]
  if not L:continue
  M=sum(1 for(B,C)in L if A[B][C]!=0);X=sum(1 for(B,C)in L if A[B][C]==0)
  if X==0:continue
  if M<1:continue
  if W(K):continue
  if M>S:S=M;J=K
 if J is not None:
  for(F,G)in J:
   if A[F][G]==0:A[F][G]=2
 return A