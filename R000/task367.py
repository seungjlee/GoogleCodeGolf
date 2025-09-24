Q=len
R=range
T=tuple
U=list
def S(I):
 C,D=Q(I),Q(I[0])
 def L(g,J):
  G=[[0]*D for a in R(C)];K=[]
  for E in R(C):
   for F in R(D):
    if G[E][F]:continue
    G[E][F]=1
    if g[E][F]!=J:continue
    H=[(E,F)];I=0;L=[(E,F)]
    while I<Q(H):
     M,N=H[I];I+=1
     for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
      a,B=M+O,N+P
      if 0<=a<C and 0<=B<D and not G[a][B]:
       G[a][B]=1
       if g[a][B]==J:H+=[(a,B)];L+=[(a,B)]
    K+=[L]
  return K
 def A(a):B=[a for(a,_)in a];C=[a for(_,a)in a];return min(B),min(C),max(B),max(C)
 def M(b):C,D,E,F=A(b);G=(E-C+1)*(F-D+1);return Q(b)==G
 def N(c):F,G,H,I=A(c);B,C=F-1,G-1;D,E=H+1,I+1;J={(a,C)for a in R(B,D+1)}|{(a,E)for a in R(B,D+1)};K={(B,a)for a in R(C,E+1)}|{(D,a)for a in R(C,E+1)};return J|K
 def O(r):B,C,D,E=A(U(r));return{(B,C),(B,E),(D,C),(D,E)}
 P={(a,B)for a in R(C)for B in R(D)if I[a][B]==5};F=set()
 for B in L(I,0):
  if not M(B):continue
  G=N(B);E=set()
  for(q,r)in O(G):
   for(s,t)in((1,0),(-1,0),(0,1),(0,-1)):u,v=q+s,r+t;E.add((u,v))
  E-=G
  if P.isdisjoint(E):F.update(B)
 H=[U(a)for a in I]
 for(J,K)in F:
  if 0<=J<C and 0<=K<D:H[J][K]=4
 return T(T(a)for a in H)
def p(g):return[U(x)for x in S(T(T(a)for a in g))]