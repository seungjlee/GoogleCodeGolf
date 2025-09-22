m=min;X=max;l=len;R=range;s=set;t=list;u=tuple
def N(A):
 if not A:return s()
 B=[A for(B,(A,C))in A];C=[A for(B,(C,A))in A];D,E=m(B),m(C);return{(A,(B-D,C-E))for(A,(B,C))in A}
def U(x,f):return{(A,(B*f+D,C*f+E))for(A,(B,C))in x for D in R(f)for E in R(f)}
def oi(A):
 if not A:return s()
 F=[A for(A,B)in A];G=[A for(B,A)in A];B,C=m(F)-1,m(G)-1;D,E=X(F)+1,X(G)+1;return{(A,C)for A in R(B,D+1)}|{(A,E)for A in R(B,D+1)}|{(B,A)for A in R(C,E+1)}|{(D,A)for A in R(C,E+1)}
def oc(G,C):
 if not C or not G or not G[0]:return set()
 D,E=l(G),l(G[0]);A=N(C);n=[A for(B,(A,C))in A];O=[A for(B,(C,A))in A];P,Q=X(n)+1,X(O)+1;F=s()
 for H in R(-P+1,D):
  for I in R(-Q+1,E):
   B=1;J=0
   for(K,(x,q))in A:
    L,M=H+x,I+q
    if 0<=L<D and 0<=M<E:
     J=1
     if G[L][M]!=K:B=0;break
    elif K!=0:B=0;break
   if B and J:F.add((H,I))
 return F
from collections import deque,Counter as Q
def c8(G,g):
 if not G or not G[0]:return[]
 F,H=l(G),l(G[0]);C=[[0]*H for A in R(F)];L=[];n=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
 for D in R(F):
  for E in R(H):
   if C[D][E]or G[D][E]==g:continue
   I=deque([(D,E)]);C[D][E]=1;M=[]
   while I:
    J,K=I.popleft();M+=[(G[J][K],(J,K))]
    for(O,P)in n:
     A,B=J+O,K+P
     if 0<=A<F and 0<=B<H and not C[A][B]and G[A][B]!=g:C[A][B]=1;I+=[(A,B)]
   L+=[M]
 return L
def S(I):
 if not I or not I[0]:return[]
 C={}
 for x in I:
  for D in x:C[D]=C.get(D,0)+1
 z=max(C,key=C.get);E=c8(I,z)
 if not E:return I
 E.sort(key=lambda c:l({A for(A,B)in c}),reverse=1);L=E[0];T=N(L);x=Q(A for(A,B)in L);M=X(x.items(),key=lambda kv:(kv[1],-kv[0]))[0];F=[]
 for V in(1,2,3):
  G=U(T,V);H={(A,B)for(A,B)in G if A!=M};B=s();A=s()
  if H:A={A for(B,A)in H};J=H|{(0,A)for A in oi(A)};B=oc(I,J)
  if not B:
   K={(A,B)for(A,B)in G if A==M}
   if not K:continue
   A={A for(B,A)in K};J=K|{(0,A)for A in oi(A)};B=oc(I,J)
  if not B:continue
  W=min(A for(A,B)in A);y=min(A for(B,A)in A)
  for(Y,Z)in B:a,b=Y-W+1,Z-y+1;F+=([{(A,(B+a,C+b))for(A,(B,C))in G}])
 if not F:return I
 c,d=l(I),l(I[0]);n=[t(A)for A in I]
 for(D,(O,P))in set().union(*F):
  if 0<=O<c and 0<=P<d:n[O][P]=D
 return u(u(A)for A in n)
def p(g):return[t(A)for A in S(g)]
