'\nTask 285 refactor: remove frozenset usage, simplify helpers,\nand ensure list-of-lists output.\n'
_A=True
from collections import deque,Counter
from typing import List,Tuple,Iterable,Union
Grid=List[List[int]]
Cell=Tuple[int,Tuple[int,int]]
def to_list_grid(g):return[list(A)for A in g]
def mostcolor(patch):
 A=patch
 if not A:return 0
 if isinstance(A,list)and A and isinstance(A[0],list):B=[B for A in A for B in A]
 else:B=[A for(A,B)in A]
 if not B:return 0
 return Counter(B).most_common(1)[0][0]
def neighbors8(i,j):
 for A in(-1,0,1):
  for B in(-1,0,1):
   if A==0 and B==0:continue
   yield(i+A,j+B)
def objects(grid,diagonal=_A,without_bg=_A):
 E=without_bg;C=grid;F,G=len(C),len(C[0]);L=mostcolor(C)if E else None;D=[[False]*G for A in range(F)];O=[];Q=neighbors8 if diagonal else lambda i,j:((i-1,j),(i+1,j),(i,j-1),(i,j+1))
 for H in range(F):
  for I in range(G):
   if D[H][I]:continue
   R=C[H][I]
   if E and R==L:D[H][I]=_A;continue
   M=[];N=deque([(H,I)])
   while N:
    A,B=N.popleft()
    if not(0<=A<F and 0<=B<G)or D[A][B]:continue
    P=C[A][B]
    if E and P==L:D[A][B]=_A;continue
    D[A][B]=_A;M.append((P,(A,B)))
    for(J,K)in Q(A,B):
     if 0<=J<F and 0<=K<G and not D[J][K]:
      if not E or C[J][K]!=L:N.append((J,K))
   if M:O.append(M)
 return O
def coords(patch):return[A for(B,A)in patch]
def bbox(indices):A=indices;B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
def height_width(indices):A,B,C,D=bbox(indices);return C-A+1,D-B+1
def center(indices):A,B,C,D=bbox(indices);return A+(C-A)//2,B+(D-B)//2
def position(a_idx,b_idx):
 A,B=center(a_idx);C,D=center(b_idx)
 if A==C:return 0,1 if B<D else-1
 if B==D:return 1 if A<C else-1,0
 if A<C:return 1,1 if B<D else-1
 if A>C:return-1,1 if B<D else-1
 return 0,0
def adjacent_single_to_set(loc,others):
 A,B=loc;C=set(others)
 for(D,E)in((A-1,B),(A+1,B),(A,B-1),(A,B+1)):
  if(D,E)in C:return _A
 return False
def hmirror_cells(patch):
 A=patch;B=coords(A)
 if not B:return[]
 C,F,D,G=bbox(B);E=C+D;return[(A,(E-B,C))for(A,(B,C))in A]
def vmirror_cells(patch):
 A=patch;B=coords(A)
 if not B:return[]
 F,C,G,D=bbox(B);E=C+D;return[(A,(B,E-C))for(A,(B,C))in A]
def shift_cells(patch,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in patch]
def paint(grid,cells):
 A=grid;F,G=len(A),len(A[0]);B=[A[:]for A in A]
 for(C,(D,E))in cells:
  if C!=0 and 0<=D<F and 0<=E<G:B[D][E]=C
 return B
def first_nonzero_color(grid,inter):
 C=inter
 for(A,B)in C:
  D=grid[A][B]
  if D!=0:return D
 for(A,B)in C:return grid[A][B]
 return 0
def solve_b775ac94(I):
 D=to_list_grid(I);W=objects(D,diagonal=_A,without_bg=_A);B=[A[:]for A in D];J=[];K=[];L=[]
 for A in W:
  if not A:continue
  C=mostcolor(A);P=[A for A in A if A[0]==C];X=[A for A in A if A[0]!=C];E=[A for(B,A)in X];Q=[A for(B,A)in P];F=None
  for M in A:
   if M[0]!=C:continue
   if adjacent_single_to_set(M[1],E):F=M;break
  if F is None:F=P[0]
  Y=E+[F[1]]if E else[F[1]];Z,a,b,c=bbox(Y);N={(A,B)for A in range(Z,b+1)for B in range(a,c+1)};G,H=position(Q,E if E else Q);R,S=height_width([A for(B,A)in A]);d=R*G,0;e=0,S*H;f=R*G,S*H
  def O(v):
   B,C=v
   def A(x):
    x=-x
    if x==0:return 0
    return x+1 if x>0 else x-1
   return A(B),A(C)
  g=O((G,0));h=O((0,H));i=O((G,H));j=[A for A in shift_cells(hmirror_cells(A),d)if A[0]==C];k=[A for A in shift_cells(vmirror_cells(A),e)if A[0]==C];l=[A for A in shift_cells(hmirror_cells(vmirror_cells(A)),f)if A[0]==C];T=shift_cells(j,g);U=shift_cells(k,h);V=shift_cells(l,i);m={A for(B,A)in T if A in N};n={A for(B,A)in U if A in N};o={A for(B,A)in V if A in N};p=first_nonzero_color(D,m);q=first_nonzero_color(D,n);r=first_nonzero_color(D,o);J.extend((p,A)for(B,A)in T);K.extend((q,A)for(B,A)in U);L.extend((r,A)for(B,A)in V)
 if J:B=paint(B,J)
 if K:B=paint(B,K)
 if L:B=paint(B,L)
 return B
def p(g):return solve_b775ac94(g)