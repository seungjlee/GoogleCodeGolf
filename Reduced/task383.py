def p(I):
 from collections import Counter as M;a,b=len(I),len(I[0]);c=M(B for A in I for B in A);R=max(c,key=c.get);K=[(A,B)for A in range(a)for B in range(b)if I[A][B]!=R]
 if not K:return I
 B=min(A for(A,B)in K);G=max(A for(A,B)in K);C=min(A for(B,A)in K);H=max(A for(B,A)in K);L=M(I[A][B]for A in range(B,G+1)for B in range(C,H+1));S={A for A in L if A!=R};D=set()
 for E in range(B,G+1):D.add(I[E][C]);D.add(I[E][H])
 for F in range(C,H+1):D.add(I[B][F]);D.add(I[G][F])
 D.discard(R);d=S-D
 if d:A=max(d,key=lambda c:(L[c],-c))
 else:A=min(S,key=lambda c:(L[c],c))
 if D:e=max(D,key=lambda c:(L[c],-c))
 else:f=[B for B in S if B!=A];e=max(f,key=lambda c:(L[c],-c))if f else A
 N=[sum(1 for C in range(C,H+1)if I[B][C]==A)for B in range(B,G+1)];O=[sum(1 for B in range(B,G+1)if I[B][C]==A)for C in range(C,H+1)];T=[A for A in N if A];g=[A for A in O if A];h=[];i=[]
 if T:
  P=M(A for A in N if A);U=max(P.items(),key=lambda kv:(kv[1],-kv[0]))[0];V=min(T);m=max(T)
  if V>2 and m-V==1:U=V
  h=[A for(A,B)in enumerate(N)if B==U];i=[A for(A,B)in enumerate(N)if B>U]
 j=[];k=[]
 if g:
  P=M(A for A in O if A);W=max(P.items(),key=lambda kv:(kv[1],-kv[0]))[0];X=min(g)
  if X>2 and P[X]>1:W=X
  j=[A for(A,B)in enumerate(O)if B==W];k=[A for(A,B)in enumerate(O)if B>W]
 J=[list(A)for A in I]
 for E in range(B,G+1):
  for F in range(C,H+1):J[E][F]=e
 for Y in h:
  Q=B+Y
  for Z in j:J[Q][C+Z]=A
 for Y in i:
  Q=B+Y
  for F in range(0,C):J[Q][F]=A
  for F in range(H+1,b):J[Q][F]=A
 for Z in k:
  l=C+Z
  for E in range(0,B):J[E][l]=A
  for E in range(G+1,a):J[E][l]=A
 return J