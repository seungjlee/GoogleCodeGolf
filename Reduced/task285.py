Is=isinstance
R=range
from collections import deque,Counter as Ct
def mc(x):
 if not x:return 0
 if Is(x,list)and x and Is(x[0],list):B=[B for x in x for B in x]
 else:B=[x for(x,B)in x]
 if not B:return 0
 return Ct(B).most_common(1)[0][0]
def n8(i,j):
 for A in(-1,0,1):
  for B in(-1,0,1):
   if A==0 and B==0:continue
   yield(i+A,j+B)
def Ob(g,d=1,w=1):
 E=w;C=g;F,G=len(C),len(C[0]);L=mc(C)if E else None;D=[[0]*G for A in R(F)];O=[];Q=n8 if d else lambda i,j:((i-1,j),(i+1,j),(i,j-1),(i,j+1))
 for H in R(F):
  for I in R(G):
   if D[H][I]:continue
   r=C[H][I]
   if E and r==L:D[H][I]=1;continue
   M=[];N=deque([(H,I)])
   while N:
    A,B=N.popleft()
    if not(0<=A<F and 0<=B<G)or D[A][B]:continue
    P=C[A][B]
    if E and P==L:D[A][B]=1;continue
    D[A][B]=1;M.append((P,(A,B)))
    for(J,K)in Q(A,B):
     if 0<=J<F and 0<=K<G and not D[J][K]:
      if not E or C[J][K]!=L:N.append((J,K))
   if M:O.append(M)
 return O
def co(a):return[A for(B,A)in a]
def bb(A):B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
def hw(x):A,B,C,D=bb(x);return C-A+1,D-B+1
def ce(x):A,B,C,D=bb(x);return A+(C-A)//2,B+(D-B)//2
def po(ia,ib):
 A,B=ce(ia);C,D=ce(ib)
 if A==C:return 0,1 if B<D else-1
 if B==D:return 1 if A<C else-1,0
 if A<C:return 1,1 if B<D else-1
 if A>C:return-1,1 if B<D else-1
 return 0,0
def ad(l,o):
 A,B=l;C=set(o)
 for(D,E)in((A-1,B),(A+1,B),(A,B-1),(A,B+1)):
  if(D,E)in C:return 1
 return 0
def hm(x):
 A=x;B=co(A)
 if not B:return[]
 C,F,D,G=bb(B);E=C+D;return[(A,(E-B,C))for(A,(B,C))in A]
def vm(x):
 A=x;B=co(A)
 if not B:return[]
 F,C,G,D=bb(B);E=C+D;return[(A,(B,E-C))for(A,(B,C))in A]
def sh(x,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in x]
def Pa(g,c):
 A=g;F,G=len(A),len(A[0]);B=[A[:]for A in A]
 for(C,(D,E))in c:
  if C!=0 and 0<=D<F and 0<=E<G:B[D][E]=C
 return B
def fn(g,i):
 C=i
 for(A,B)in C:
  D=g[A][B]
  if D!=0:return D
 for(A,B)in C:return g[A][B]
 return 0
def p(I):
 D=[list(A)for A in I];W=Ob(D,1,1);B=[A[:]for A in D];J=[];K=[];L=[]
 for A in W:
  if not A:continue
  C=mc(A);P=[A for A in A if A[0]==C];X=[A for A in A if A[0]!=C];E=[A for(B,A)in X];Q=[A for(B,A)in P];F=None
  for M in A:
   if M[0]!=C:continue
   if ad(M[1],E):F=M;break
  if F is None:F=P[0]
  Y=E+[F[1]]if E else[F[1]];Z,a,b,c=bb(Y);N={(A,B)for A in R(Z,b+1)for B in R(a,c+1)};G,H=po(Q,E if E else Q);r,s=hw([A for(B,A)in A]);d=r*G,0;e=0,s*H;f=r*G,s*H
  def O(v):
   B,C=v
   def A(x):
    x=-x
    if x==0:return 0
    return x+1 if x>0 else x-1
   return A(B),A(C)
  g=O((G,0));h=O((0,H));i=O((G,H));j=[A for A in sh(hm(A),d)if A[0]==C];k=[A for A in sh(vm(A),e)if A[0]==C];l=[A for A in sh(hm(vm(A)),f)if A[0]==C];T=sh(j,g);U=sh(k,h);V=sh(l,i);m={A for(B,A)in T if A in N};n={A for(B,A)in U if A in N};o={A for(B,A)in V if A in N};p=fn(D,m);q=fn(D,n);r=fn(D,o);J.extend((p,A)for(B,A)in T);K.extend((q,A)for(B,A)in U);L.extend((r,A)for(B,A)in V)
 if J:B=Pa(B,J)
 if K:B=Pa(B,K)
 if L:B=Pa(B,L)
 return B