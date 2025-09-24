L=len
R=range
T=tuple
V=reversed
X=max
Y=min
Z=list
def p(g):
 O=None
 if not g or not g[0]:return[Z(A)for A in g]
 E=T(T(A)for A in g);f,h=L(E),L(E[0])
 def J(a):A=[A for(A,B)in a];B=[A for(B,A)in a];return Y(A),Y(B),X(A),X(B)
 def P(a):
  A=a
  if not A:return set()
  B,C,_,_=J(A);return{(A-B,D-C)for(A,D)in A}
 K=T(T(V(A))for A in E);from collections import Counter as i;F=i(B for A in K for B in A);Q=X(F.items(),key=lambda k:k[1])[0];A={}
 for r in R(f):
  B=K[r]
  for S in R(h):
   t=B[S]
   if t!=Q:A.setdefault(t,set()).add((r,S))
 if not A:return[Z(A)for A in E]
 C=X(A,key=lambda c:L(A[c]));G=P(A[C]);D=O
 for(F,H)in A.items():
  if F==C:continue
  if L(H)==L(A[C]):continue
  j=P(H);I={(2*A+C,2*B+D)for(A,B)in j for C in(0,1)for D in(0,1)}
  if I and G:
   U=[A for(A,B)in I];v=[A for(B,A)in I];W=[A for(A,B)in G];x=[A for(B,A)in G];k=Y(W)-X(U);l=X(W)-Y(U);m=Y(x)-X(v);n=X(x)-Y(v);o=I;p=G;l=0
   for q in R(k,l+1):
    for r in R(m,n+1):
     y=sum(1 for(A,B)in o if(A+q,B+r)in p)
     if y>l:l=y
   z=l
  else:z=0
  s=J(H)[3];b=L(H);t=z-2*b;c=t,b,s,F
  if D is O or c>D:D=c
 if D is O:d=[A for A in A if A!=C];M=X(d,key=lambda c:L(A[c]))if d else C
 else:M=D[3]
 u,v,w,x=J(A[M]);N=[Z(K[A][v:x+1])for A in R(u,w+1)]
 for y in R(L(N)):
  B=N[y]
  for e in R(L(B)):
   if B[e]!=M:B[e]=Q
 z=T(T(V(A))for A in N);return[Z(A)for A in z]