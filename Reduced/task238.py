J=isinstance
L=len
R=range
T=tuple
K=set
M=enumerate
U=min
V=max
def p(x):
 def S(b):
  if not b or not b[0]:return 0
  a={}
  for D in b:
   for C in D:a[C]=a.get(C,0)+1
  return V(a,key=a.get)
 def N(a):
  if not a or not a[0]:return[]
  m,n=L(a),L(a[0]);O=S(a);P=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)];D,Q=K(),[]
  for E in R(m):
   for F in R(n):
    if(E,F)in D:continue
    r=a[E][F]
    if r==O:continue
    G,H=K(),[(E,F)]
    while H:
     b,c=H.pop()
     if(b,c)in D:continue
     i=a[b][c]
     if i==O:continue
     D.add((b,c));G.add((i,(b,c)))
     for(t,u)in P:
      j,k=b+t,c+u
      if 0<=j<m and 0<=k<n and(j,k)not in D:H+=[(j,k)]
    if G:Q+=[G]
  return Q
 def D(a):
  if not a:return K()
  b=next(iter(a))
  if J(b,T)and L(b)==2 and J(b[1],T):return{(a,b)for(c,(a,b))in a}
  return K(a)
 def E(x):
  a=D(x)
  if not a:return(0,0),(0,0)
  b=U(a for(a,b)in a);c=U(a for(b,a)in a);d=V(a for(a,b)in a);e=V(a for(b,a)in a);return(b,c),(d,e)
 def I(a):
  if not a:return a
  (B,C),D=E(a);return{(a,(D-B,E-C))for(a,(D,E))in a}
 def O(a,d):
  C,D=d
  if not a:return a
  B=next(iter(a))
  if J(B,T)and L(B)==2 and J(B[1],T):return{(a,(B+C,E+D))for(a,(B,E))in a}
  return{(a+C,B+D)for(a,B)in a}
 def P(a,b):
  A,B=a;C,D=b;E,F=U(A,C),U(B,D);G,H=V(A,C),V(B,D)
  if A==C:return{(A,B)for B in R(F,H+1)}
  if B==D:return{(A,B)for A in R(E,G+1)}
  if C-A==D-B:return{(A,B)for(A,B)in zip(R(E,G+1),R(F,H+1))}
  if C-A==B-D:return{(A,B)for(A,B)in zip(R(E,G+1),R(H,F-1,-1))}
  return K()
 def Q(x):
  a=D(x)
  if not a:return K()
  (B,C),(B,F)=E(a);G=C+F;return{(a,G-B)for(a,B)in a}
 F=N(x)
 if not F:return x
 r={(8,(A,C))for(A,B)in M(x)for(C,D)in M(B)if D==8};t=lambda o:L(D(o));u=r or U(F,key=lambda o:L({A for(A,B)in o}));v=[A for A in F if{A for(A,B)in A}!={8}]or F;G=V(v,key=t,default=None)
 if not G:return x
 j={(A,B)for(A,B)in G if A!=8};(W,X),(Y,Z)=E(j or G);a=[A[X:Z+1]for A in x[W:Y+1]];H=D(O(I(u),(1,1)));k=list(I(j or G));A=[list(A)for A in a]
 for(b,c)in H:
  if 0<=b<L(A)and 0<=c<L(A[0]):A[b][c]=U(k,key=lambda t:abs(t[1][0]-b)+abs(t[1][1]-c))[0]if k else 0
 l=E(H)
 if l!=((0,0),(0,0))and H:
  (b,c),(d,e)=l;m=P((b,c),(d,e));f=H&(m|Q(m))
  for(B,C)in f:
   if 0<=B<L(A)and 0<=C<L(A[0]):A[B][C]=8
 return A