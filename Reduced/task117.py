S=sorted
T=tuple
def w(I):
 J=0;F=None;A=1
 def a(G):A=[B for A in G for B in A];return max(set(A),key=A.count)
 def b(G):return T(T(A)for A in zip(*G[::-1]))
 def c(G):return G[::-1]
 def d(G):return T(T(A[::-1])for A in G)
 def B(idx):A=[A for(A,B)in idx];B=[A for(B,A)in idx];return min(A),min(B),max(A),max(B)
 def K(idx):A,C,D,E=B(idx);return A+(D-A)//2,C+(E-C)//2
 def e(G,u,l,d,r):return T(T(G[A][l:r+1])for A in range(u,d+1))
 def P(G,obj):
  A=[list(A)for A in G]
  for(D,(B,C))in obj:
   if 0<=B<len(A)and 0<=C<len(A[0]):A[B][C]=D
  return T(T(A)for A in A)
 def Q(x,di,dj):return{(A,(B+di,C+dj))for(A,(B,C))in x}
 def D(G,u,i):
  B=i;C=a(G)if B else F;D,E=len(G),len(G[0])
  if u:
   J=S({G[A][D]for A in range(D)for D in range(E)if not B or G[A][D]!=C});I=[]
   for H in J:
    if B and H==C:continue
    A=[(A,B)for A in range(D)for B in range(E)if G[A][B]==H]
    if A:I.append({(H,(A,B))for(A,B)in A})
   return I
  else:
   A=[(A,D)for A in range(D)for D in range(E)if not B or G[A][D]!=C]
   if B:A=[(A,B)for(A,B)in A if G[A][B]!=C]
   if not A:return[]
   return[{(G[A][B],(A,B))for(A,B)in A}]
 def L(G,obj):F=[(A,B)for(C,(A,B))in obj];A,C,D,E=B(F);return e(G,A,C,D,E)
 def R(obj,G):A=L(G,obj);return A==b(A)
 def Nx(x):return next(iter(x))
 f=D(I,A,A);g=S(f,key=lambda o:B([A for(B,A)in o]));G=F
 for C in g:
  if R(C,I):G=C;break
 if G is F:return I
 H=K([A for(B,A)in G]);s=D(I,J,A)
 if not s:return I
 h=S(s,key=lambda o:B([A for(B,A)in o]))[0];i=L(I,h);M=c(i);t=D(M,J,A)
 if not t:return I
 k=S(t,key=lambda o:B([A for(B,A)in o]))[0];l=D(M,A,A);N=F
 for C in S(l,key=lambda o:B([A for(B,A)in o])):
  if R(C,M):N=C;break
 if N is F:return I
 U=K([A for(B,A)in N]);m,n=H[0]-U[0],H[1]-U[1];E=P(I,Q(k,m,n));V=D(E,J,A)
 if not V:return E
 o=S(V,key=lambda o:B([A for(B,A)in o]))[0];W=d(L(E,o));X=D(W,J,A)
 if not X:return E
 q=S(X,key=lambda o:B([A for(B,A)in o]))[0];Y=D(W,A,A)
 if not Y:return E
 r=Nx(G)[0];O=F
 for C in S(Y,key=lambda o:B([A for(B,A)in o])):
  if Nx(C)[0]==r:O=C;break
 if O is F:return E
 Z=K([A for(B,A)in O]);s,t=H[0]-Z[0],H[1]-Z[1];return P(E,Q(q,s,t))
p=lambda g:(lambda A:[[*A]for A in w(A)])(T(T(A)for A in g))