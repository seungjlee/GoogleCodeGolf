r=range;l=len;M=max;s=set;m=min
def p(g):
 A=[A[:]for A in g];G,H=l(A),l(A[0]);L=[B for A in A for B in A];Q=M(s(L),key=L.count);F=[[0]*H for A in r(G)];I=[]
 for B in r(G):
  for C in r(H):
   if A[B][C]==Q or F[B][C]:continue
   mm=A[B][C];J=[(B,C)];N=[];F[B][C]=1
   while J:
    O,P=J.pop();N+=[(O,P)]
    for(R,S)in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
     D,E=O+R,P+S
     if 0<=D<G and 0<=E<H and not F[D][E]and A[D][E]==mm:F[D][E]=1;J+=[(D,E)]
   I+=[(mm,N)]
 from collections import Counter as T;K=T(A for(A,B)in I)
 if not K:return A
 U=M(K.keys(),key=lambda c:(K[c],c));V=[B for(A,B)in I if A==U]
 def W(cells):A=cells;B=[A for(A,B)in A];C=[A for(B,A)in A];return m(B),m(C),M(B),M(C)
 X,Y,Z,a=min((W(A),)for A in V)[0];return[A[Y:a+1]for A in A[X:Z+1]]