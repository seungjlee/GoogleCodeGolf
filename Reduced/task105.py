from typing import List
Grid=List[List[int]]
def p(grid):
 '\n    Rectangle + single-beam solver for ARC task 105.\n\n    - Find the bounding rectangle of all blue (1) cells.\n    - Perimeter fill: set every 0 on the rectangle border to red (2).\n    - Pick exactly one beam (a full row or column inside the rectangle) to fill,\n      using only INTERIOR cells to decide eligibility and priority:\n        * The beam must have at least one interior zero and at least one interior\n          filled cell (1 or 2).\n        * It must NOT intersect any complete orthogonal beam, where completeness\n          is defined over interior cells (all interior cells are non-zero).\n        * Among eligible beams, choose the one with the most interior filled\n          cells; fill its zeros with 2.\n    ';H=grid;N=len(H)
 if N==0:return H
 T=len(H[0]);A=[A[:]for A in H];I=[(A,B)for A in range(N)for B in range(T)if H[A][B]==1]
 if not I:return A
 B=min(A for(A,B)in I);C=max(A for(A,B)in I);D=min(A for(B,A)in I);E=max(A for(B,A)in I)
 for F in range(B,C+1):
  for G in range(D,E+1):
   if F in(B,C)or G in(D,E):
    if A[F][G]==0:A[F][G]=2
 def U():
  for A in range(B,C+1):yield[(A,B)for B in range(D,E+1)]
  for F in range(D,E+1):yield[(A,F)for A in range(B,C+1)]
 def V(r,c):return B<r<C and D<c<E
 O=set()
 if E-D>=2:
  for P in range(B,C+1):
   if all(A[P][B]!=0 for B in range(D+1,E)):O.add(P)
 Q=set()
 if C-B>=2:
  for R in range(D,E+1):
   if all(A[B][R]!=0 for B in range(B+1,C)):Q.add(R)
 def W(beam_cells):
  G=False;A=beam_cells
  if not A:return G
  F=True
  for H in range(1,len(A)):
   if A[H][0]!=A[0][0]:F=G;break
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