def p(g):
 C=tuple(tuple(A)for A in g);I,J=len(C),len(C[0]);P=[[False]*J for A in range(I)];T=[]
 def p(i,j):
  for(C,D)in((1,0),(-1,0),(0,1),(0,-1)):
   A,B=i+C,j+D
   if 0<=A<I and 0<=B<J:yield(A,B)
 for G in range(I):
  for H in range(J):
   if not P[G][H]:
    f=C[G][H];U=[(G,H)];P[G][H]=True;h=set()
    while U:
     i,j=U.pop();h.add((i,j))
     for(Q,R)in p(i,j):
      if not P[Q][R]and C[Q][R]==f:P[Q][R]=True;U.append((Q,R))
    T.append((f,h))
 k=[(B,A)for(B,A)in T if len(A)==1];l=[(B,A)for(B,A)in T if len(A)>1]
 if not l:return[list(A)for A in C]
 V={}
 for(L,W)in l:V[L]=V.get(L,0)+len(W)
 M=sorted(V.items(),key=lambda kv:(-kv[1],kv[0]))
 if not M:return[list(A)for A in C]
 X=M[0][0];Y=M[1][0]if len(M)>1 else M[0][0];q={(A,B)for A in range(I)for B in range(J)if C[A][B]==X};r={(A,B)for A in range(I)for B in range(J)if C[A][B]==Y};s=[(1,1),(-1,-1),(1,-1),(-1,1)]
 def t(i,j,di,dj):
  C=[];A,B=i,j
  while 0<=A<I and 0<=B<J:C.append((A,B));A+=di;B+=dj
  return C
 K=[(A,B)for(A,B)in k if A not in(X,Y)]
 if not K:K=k[:]
 Z=set()
 for(u,W)in K:
  v,w=next(iter(W))
  for(x,y)in s:Z.update(t(v,w,x,y))
 z=Z&q;A0=Z&r
 if K:
  S={}
  for(L,u)in K:S[L]=S.get(L,0)+1
  F=sorted(S.keys(),key=lambda c:(-S[c],c))
  if len(F)==1:F=F+[F[0]]
  elif len(F)>2:F=F[:2]
  A,B=F[0],F[1]
  def m(mc):
   A=B=0
   for(L,M)in K:
    if L!=mc:continue
    N,O=next(iter(M))
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
  else:
   a,b=overlaps_for(A);c,d=overlaps_for(B)
   if a>b and c<d:D,E=A,B
   elif a<b and c>d:D,E=B,A
   else:
    n=a+d;o=c+b
    if n>o:D,E=A,B
    elif o>n:D,E=B,A
    else:D,E=(A,B)if A<=B else(B,A)
 else:return[list(A)for A in C]
 e=[list(A)for A in C]
 for(G,H)in z:e[G][H]=D
 for(G,H)in A0:e[G][H]=E
 return e