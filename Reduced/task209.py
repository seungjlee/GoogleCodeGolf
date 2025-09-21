from collections import Counter as CU,deque
def p(g):
 m=0;D=1;C=None;z=len;r=range
 if not g or not g[0]:return[A[:]for A in g]
 E,F=z(g),z(g[0])
 def A3(G,u,d,w):
  K=w;Q=CU(B for A in G for B in A).most_common(1)[0][0]if K else C;A=[[m]*F for A in r(E)];R=[];S=[(1,0),(-1,0),(0,1),(0,-1)]
  if d:S+=[(1,1),(1,-1),(-1,1),(-1,-1)]
  for B in r(E):
   for H in r(F):
    T=G[B][H]
    if K and T==Q or A[B][H]:continue
    L=[];M=[(B,H)];A[B][H]=D;V=T
    while M:
     N,O=M.pop();P=G[N][O]
     if u and P!=V or K and P==Q:continue
     L.append((P,(N,O)))
     for(W,X)in S:
      I,J=N+W,O+X
      if 0<=I<E and 0<=J<F and not A[I][J]:A[I][J]=D;M.append((I,J))
    if L:R.append(L)
  return R
 def G(x):A=x;return[A for(B,A)in A]if A and isinstance(A[0],tuple)and isinstance(A[0][1],tuple)else list(A)
 def R(x):return min(A for(B,A)in G(x))
 def A4(x):return max(A for(B,A)in G(x))
 def S(x):return min(A for(A,B)in G(x))
 def T(x):return max(A for(A,B)in G(x))
 def K(x):A=x;return A4(A)-R(A)+1
 def L(x):A=x;return T(A)-S(A)+1
 def n(x):A=x;return S(A),R(A)
 def o(x,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in x]
 def A5(x):A=x;return o(A,(-S(A),-R(A)))
 def A6(cont):
  C,D=set(),[]
  for E in cont:
   for(F,(A,B))in E:
    if(A,B)not in C:C.add((A,B));D.append((F,(A,B)))
  return D
 def A7(x,f):
  A=x
  if f<=1:return A
  B=[]
  for(C,(D,E))in A:
   for F in r(f):
    for G in r(f):B.append((C,(D*f+F,E*f+G)))
  return B
 def A8(G,obj):
  A=[A[:]for A in G]
  for(D,(B,C))in obj:
   if 0<=B<z(A)and 0<=C<z(A[0]):A[B][C]=D
  return A
 def A9(x,G):A=x;B,C=n(A);D,E=L(A),K(A);return[G[A][C:C+E]for A in r(B,B+D)]
 def p(x):
  D={}
  for(E,(B,C))in x:
   if E in(0,4):continue
   A=D.setdefault(E,[B,B,C,C])
   if B<A[0]:A[0]=B
   if B>A[1]:A[1]=B
   if C<A[2]:A[2]=C
   if C>A[3]:A[3]=C
  return D
 def q(a,b):return(a+b-1)//b if b>0 else 0
 def AA(l,b,i):
  F=b;E=l;G=p(E);Y=CU(A for(A,B)in E if A not in(0,4));H=[A for A in G if A in F]
  if not H:return
  I,J=[],[];A=[];K=[]
  for B in H:
   L,Z,M,a=G[B];N,b,O,c=F[B];P=a-M+1;Q=Z-L+1;R=c-O+1;S=b-N+1
   if P<=0 or Q<=0 or R<=0 or S<=0:return
   d=max(1,q(R,P));e=max(1,q(S,Q));I.append(d);J.append(e);A.append((L,M,N,O));T=Y.get(B,0);f=i.get(B,0)
   if T>0:
    C=1
    while T*C*C<f:C+=1
    K.append(C)
  U=I+J+K;D=max(U)if U else 0
  if D<=0:return
  V=[C-A*D for(A,B,C,B)in A];W=[C-B*D for(A,B,A,C)in A];g=min(V)if V else 0;h=min(W)if W else 0;return D,(g,h),A
 U=[A[:]for A in g]
 for a in r(E):
  for s in r(F):
   if U[a][s]==4:U[a][s]=0
 M=A3(U,m,D,D);AB=[(0,(A,B))for A in r(E)for B in r(F)if g[A][B]==4];B=A9(AB,g);AC=max(map(T,M))if M else 0;AD=[A for A in M if T(A)==AC]or M;H=[[0 if A==4 else A for A in A]for A in B];V,W=(z(H),z(H[0]))if H and H[0]else(0,0)
 def AE(Gc):
  A=Gc
  if not A or not A[0]:return[]
  J=CU(B for A in A for B in A).most_common(1)[0][0];I=[[m]*W for A in r(V)];M=[]
  for E in r(V):
   for F in r(W):
    if I[E][F]or A[E][F]==J:continue
    N=A[E][F];K,L=deque([(E,F)]),[];I[E][F]=D
    while K:
     G,H=K.popleft()
     if A[G][H]!=N or A[G][H]==J:continue
     L.append((A[G][H],(G,H)))
     for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
      B,C=G+P,H+Q
      if 0<=B<V and 0<=C<W and not I[B][C]:
       if A[B][C]==N and A[B][C]!=J:I[B][C]=D;K.append((B,C))
    if L:M.append(L)
  return M
 A=A6(AE(H));AY=set(G(A));AF,AG=(K(A),L(A))if A else(0,0);AH,AI=n(A)if A else(0,0);AJ=p(A);AL=CU(A for(A,B)in A);X={(B,C):A for(A,(B,C))in A}
 def Y(o,m):
  B=m;A=o
  if B<0:return 0
  if A<0:return 0
  if A>B:return B
  return A
 def AM(r,s):
  B=s;A=r
  if not A:return 0,0
  C=[D-A*B for(A,C,D,C)in A];D=[D-C*B for(A,C,A,D)in A];return min(C)if C else 0,min(D)if D else 0
 Z,t=C,C
 for N in AD or[]:
  if not N:continue
  u=A5(N);v=AA(u,AJ,AL);O=[]
  if v:a,b,I=v;O.append((a,b,I));O.append((a+1,AM(I,a+1),I))
  else:c,d=K(N),L(N);AN=(AF+c-1)//c if c else 1;AO=(AG+d-1)//d if d else 1;P=max(1,AN,AO);O.append((P,(AH,AI),C))
  for(P,(AP,AQ),I)in O:
   if P<=0:continue
   e=A7(u,P);w,AR=L(e),K(e);f=z(B)-w;h=z(B[0])-AR
   if f>=0:
    i=1;x=z(B)-w-1
    if x>=i:j=r(i,x+1)
    else:j=[Y(i,f)]
   else:j=[0]
   AS=r(h+1)if h>=0 else[0];b=Y(AP,f),Y(AQ,h);Q={b}
   if I is C:Q.update((A,B)for A in j for B in AS)
   if not Q:Q.add((0,0))
   for(AT,AU)in Q:
    y=o(e,(AT,AU));J={(A,C):D for(D,(A,C))in y if 0<=A<z(B)and 0<=C<z(B[0])}
    if not J:continue
    if any(B[A][C]==4 for(A,C)in J):continue
    if X:
     cc=A0=A1=0
     for((AV,AW),AX)in X.items():
      A2=J.get((AV,AW))
      if A2 is C:A1+=1
      elif A2==AX:cc+=1
      else:A0+=1
     k=z([1 for A in J if A not in X]);l=cc*200-A0*500-A1*1000-k
    else:k=z(J);l=-k
    if Z is C or l>Z:Z,t=l,y
 return A8(B,t or[])