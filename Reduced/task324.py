R=range
T=tuple
V=list
W=len
def Nx(x):return next(iter(x))
def p(g):
 C=T(T(A)for A in g);I,J=W(C),W(C[0]);P=[[False]*J for A in R(I)];t=[]
 def n(i,j):
  for(C,D)in((1,0),(-1,0),(0,1),(0,-1)):
   A,B=i+C,j+D
   if 0<=A<I and 0<=B<J:yield(A,B)
 for G in R(I):
  for H in R(J):
   if not P[G][H]:
    f=C[G][H];U=[(G,H)];P[G][H]=True;h=set()
    while U:
     i,j=U.pop();h.add((i,j))
     for(q,r)in n(i,j):
      if not P[q][r]and C[q][r]==f:P[q][r]=True;U+=[(q,r)]
    t+=[(f,h)]
 k=[(B,A)for(B,A)in t if W(A)==1];l=[(B,A)for(B,A)in t if W(A)>1]
 if not l:return[V(A)for A in C]
 v={}
 for(L,w)in l:v[L]=v.get(L,0)+W(w)
 M=sorted(v.items(),key=lambda k:(-k[1],k[0]))
 if not M:return[V(A)for A in C]
 X=M[0][0];Y=M[1][0]if W(M)>1 else M[0][0];q={(A,B)for A in R(I)for B in R(J)if C[A][B]==X}
 r={(A,B)for A in R(I)for B in R(J)if C[A][B]==Y};s=[(1,1),(-1,-1),(1,-1),(-1,1)]
 def Q(i,j,di,dj):
  C=[];A,B=i,j
  while 0<=A<I and 0<=B<J:C+=[(A,B)];A+=di;B+=dj
  return C
 K=[(A,B)for(A,B)in k if A not in(X,Y)]
 if not K:K=k[:]
 Z=set()
 for(_,w)in K:
  v,w=Nx(w)
  for(x,y)in s:Z.update(Q(v,w,x,y))
 z=Z&q;A0=Z&r
 if K:
  S={}
  for(L,u)in K:S[L]=S.get(L,0)+1
  F=sorted(S.keys(),key=lambda c:(-S[c],c))
  if W(F)==1:F=F+[F[0]]
  elif W(F)>2:F=F[:2]
  A,B=F[0],F[1]
  def m(x):
   A=B=0
   for(L,M)in K:
    if L!=x:continue
    N,O=Nx(M)
    for D in(-1,0,1):
     for E in(-1,0,1):
      if D==0 and E==0:continue
      F,G=N+D,O+E
      if 0<=F<I and 0<=G<J:
       H=C[F][G]
       if H==X:A+=1
       elif H==Y:B+=1
   return A-B
  N=m(A);O=m(B)
  if N>0 and O<0:D,E=A,B
  elif N<0 and O>0:D,E=B,A
  elif N==0 and O!=0:
   if O>0:D,E=B,A
   else:D,E=A,B
  elif O==0 and N!=0:
   if N>0:D,E=A,B
   else:D,E=B,A
 else:return[V(A)for A in C]
 e=[V(A)for A in C]
 for(G,H)in z:e[G][H]=D
 for(G,H)in A0:e[G][H]=E
 return e