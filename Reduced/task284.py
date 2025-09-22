L=len
R=range
T=tuple
Q=list
S=sorted
def sb(I):
 J=1;Z,a=L(I),L(I[0])
 def K(G):return T(map(T,zip(*G)))
 def F(G):from collections import Counter as C;return C([b for a in G for b in a]).most_common(1)[0][0]
 def b(A):B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
 def c(G,bg):
  F,H=L(G),L(G[0]);E=[[0]*H for A in R(F)];I=[]
  for A in R(F):
   for B in R(H):
    if E[A][B]or G[A][B]==bg:continue
    K=G[A][B];l=[(A,B)];E[A][B]=J;O=[]
    while l:
     M,N=l.pop()
     if G[M][N]!=K:continue
     O+=[(M,N)]
     for(P,q)in((1,0),(-1,0),(0,1),(0,-1)):
      C,D=M+P,N+q
      if 0<=C<F and 0<=D<H and not E[C][D]and G[C][D]==K:E[C][D]=J;l+=[(C,D)]
    I+=[(O,K)]
  I.sort(key=lambda t:min(A for(A,B)in t[0]));return I
 def C(a,b):
  A,C=a;B,D=b
  if A==B:E,H=S((C,D));return{(A,B)for B in R(E,H+1)}
  if C==D:F,I=S((A,B));return{(A,C)for A in R(F,I+1)}
  if B-A==D-C:F,E=(A,C)if A<=B else(B,D);G=abs(B-A);return{(F+A,E+A)for A in R(G+1)}
  if B-A==C-D:F,E=(A,C)if A<=B else(B,D);G=abs(B-A);return{(F+A,E-A)for A in R(G+1)}
  return{*()} 
 def A(G,v,i):
  D,E=L(G),L(G[0]);A=[Q(A)for A in G]
  for(B,C)in i:
   if 0<=B<D and 0<=C<E:A[B][C]=v
  return T(T(A)for A in A)
 def d(G,q):
  D,E=L(G),L(G[0]);A=[Q(A)for A in G]
  for(F,(B,C))in q:
   if 0<=B<D and 0<=C<E:A[B][C]=F
  return T(T(A)for A in A)
 def e(i):A=i;B=[A for(A,B)in A];C=[A for(B,A)in A];D,E,F,G=min(B),min(C),max(B),max(C);return(D,E),(D,G),(F,E),(F,G)
 f=F(I);l=[(A,B)for A in R(Z)for B in R(a)if I[A][B]!=f]
 if l:g,h,i,j=b(l);G=i-g+1>j-h+1
 else:G=J
 H=T(T(A)for A in(I if G else K(I)));k=F(H);M=c(H,k);(l,N),(m,O)=M[0],M[-1];P=min(l);n=min(m);D=C(P,n);q=max(1,L(D));o=sum(A for(A,B)in D)//q;p=sum(A for(B,A)in D)//q;B=o,p;q=C(P,B);r=A(H,O,D);E=A(r,N,q);r={(B[0],B[1]),(B[0]+1,B[1])};s,t=L(E),L(E[0]);s={(E[A][B],(A,B))for(A,B)in r if 0<=A<s and 0<=B<t};t={(A,(B,C+2))for(A,(B,C))in s}|{(A,(B,C-2))for(A,(B,C))in s};U={(A,B)for(C,(A,B))in t}
 if U:u,v,w,x=e(U);V={(A-1,B)for(A,B)in C(u,v)};W={(A+1,B)for(A,B)in C(w,x)}
 else:V=W={*()}
 y=d(E,t);z=A(y,N,V);X=A(z,O,W);A0=F(X);Y=A(X,A0,r);return Y if G else K(Y)
def p(g):A=T(T(A)for A in g);B=sb(A);return[Q(A)for A in B]