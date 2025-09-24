R=range
W=enumerate
T=tuple
z=len
def s(I):
 a=I;K,L=z(a),z(a[0])
 def M(g,v):return{(a,C)for(a,B)in W(g)for(C,D)in W(B)if D==v}
 def G(c):a=c;B=min(a for(a,B)in a);C=min(a for(B,a)in a);return B,C
 def A(c):
  a=c
  if not a:return 0,0,-1,-1
  B=min(a for(a,B)in a);C=max(a for(a,B)in a);D=min(a for(B,a)in a);E=max(a for(B,a)in a);return B,D,C,E
 def b(g):return T(T(a)for a in zip(*g[::-1]))
 def c(g):return T(T(a[::-1])for a in g[::-1])
 def d(g):return T(T(a[::-1])for a in zip(*g[::-1]))[::-1]
 def N(c):
  a=c
  if not a:return{*()}
  B,C=G(a);return{(a-B,D-C)for(a,D)in a}
 def e(c):
  a=c
  if not a:return 0,0
  B,C,D,E=A(a);return D-B+1,E-C+1
 def f(g,v,c):
  a=[list(a)for a in g]
  for(B,C)in c:
   if 0<=B<K and 0<=C<L:a[B][C]=v
  return T(T(a)for a in a)
 B=M(a,1);g=M(a,4)
 if not B:return a
 O=min(a for(a,B)in B);h=max(a for(a,B)in B);P=min(a for(B,a)in B);i=max(a for(B,a)in B);C=T(T(a[B][P:i+1])for B in R(O,h+1));H=[C,b(C),c(C),d(C)]
 def j(g):return T(T(a[::-1])for a in g)
 H+=[j(a)for a in H];r={*()}
 for S in H:
  D={(a,C)for(a,B)in W(S)for(C,D)in W(B)if D==4};J={(a,C)for(a,B)in W(S)for(C,D)in W(B)if D==1};k=g;t=G(D)if D else(0,0);U=G(J)if J else(0,0);l=U[0]-t[0];m=U[1]-t[1];V=N(D);n=N(J);w,X=e(V);Y=K-w+1;Z=L-X+1
  if Y<0 or Z<0:continue
  for E in R(Y):
   for F in R(Z):
    o={(a+E,B+F)for(a,B)in V};p={(a,B)for(a,B)in k if E<=a<E+w and F<=B<F+X}
    if p==o:q={(a+E+l,B+F+m)for(a,B)in n};r.update(q)
 return f(a,1,r)
def p(g):
 a=s(g)
 if isinstance(a,T):return[list(a)for a in a]
 return a