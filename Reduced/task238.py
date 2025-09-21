R=range
En=enumerate
Tu=tuple
def m(g):
 B=g
 if not B or not B[0]:return 0
 A={}
 for D in B:
  for C in D:A[C]=A.get(C,0)+1
 return max(A,key=A.get)
def Oj(g,u,d,w):
 L=u;A=g
 if not A or not A[0]:return[]
 M,N=len(A),len(A[0]);O=m(A)if w else None;P=[(-1,0),(1,0),(0,-1),(0,1)]
 if d:P+=[(-1,-1),(-1,1),(1,-1),(1,1)]
 D,Q=set(),[]
 for E in R(M):
  for F in R(N):
   if(E,F)in D:continue
   r=A[E][F]
   if r==O:continue
   G,H=set(),[(E,F)]
   while H:
    B,C=H.pop()
    if(B,C)in D:continue
    I=A[B][C]
    if L and I!=r or not L and I==O:continue
    D.add((B,C));G.add((I,(B,C)))
    for(s,q)in P:
     J,K=B+s,C+q
     if 0<=J<M and 0<=K<N and(J,K)not in D:H.append((J,K))
   if G:Q.append(G)
 return Q
def T(obj):
 A=obj
 if not A:return set()
 B=next(iter(A))
 if isinstance(B,Tu)and len(B)==2 and isinstance(B[1],Tu):return{(A,B)for(C,(A,B))in A}
 return set(A)
def bb(patch):A=T(patch);B=min(A for(A,B)in A);C=min(A for(B,A)in A);D=max(A for(A,B)in A);E=max(A for(B,A)in A);return(B,C),(D,E)
def n(obj):
 A=obj
 if not A:return A
 (B,C),D=bb(A);return{(A,(D-B,E-C))for(A,(D,E))in A}
def S(patch,d):
 A=patch;C,D=d
 if not A:return A
 B=next(iter(A))
 if isinstance(B,Tu)and len(B)==2 and isinstance(B[1],Tu):return{(A,(B+C,E+D))for(A,(B,E))in A}
 return{(A+C,B+D)for(A,B)in A}
def c(grid,start,dims):A,B=start;C,D=dims;return[A[B:B+D]for A in grid[A:A+C]]
def uu(patch,grid):(A,B),(C,D)=bb(patch);return c(grid,(A,B),(C-A+1,D-B+1))
def v(idx):
 A=T(idx)
 if not A:return set()
 (B,C),(B,D)=bb(A);E=C+D;return{(A,E-B)for(A,B)in A}
def k(x,y):
 A,B=x;C,D=y;E,F=min(A,C),min(B,D);G,H=max(A,C),max(B,D)
 if A==C:return{(A,B)for B in R(F,H+1)}
 if B==D:return{(A,B)for A in R(E,G+1)}
 if C-A==D-B:return{(A,B)for(A,B)in zip(R(E,G+1),R(F,H+1))}
 if C-A==B-D:return{(A,B)for(A,B)in zip(R(E,G+1),R(H,F-1,-1))}
 return set()
def z(g,o):
 A=g;B=len(A);F=len(A[0])if B and A[0]else 0;C=[list(A)for A in A]
 for(G,(D,E))in o:
  if 0<=D<B and 0<=E<F:C[D][E]=G
 return C
def f(g,value,idx):
 A=g;B=len(A);F=len(A[0])if B and A[0]else 0;C=[list(A)for A in A]
 for(D,E)in T(idx):
  if 0<=D<B and 0<=E<F:C[D][E]=value
 return C
def nc(o):return len({A for(A,B)in o})
def p(I):
 A=Oj(I,0,1,1)
 if not A:return I
 G={(8,(A,C))for(A,B)in En(I)for(C,D)in En(B)if D==8};H=lambda o:len(T(o));J=G or min(A,key=nc);K=[A for A in A if{A for(A,B)in A}!={8}]or A;B=max(K,key=H,default=None)
 if not B:return I
 D={(A,B)for(A,B)in B if A!=8};L=uu(D or B,I);C=T(S(n(J),(1,1)));E=list(n(D or B));M=z(L,[(min(E,key=lambda t,i=A,j=B:abs(t[1][0]-i)+abs(t[1][1]-j))[0]if E else 0,(A,B))for(A,B)in C]);(N,O),(P,Q)=bb(C);F=k((N,O),(P,Q));r=C&(F|v(F));return f(M,8,r)