m=min;r=range;l=len
def p(g):
 M=[A[:]for A in g];a,b=l(M),l(M[0]);A=[]
 for W in M:
  b=[]
  for X in W:b+=[X]*2
  A.extend([b[:],b[:]])
 J,K=l(A),l(A[0]);L=[[0]*K for A in r(J)];D=[]
 for B in r(J):
  for a in r(K):
   if A[B][a]!=2 or L[B][a]:continue
   O=[(B,a)];L[B][a]=1;P=[]
   while O:
    E,Q=O.pop();P+=[(E,Q)]
    for R in(-1,0,1):
     for S in(-1,0,1):
      if R==S==0:continue
      F,G=E+R,Q+S
      if 0<=F<J and 0<=G<K and not L[F][G]and A[F][G]==2:L[F][G]=1;O+=[(F,G)]
   D+=[P]
 Y={(B,a)for B in r(J)for a in r(K)if A[B][a]==2}
 def T(si,q,u,ej):
  for B in r(si,u+1):
   for a in r(q,ej+1):A[B][a]=4
 for E in D:H=[A for(A,B)in E];I=[A for(B,A)in E];T(m(H),m(I),max(H),max(I))
 def Z(A,B):
  a=10**9
  for(E,F)in A:
   for(G,H)in B:
    D=abs(E-G)+abs(F-H)
    if D<a:a=D
    if a==0:return 0
  return a
 d=l(D)
 for B in r(d):
  for a in r(d):
   if Z(D[B],D[a])<5:k=D[B]+D[a];H=[A for(A,B)in k];I=[A for(B,A)in k];T(m(H),m(I),max(H),max(I))
 for(B,a)in Y:A[B][a]=2
 return[A[::2]for A in A[::2]]