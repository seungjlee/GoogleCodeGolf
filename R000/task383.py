z=len;n=min;x=max;r=range;t=set
def p(I):
 from collections import Counter as M;a,b=z(I),z(I[0]);c=M(B for A in I for B in A);R=x(c,key=c.get);K=[(A,B)for A in r(a)for B in r(b)if I[A][B]!=R]
 if not K:return I
 B=n(A for(A,B)in K);G=x(A for(A,B)in K);C=n(A for(B,A)in K);H=x(A for(B,A)in K);L=M(I[A][B]for A in r(B,G+1)for B in r(C,H+1));S={A for A in L if A!=R};D=t()
 for E in r(B,G+1):D.add(I[E][C]);D.add(I[E][H])
 for F in r(C,H+1):D.add(I[B][F]);D.add(I[G][F])
 D.discard(R);d=S-D
 if d:A=x(d,key=lambda c:(L[c],-c))
 else:A=n(S,key=lambda c:(L[c],c))
 if D:e=x(D,key=lambda c:(L[c],-c))
 else:f=[B for B in S if B!=A];e=x(f,key=lambda c:(L[c],-c))if f else A
 N=[sum(1 for C in r(C,H+1)if I[B][C]==A)for B in r(B,G+1)];O=[sum(1 for B in r(B,G+1)if I[B][C]==A)for C in r(C,H+1)];T=[A for A in N if A];g=[A for A in O if A];h=[];i=[]
 if T:
  P=M(A for A in N if A);U=x(P.items(),key=lambda kv:(kv[1],-kv[0]))[0];V=n(T);m=x(T)
  if V>2 and m-V==1:U=V
  h=[A for(A,B)in enumerate(N)if B==U];i=[A for(A,B)in enumerate(N)if B>U]
 j=[];k=[]
 if g:
  P=M(A for A in O if A);W=x(P.items(),key=lambda kv:(kv[1],-kv[0]))[0];X=n(g)
  if X>2 and P[X]>1:W=X
  j=[A for(A,B)in enumerate(O)if B==W];k=[A for(A,B)in enumerate(O)if B>W]
 J=[list(A)for A in I]
 for E in r(B,G+1):
  for F in r(C,H+1):J[E][F]=e
 for Y in h:
  Q=B+Y
  for Z in j:J[Q][C+Z]=A
 for Y in i:
  Q=B+Y
  for F in r(0,C):J[Q][F]=A
  for F in r(H+1,b):J[Q][F]=A
 for Z in k:
  l=C+Z
  for E in r(0,B):J[E][l]=A
  for E in r(G+1,a):J[E][l]=A
 return J