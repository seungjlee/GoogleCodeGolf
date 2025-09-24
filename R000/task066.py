_A=None;m=min;e=enumerate;z=len;w=abs;q=set
from copy import deepcopy as dc
def ib(g,r,c):return 0<=r<z(g)and 0<=c<z(g[0])
def n4(r,c):return[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def norm1(d):return 0 if d[0]==0 else 1 if d[0]>0 else-1,0 if d[1]==0 else 1 if d[1]>0 else-1
def rl(d):return-d[1],d[0]
def rr(d):return d[1],-d[0]
def man(a,b):return w(a[0]-b[0])+w(a[1]-b[1])
def fpos(g,val):return[(A,C)for(A,B)in e(g)for(C,D)in e(B)if D==val]
def c4(g,positions):
 A=q(positions);E=[]
 while A:
  F=A.pop();D=[F];G=[F]
  while D:
   H,I=D.pop()
   for(B,C)in n4(H,I):
    if(B,C)in A:A.remove((B,C));D+=[(B,C)];G+=[(B,C)]
  E+=[G]
 return E
def cgd(goals,p):A=goals;return m(man(p,A)for A in A)if A else 10**9
def ifp(val):return val==0 or val==3
def csad(g,greens,reds):
 F=greens
 if not F or not reds:return
 M=c4(g,F);E=m(M,key=lambda comp:(z(comp),cgd(reds,(round(sum(A for(A,B)in comp)/z(comp)),round(sum(A for(B,A)in comp)/z(comp))))));B=_A;N=q(E)
 for(G,H)in E:
  for(I,J)in n4(G,H):
   if(I,J)in N:B=(G,H),(I,J);break
  if B:break
 if B is _A:
  K=_A;L=-1
  for C in E:
   for D in E:
    A=man(C,D)
    if A>L:K=C,D;L=A
  B=K
 C,D=B;A=norm1(sub(D,C));O=[(D,A),(C,(-A[0],-A[1]))];return m(O)
class R:
 __slots__='pred','path','steps','dmin','dend','bounces','start','start_dir'
 def __init__(A,pred,path,steps,dmin,dend,bounces,start,start_dir):A.pred=pred;A.path=path;A.steps=steps;A.dmin=dmin;A.dend=dend;A.bounces=bounces;A.start=start;A.start_dir=start_dir
def rws(g,start,d,reds):
 M=start;J=reds;T,U=z(g),z(g[0]);C=dc(g);G=q();K=0;A=M;D=d;N=[A];H=cgd(J,A);O=H;L=0
 while K<T*U*10:
  K+=1;F=add(A,D)
  if ib(g,*F)and C[F[0]][F[1]]==2:break
  V=not ib(g,*F)or not ifp(C[F[0]][F[1]])
  if not V:
   A=F
   if C[A[0]][A[1]]==0:C[A[0]][A[1]]=3
   E=A,D
   if E in G:break
   G.add(E)
  else:
   P,W=rl(D),rr(D);I=[]
   for Q in(P,W):
    B=add(A,Q)
    if ib(g,*B)and ifp(C[B[0]][B[1]]):I+=[(cgd(J,B),Q,B)]
   if I:
    I.sort(key=lambda x:(x[0],0 if x[1]==P else 1));Y,X,B=I[0];D=X;A=B
    if C[A[0]][A[1]]==0:C[A[0]][A[1]]=3
    E=A,D
    if E in G:break
    G.add(E);L+=1
   else:
    Q=-D[0],-D[1];B=add(A,Q)
    if ib(g,*B)and ifp(C[B[0]][B[1]]):
     D=Q;A=B
     if C[A[0]][A[1]]==0:C[A[0]][A[1]]=3
     E=A,D
     if E in G:break
     G.add(E);L+=1
    else:break
  N+=[A];S=cgd(J,A);H=m(H,S);O=S
 return R(C,N,K,H,O,L,M,d)
def dss(g):
 D=fpos(g,2);G=fpos(g,3)
 if not D or not G:return dc(g)
 P=c4(g,G);E=m(P,key=lambda comp:(z(comp),cgd(D,(round(sum(A for(A,B)in comp)/z(comp)),round(sum(A for(B,A)in comp)/z(comp))))));A=_A;Q=q(E)
 for(H,I)in E:
  for(J,K)in n4(H,I):
   if(J,K)in Q:A=(H,I),(J,K);break
  if A:break
 if A is _A:
  L=_A;M=-1
  for B in E:
   for C in E:
    N=man(B,C)
    if N>M:L=B,C;M=N
  A=L
 B,C=A;F=norm1(sub(C,B));O=[rws(g,C,F,D),rws(g,B,(-F[0],-F[1]),D)];O.sort(key=lambda r:(r.dend,r.bounces,r.dmin,r.steps));return O[0].pred
def dastbr(g):
 D=fpos(g,2);E=fpos(g,3)
 if z(D)!=2 or z(E)!=2:return
 def H(ps):(A,B),(C,D)=sorted(ps);return B==D and w(A-C)==1
 if not(H(D)and H(E)):return
 (I,F),(J,P)=sorted(E);(K,G),(L,P)=sorted(D)
 if{I,J}!={K,L}:return
 M,N=sorted([F,G]);C=_A
 for A in range(0,m(I,K)+1):
  if all(g[A][B]in(0,3,2)for B in range(M,N+1)):C=A;break
 if C is _A or C==0:return
 B=dc(g);Q=max(J,L)
 for A in range(C,Q+1):
  if B[A][F]==0:B[A][F]=3
  if B[A][G]==0:B[A][G]=3
 for O in range(M,N+1):
  if B[C][O]==0:B[C][O]=3
 return B
def p(grid):
 A=dastbr(grid)
 if A is not _A:return A
 return dss(grid)