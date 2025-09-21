R=range
S=sorted
T=tuple
X=list
Y=len
def se(I):
 if not I or not I[0]:return I
 D,E=Y(I),Y(I[0]);x=[B for A in I for B in A];y=min(set(x),key=x.count);C={(A,B)for A in R(D)for B in R(E)if I[A][B]==0}
 if not C:return I
 r={(A,B)for A in R(D)for B in R(E)if I[A][B]==y}
 def Z(x):A=[A for(A,B)in x];B=[A for(B,A)in x];return min(A),min(B),max(A),max(B)
 def a(x):A,B,C,D=Z(x);return(A+C)//2,(B+D)//2
 def g(x,y):
  A,B=x;C,D=y;E=[]
  if A==C:
   F,G=S((B,D))
   for H in R(F,G+1):E+=[(A,H)]
  elif B==D:
   I,J=S((A,C))
   for K in R(I,J+1):E+=[(K,B)]
  elif C-A==D-B:
   I,J=S((A,C));F,G=S((B,D))
   for(K,H)in zip(R(I,J+1),R(F,G+1)):E+=[(K,H)]
  elif C-A==-(D-B):
   I,J=S((A,C));F,G=S((B,D))
   for(K,H)in zip(R(I,J+1),R(G,F-1,-1)):E+=[(K,H)]
  return E
 s,t,u,V=Z(C);h=set(g((s,t),(u,V))).issubset(C)
 i,j=a(C);k,l=a(r);b,W=(k-i>0)-(k-i<0),(l-j>0)-(l-j<0);N,O=u-s+1,V-t+1;G=N*b,O*W;c=Y(C)==2*(N+O)-4
 if c:J=G
 else:J=G if h else(G[0]-((G[0]>0)-(G[0]<0)),G[1]-((G[1]>0)-(G[1]<0)))
 F=set()
 U = F.update
 if c:
  for H in R(1,5):
   A,B=H*J[0],H*J[1];d,m,e,n=s+A,t+B,u+A,V+B;K=0<=d and e<D;L=0<=m and n<E
   if K and L:U({(C+A,D+B)for(C,D)in C});continue
   if H==1:U({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E});break
   if not K and L:U({(C+A,E+B)for(C,E)in C if 0<=C+A<D})
   elif not K and not L:U({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E})
   elif K and not L and(W<0 or N==3 and O==3):U({(D+A,C+B)for(D,C)in C if 0<=C+B<E})
   elif K and not L and(e>=D-1 or d<=0):U({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E})
   break
 else:
  for H in R(1,5):A,B=H*J[0],H*J[1];U({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E})
 if Y(C)==8 and N==3 and O==3 and Y(r)==1:o,z=next(iter(r));P,Q=o+b,z+W;q={(P-1,Q+A)for A in(-1,0,1)}|{(P,Q-1),(P,Q+1)}|{(P+1,Q+A)for A in(-1,0,1)};F|={(A,B)for(A,B)in q if 0<=A<D and 0<=B<E}
 f=[X(A)for A in I]
 for(r,s)in F:f[r][s]=y
 return T(map(T,f))
def p(g):return[X(A)for A in se(T(map(T,g)))]