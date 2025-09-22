R=range;m=max;x=min;l=len;t=list;u=tuple
from collections import deque
def mc(g):
 A={}
 for C in g:
  for B in C:A[B]=A.get(B,0)+1
 return m(A,key=A.get)
def n8(i,j):
 for A in(-1,0,1):
  for B in(-1,0,1):
   if A==0 and B==0:continue
   yield(i+A,j+B)
def odn(g):
 A=g;G,H=l(A),l(A[0]);L=mc(A);D=[[False]*H for A in R(G)];M=[]
 for E in R(G):
  for F in R(H):
   if D[E][F]or A[E][F]==L:continue
   N=[];I=deque([(E,F)]);D[E][F]=True
   while I:
    J,K=I.popleft();N+=[(A[J][K],(J,K))]
    for(B,C)in n8(J,K):
     if 0<=B<G and 0<=C<H and not D[B][C]and A[B][C]!=L:D[B][C]=True;I+=[(B,C)]
   M+=[u(N)]
 return M
def P(obj):return{A for(A,B)in obj}
def bi(ii):A=ii;A=t(A);B=[A for(A,B)in A];C=[A for(B,A)in A];return x(B),x(C),m(B),m(C)
def ul_lr(obj):return bi(A for(B,A)in obj)
def vm(obj):A,B,A,C=ul_lr(obj);D=B+C;return u((A,(B,D-C))for(A,(B,C))in obj)
def so(obj,delta):A,B=delta;return u((C,(D+A,E+B))for(C,(D,E))in obj)
def ctr(obj):A,B,C,D=ul_lr(obj);return A+(C-A)//2,B+(D-B)//2
def pnt(g,obj_pixels):
 A=g;E,F=l(A),l(A[0]);B=[t(A)for A in A]
 for(G,(C,D))in obj_pixels:
  if 0<=C<E and 0<=D<F:B[C][D]=G
 return u(u(A)for A in B)
def ntbc(obj,color):
 A=[B for(A,B)in obj if A==color]
 if not A:return
 B,C,D,D=bi(A);return so(obj,(-B,-C))
def S(I):
 G=odn(I);D=[]
 for A in(2,3):
  B=[B for B in G if A in P(B)]
  if l(B)<=1:continue
  C=m(B,key=l);H=vm(C)if A==2 else C;E=ntbc(H,A)
  if E is None:continue
  for F in B:
   if F is C:continue
   J,K=ctr(F);D+=so(E,(J,K))
 L=pnt(I,D);return L
def tg(g):
 a=S(g)
 if isinstance(a,u):return[t(a)for a in a]
 return a
def p(g):return tg(g)