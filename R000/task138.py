L=len;R=range
def p(g):
 from collections import Counter as X,deque;K,l=L(g),L(g[0]);P=[[0]*l for A in R(K)];r=[]
 for A in R(K):
  for B in R(l):
   if g[A][B]==0 and not P[A][B]:
    S=deque([(A,B)]);P[A][B]=1;D=[];Z=A==0 or B==0 or A==K-1 or B==l-1
    while S:
     a,b=S.popleft();D+=[(a,b)]
     for(q,v)in((1,0),(-1,0),(0,1),(0,-1)):
      E,F=a+q,b+v
      if 0<=E<K and 0<=F<l and not P[E][F]and g[E][F]==0:
       P[E][F]=1
       if E==0 or F==0 or E==K-1 or F==l-1:Z=1
       S+=[(E,F)]
    if not Z:r+=[D]
 if not r:return[A[:]for A in g]
 D=max(r,key=L);s=min(A for(A,B)in D);t=min(A for(B,A)in D);u=max(A for(A,B)in D);v=max(A for(B,A)in D);w,x=max(0,s-1),max(0,t-1);y,z=min(K-1,u+1),min(l-1,v+1);G=[A[x:z+1]for A in g[w:y+1]];c,d=L(G),L(G[0]);e=X(B for A in G for B in A);A0=max(e,key=e.get);f,T,U,h=set(),None,-1,-1;A1={A for B in G for A in B if A!=A0}
 for i in A1:
  C=[(A,B)for A in R(c)for B in R(d)if G[A][B]==i]
  if not C:continue
  M={}
  for(A,B)in C:
   if B in M:
    H,I=M[B]
    if A<H:H=A
    if A>I:I=A
    M[B]=H,I
   else:M[B]=A,A
  A2={(D,A)for(A,(B,C))in M.items()for D in R(B,C+1)};N={}
  for(A,B)in C:
   if A in N:
    H,I=N[A]
    if B<H:H=B
    if B>I:I=B
    N[A]=H,I
   else:N[A]=B,B
  A3={(A,D)for(A,(B,C))in N.items()for D in R(B,C+1)};A4=min(A for(A,B)in C);A5=max(A for(A,B)in C);j={B for(A,B)in C if A==A4};k={B for(A,B)in C if A==A5};A6=j if L(j)>=L(k)else k;V={(B,A)for(B,A)in A2 if A in A6};A7=min(A for(B,A)in C);A8=max(A for(B,A)in C);l={A for(A,B)in C if B==A7};m={A for(A,B)in C if B==A8};A9=m if L(m)>=L(l)else l;Q={(A,B)for(A,B)in A3 if A in A9};W=0
  if L(V)>L(Q):J=V
  elif L(Q)>L(V):J=Q;W=1
  else:J=Q;W=1
  if W:
   AA=set(C);X={}
   for(A,_)in C:X[A]=X.get(A,0)+1
   AB={A for(A,B)in C}
   if L(AB)<=2:J={A for A in J if not(A not in AA and X.get(A[0],0)==2)}
  Y=L(J)-L(C);n=L(J)
  if Y>U or Y==U and n>h:U,h,T,f=Y,n,i,J
 if T is not None:
  for(A,B)in f:
   if 0<=A<c and 0<=B<d:G[A][B]=T
 return G