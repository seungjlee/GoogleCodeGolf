R=range
T=tuple
z=len
m=min
x=max
def mc(g):
 A={}
 for C in g:
  for B in C:A[B]=A.get(B,0)+1
 return max(A,key=A.get)
def _o(g):
 A=g;I,J=z(A),z(A[0]);L=mc(A);F=[[0]*J for A in R(I)];M=[]
 for G in R(I):
  for H in R(J):
   if F[G][H]or A[G][H]==L:continue
   K=[(G,H)];F[G][H]=1;N=[]
   while K:
    B,C=K.pop();O=A[B][C];N+=[(O,(B,C))]
    for(D,E)in((B-1,C),(B+1,C),(B,C-1),(B,C+1)):
     if 0<=D<I and 0<=E<J and not F[D][E]and A[D][E]!=L:F[D][E]=1;K+=[(D,E)]
   M+=[N]
 return M
def ti(A):
 if not A:return[]
 B=next(iter(A))
 if isinstance(B,T)and z(B)==2 and isinstance(B[1],T):return[A for(B,A)in A]
 return list(A)
def bb(a):A=ti(a);B=[A for(A,B)in A];C=[A for(B,A)in A];return m(B),x(B),m(C),x(C)
def h(a):
 if not a:return 0
 B,C,_,_=bb(a);return C-B+1
def w(a):
 if not a:return 0
 _,_,C,D=bb(a);return D-C+1
def u(a):return bb(a)[0]
def l(a):return bb(a)[1]
def q(a):return bb(a)[2]
def r(a):return bb(a)[3]
def _v(a):
 a=ti(a)
 if not a:return 0
 return w(a)==1 and h(a)==z(a)
def _c(a,b):
 A,B=a;C,D=b;E,F=m(A,C),x(A,C)+1;G,H=m(B,D),x(B,D)+1
 if A==C:return{(A,B)for B in R(G,H)}
 if B==D:return{(A,B)for A in R(E,F)}
 if C-A==D-B:return{(A,B)for(A,B)in zip(R(E,F),R(G,H))}
 if C-A==B-D:return{(A,B)for(A,B)in zip(R(E,F),R(H-1,G-1,-1))}
 return{*()} 
def _s(A,d):B=d;return _c(A,(A[0]+42*B[0],A[1]+42*B[1]))
def _f(A,v,i):
 E,F=z(A),z(A[0]);B=[list(A)for A in A]
 for(C,D)in ti(i):
  if 0<=C<E and 0<=D<F:B[C][D]=v
 return B
def _uf(A,v,i):
 E,F=z(A),z(A[0]);G=mc(A);B=[list(A)for A in A]
 for(C,D)in ti(i):
  if 0<=C<E and 0<=D<F and B[C][D]==G:B[C][D]=v
 return B
def p(I):
 F=_o(I);D=[]
 for B in F:
  A={B for(A,B)in B if A==2}
  if not A:continue
  J=l(A)==l(B);K=r(A)==r(B);L=u(A)==u(B);M=q(A)==q(B);N=(1 if J else 0)+(-1 if L else 0);O=(1 if K else 0)+(-1 if M else 0);P=u(A)+h(A)//2;Q=q(A)+w(A)//2;C=_s((P,Q),(N,O));D+=[C]
 S=_f(I,2,{B for A in D for B in A});E={*()} 
 for(B,C)in zip(F,D):
  t=_v(C);G=m(h(B),w(B))
  U=E.update
  for H in R(-(G-1),G):
   if t:U({(A,B+H)for(A,B)in C})
   else:U({(A+H,B)for(A,B)in C})
 return _uf(S,3,E)