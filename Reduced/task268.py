E=enumerate
Q=list
R=range
X=len
def mc(g):a=[b for a in g for b in a];return max(set(a),key=a.count)
def oc(g,v):return{(a,c)for(a,b)in E(g)for(c,d)in E(b)if d==v}
def V(g,v,c):
 b=c;a=g
 if not b:return[Q(a)for a in a]
 f,g=X(a),X(a[0]);c=[Q(a)for a in a]
 for(d,e)in b:
  if 0<=d<f and 0<=e<g:c[d][e]=v
 return c
def bb(i):a=i;b=min(a for(a,b)in a);c=min(a for(b,a)in a);d=max(a for(a,b)in a);e=max(a for(b,a)in a);return b,c,d,e
def po(a,b):
 e,F,G,H=bb(a);I,J,K,L=bb(b);A,B=(e+G)//2,(F+H)//2;C,D=(I+K)//2,(J+L)//2
 if A==C:return 0,1 if B<D else-1
 if B==D:return 1 if A<C else-1,0
 if A<C:return 1,1 if B<D else-1
 if A>C:return-1,1 if B<D else-1
 return 0,0
def dn(l):A,B=l;return{(A-1,B),(A+1,B),(A,B-1),(A,B+1)}
def cn(a,b):
 A,B=a;C,D=b
 if A==C:e,I=(B,D)if B<=D else(D,B);return{(A,B)for B in R(e,I+1)}
 if B==D:F,J=(A,C)if A<=C else(C,A);return{(A,B)for A in R(F,J+1)}
 G,H=C-A,D-B
 if abs(G)==abs(H):F=1 if G>0 else-1;e=1 if H>0 else-1;K=abs(G);return{(A+C*F,B+C*e)for C in R(K+1)}
 return set()
def p(I):
 A0='bottom';z='top'
 if not I or not I[0]:return[Q(A)for A in I]
 L,F=X(I),X(I[0]);G=mc(I);S={(A,B)for A in R(L)for B in R(F)if I[A][B]!=G}
 if not S:return[Q(A)for A in I]
 D,B,A,C=bb(S);A1={(A,B)for A in R(D,A+1)}|{(A,C)for A in R(D,A+1)}|{(D,A)for A in R(B,C+1)}|{(A,B)for B in R(B,C+1)};T=A1-S;A2={(A,D)for A in R(D,A+1)for D in R(B,C+1)};P=A2-S;x=po(P,T);Z=po(T,P);A3={z:sum(1 for A in R(B,C+1)if I[D][A]==G),A0:sum(1 for B in R(B,C+1)if I[A][B]==G),'left':sum(1 for A in R(D,A+1)if I[A][B]==G),'right':sum(1 for A in R(D,A+1)if I[A][C]==G)};A4={z:(-1,0),A0:(1,0),'left':(0,-1),'right':(0,1)};M=None;q=[(A,A4[B])for(B,A)in A3.items()if A]
 if q:
  q.sort(key=lambda item:item[0],reverse=1)
  if X(q)==1 or q[0][0]>q[1][0]:M=q[0][1]
 a=sum(1 for A in R(L)for C in R(B)if I[A][C]==0);b=sum(1 for A in R(L)for B in R(C+1,F)if I[A][B]==0);c=sum(1 for A in R(D)for B in R(F)if I[A][B]==0);d=sum(1 for A in R(A+1,L)for B in R(F)if I[A][B]==0);H=1 if b>a else-1 if a>b else 0;J=1 if d>c else-1 if c>d else 0
 def e(d):
  B,C=d;A=0
  if H and C==H:A+=1
  if J and B==J:A+=1
  return A
 K=M
 if K is None:
  if x==Z:
   if H==0 and J!=0:K=J,0
   elif J==0 and H!=0:K=0,H
   else:K=x
  else:
   K=max((x,Z),key=e)
   if e(K)==0 and(J or H):
    N=J if J else 0;O=H if H else 0
    if N or O:K=N,O
 N,O=K;Y=set()
 for f in R(9):
  A5,A6=N*f,O*f
  for(A7,A8)in T:Y.add((A7+A5,A8+A6))
 r=V(I,4,P);g=oc(I,0);r=V(r,4,Y&g)
 if T:h,i,j,k=bb(T);l={(h,i),(h,k),(j,i),(j,k)}
 else:l={(D,B),(D,C),(A,B),(A,C)}
 U=oc(r,0);N,O=K
 if O==0 and N!=0:U={A for A in U if B<=A[1]<=C}
 elif N==0 and O!=0:U={B for B in U if D<=B[0]<=A}
 A9=J==0 and H==0;AA=I if A9 else r
 def AB(loc):
  A=0
  for(B,C)in dn(loc):
   if 0<=B<L and 0<=C<F and AA[B][C]==0:A+=1
  return A==2
 def m(idxs,loc):return any((A,B)in idxs for(A,B)in dn(loc))
 AC=[A for A in U if AB(A)and m(S,A)and m(Y,A)];n=set()
 for v in l:
  for o in AC:p=o[0]-v[0],o[1]-v[1];AD=v[0]+42*p[0],v[1]+42*p[1];n|=cn(v,AD)
 e=V(r,4,n&g)
 if M and P:
  q={A for(B,A)in P};x={A for(A,B)in P}
  if M==(-1,0)and D>0:
   s={(D-1,A)for A in q if 0<=A<F and I[D-1][A]==G}
   if s:e=V(e,4,s)
  elif M==(1,0)and A+1<L:
   t={(A+1,B)for B in q if 0<=B<F and I[A+1][B]==G}
   if t:e=V(e,4,t)
  elif M==(0,-1)and B>0:
   u={(A,B-1)for A in x if 0<=A<L and I[A][B-1]==G}
   if u:e=V(e,4,u)
  elif M==(0,1)and C+1<F:
   v={(A,C+1)for A in x if 0<=A<L and I[A][C+1]==G}
   if v:e=V(e,4,v)
 if M==(1,0):
  AE=any(B not in(0,4)for A in I for B in A);W=A+1
  if AE or 0<=W==X(I)-1:
   w=0
   if 0<=W<X(I):
    AF=R(B+1,C)
    def AG(j):return any(B+1<=D<C and r[A][D]==4 for D in(j-1,j,j+1))
    x=tuple(A for A in AF if I[W][A]==0 and AG(A))
    if x:AH={(W,A)for A in x};e=V(e,4,AH);w=1
   if w:
    F=X(I[0]);y={(A,D)for D in R(F)if(D<B or D>C)and e[A][D]==4}
    if y:e=V(e,0,y)
 return e