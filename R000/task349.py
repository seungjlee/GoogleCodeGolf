z=len;m=min;x=max;r=range
def p(I):
 A=[A[:]for A in I];B,D=z(A),z(A[0]);from collections import Counter as a,deque;T=a([B for A in A for B in A]).most_common(1)[0][0];M=[[0]*D for A in r(B)];U=[]
 for E in r(B):
  for C in r(D):
   if M[E][C]:continue
   M[E][C]=1;J=A[E][C]
   if J==T:continue
   s=deque([(E,C)]);F=[(E,C)]
   while s:
    K,L=s.popleft()
    for V in(-1,0,1):
     for W in(-1,0,1):
      if V==0 and W==0:continue
      G,H=K+V,L+W
      if 0<=G<B and 0<=H<D and not M[G][H]and A[G][H]==J:M[G][H]=1;s+=[(G,H)];F+=[(G,H)]
   U+=[(J,F)]
 for E in r(B):
  for C in r(D):
   if A[E][C]==9:
    for X in r(E,B):
     if A[X][C]==T:A[X][C]=1
 for(J,F)in U:
  if J!=9 or not F:continue
  b=m(A for(A,B)in F);c=x(A for(A,B)in F);Y=m(A for(B,A)in F);Z=x(A for(B,A)in F);d=(Z-Y+1)//2
  for N in r(1,d+1):
   O,P=b-N,c+N;Q,R=Y-N,Z+N
   if 0<=O<B:
    for L in r(x(0,Q),m(D,R+1)):A[O][L]=3
   if 0<=P<B:
    for L in r(x(0,Q),m(D,R+1)):A[P][L]=3
   if 0<=Q<D:
    for K in r(x(0,O),m(B,P+1)):A[K][Q]=3
   if 0<=R<D:
    for K in r(x(0,O),m(B,P+1)):A[K][R]=3
 return A