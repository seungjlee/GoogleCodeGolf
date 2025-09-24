t=range;u=len;v=sorted;w=min;y=max
def p(j):
 d=1;from collections import Counter as e,deque;N,V=u(j),u(j[0]);F=e(B for A in j for B in A).most_common(1)[0][0];R=[[0]*V for A in t(N)];O=[]
 for G in t(N):
  for H in t(V):
   if R[G][H]or j[G][H]==F:continue
   S=j[G][H];W=deque([(G,H)]);R[G][H]=1;T=[(G,H)]
   while W:
    C,A=W.popleft()
    for f in(-1,0,1):
     for g in(-1,0,1):
      if f==g==0:continue
      I,J=C+f,A+g
      if 0<=I<N and 0<=J<V and not R[I][J]and j[I][J]==S:R[I][J]=1;W+=[(I,J)];T+=[(I,J)]
   h=[A for(A,B)in T];K=[A for(B,A)in T];O+=[(S,T,(w(h),w(K),y(h),y(K)))]
 if not O:return j
 O.sort(key=lambda x:u(x[1]),reverse=d);X=O[0];Y=O[1:]
 if not Y:return j
 o,p,q,r=X[2];Z=e(A for(A,B,__)in Y).most_common(1)[0][0];P={};l={*()}
 for(C,A)in X[1]:
  l.add(A)
  if C in P:a,B=P[C];P[C]=w(a,A),y(B,A)
  else:P[C]=A,A
 m,i={*()},{}
 for(C,(a,B))in P.items():
  for A in t(a+1,B):
   if j[C][A]==F:m.add(A);i[A]=i.get(A,0)+1
 U={}
 for(C,A)in X[1]:U.setdefault(A,[]).append(C)
 for K in U.values():K.sort()
 b={}
 for(S,n,s)in Y:
  if S!=Z:continue
  for(C,A)in n:b.setdefault(A,[]).append(C)
 for K in b.values():K.sort()
 c=[]
 for(D,E)in U.items():
  k=b.get(D)
  if not k or k[-1]<E[-1]:continue
  Q=0;L=E[0]
  for M in E[1:]:
   if M-L>1:
    for B in t(L+1,M):
     if j[B][D]==F:Q=d;break
    if Q:break
   L=M
  if not Q:
   for B in t(E[-1]+1,N):
    if j[B][D]==F:Q=d;break
  if Q:c+=[D]
 if not c:return j
 for D in v(c):
  E=U[D];L=E[0]
  for M in E[1:]:
   for B in t(L+1,M):
    if j[B][D]==F:j[B][D]=Z
   L=M
  for B in t(E[-1]+1,N):
   if j[B][D]==F:j[B][D]=Z
 return j