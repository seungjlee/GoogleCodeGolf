L=len
S=sorted
T=tuple
def p(g):
 if not g or not g[0]:return[A[:]for A in g]
 B=[A[:]for A in g];H,I=L(B),L(B[0]);from collections import Counter as Z
 def Q(g):A=Z(B for A in g for B in A);return max(A,key=lambda k:A[k])
 def a(i,j):
  for A in(-1,0,1):
   for B in(-1,0,1):
    if A==0 and B==0:continue
    C,D=i+A,j+B
    if 0<=C<H and 0<=D<I:yield(C,D)
 def b(g):
  A=g;P=Q(A);J,K=L(A),L(A[0]);D=set();l=[]
  for E in range(J):
   for F in range(K):
    if(E,F)in D:continue
    G=A[E][F]
    if G==P:continue
    H=set();I={(E,F)}
    while I:
     M=set()
     for(B,C)in I:
      if(B,C)in D:continue
      W=A[B][C]
      if W==G:
       H.add((B,C));D.add((B,C))
       for(N,O)in a(B,C):
        if 0<=N<J and 0<=O<K:M.add((N,O))
     I=M-D
    if H:l+=[(G,T(S(H)))]
  return l
 def C(q):return min(A for(A,B)in q)
 def J(q):A=q;return min(A for(A,B)in A),min(A for(B,A)in A)
 def W(c,dv):A,B=c;C,D=dv;return A,T(S((A+C,B+D)for(A,B)in B))
 s=Q(B);c=b(B);t={}
 for(K,A)in c:t[A]=K
 u=[(B,A)for(A,B)in t.items()]
 if not u:return[A[:]for A in B]
 D=S(u,key=lambda cp:(C(cp[1]),J(cp[1])[1]));l=C(D[0][1]);E=l
 for V in range(l+1,H):
  if any(B[V][A]!=s for A in range(I)):E=V
  elif E>=l:break
 F=set();M=D[0][0]
 for(K,A)in D:
  if C(A)<=E:F.update(A)
  else:break
 d=min(A for(A,B)in F);e=min(A for(B,A)in F);f=T(S((A-d,B-e)for(A,B)in F));h=M,f
 def i(seq):
  F=None;G=[];A=F;B=-1
  for(J,D)in seq:
   I=C(D)
   if I<=E:continue
   H=max(A for(A,B)in D)
   if A is F or I>B+1:
    if A is not F:G+=[(M,T(S(A)))]
    A=set(D);B=H
   else:
    A.update(D)
    if H>B:B=H
  if A is not F:G+=[(M,T(S(A)))]
  return G
 j=i(D);k=[(0,2),(0,1),(0,0),(0,-1),(0,-2),(-1,0)];N=[]
 for(K,A)in j:
  l=J(A);m=W(h,l);n=[set(W(m,A)[1])for A in k];w=set(A);o=[(A,L(A&w),min(A for(A,B)in A)if A else 1e9)for A in n];X=max(o,key=lambda x:(x[1],-x[2]));Y=max(A for(B,A)in A)
  if X[1]>0:N+=[(X[0],Y)]
  else:N+=[(w,Y)]
 O=[A[:]for A in B]
 for(p,q)in N:
  for(P,G)in p:
   if G<=q:continue
   if 0<=P<H and 0<=G<I and O[P][G]==s:O[P][G]=1
 return O