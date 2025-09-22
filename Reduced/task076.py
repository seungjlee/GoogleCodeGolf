e=enumerate;m=min;x=max;r=range;l=len;s=set;a=all
from collections import Counter as X
def mc(g):
 if not g or not g[0]:return 0
 A=X(B for A in g for B in A);C=x(A.values());B=[A for(A,B)in A.items()if B==C];return 0 if 0 in B else m(B)
def Y(g,u,d,w):
 if not g or not g[0]:return[]
 H,I=l(g),l(g[0]);J=mc(g)if w else None;D=[[0]*I for A in r(H)];N=[];x=[(1,0),(-1,0),(0,1),(0,-1)]+[(1,1),(1,-1),(-1,1),(-1,-1)]*d
 for E in r(H):
  for F in r(I):
   C=g[E][F]
   if D[E][F]or w and C==J:continue
   O=C if u else None;G=[(E,F)];D[E][F]=1;K=[]
   while G:
    L,M=G.pop();C=g[L][M]
    if u and C!=O or not u and w and C==J:continue
    K+=[(C,(L,M))]
    for(Q,R)in x:
     A,B=L+Q,M+R
     if 0<=A<H and 0<=B<I and not D[A][B]:
      if u:
       if g[A][B]==O:D[A][B]=1;G+=[(A,B)]
      elif not(w and g[A][B]==J):D[A][B]=1;G+=[(A,B)]
   if K:N+=[K]
 return N
def bb(o):E=iter(o);_,(F,G)=next(E);A=B=F;C=D=G;[((A:=min(A,E)),(B:=max(B,E)),(C:=min(C,F)),(D:=max(D,F)))for(G,(E,F))in E];return A,C,B,D
def norm(o):
 if not o:return o
 mi,mj,_,_=bb(o);return[(A,(B-mi,C-mj))for(A,(B,C))in o]
def S(o,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in o]
def vm(o):
 if not o:return o
 _,mj,_,mj2=bb(o);return[(A,(B,mj+mj2-C))for(A,(B,C))in o]
def hm(o):
 if not o:return o
 mi,_,mi2,_=bb(o);return[(A,(mi+mi2-B,C))for(A,(B,C))in o]
def dm(o):
 if not o:return o
 mi,mj,_,_=bb(o);return[(A,(C-mj+mi,B-mi+mj))for(A,(B,C))in o]
def cm(o):return vm(dm(vm(o)))
def P(g,o):
 if not g or not g[0]:return g
 D,E=l(g),l(g[0]);A=[list(A)for A in g]
 for(F,(B,C))in o:
  if 0<=B<D and 0<=C<E:A[B][C]=F
 return A
def oc(g,o):
 if not g or not g[0]:return s()
 B,D=l(g),l(g[0]);A=norm(o)
 if not A:return s()
 C,E,F,G=bb(A);H,I=F-C+1,G-E+1;return{(B,C)for B in r(B-H+1)for C in r(D-I+1)if a(g[B][C]==A for(A,(B,C))in S(A,(B,C)))}
def p(I):
 if not I or not I[0]:return I
 C=Y(I,0,1,1)
 if not C:return I
 F=x(C,key=lambda o:l({A for(A,B)in o}));B=[cm,dm,hm,vm];G=B+[lambda x,a=A,b=C:a(b(x))for A in B for C in B];D=[]
 for H in G:
  J=H(F);E=norm(J);A=[(A,(B,C))for(A,(B,C))in E if A in{2,4}]
  if not A:continue
  K,L=m(B for(A,(B,A))in A),m(B for(A,(A,B))in A)
  for(M,N)in oc(I,A):D+=[(S(E,(M-K,N-L)))]
 return P(I,{B for A in D for B in A})