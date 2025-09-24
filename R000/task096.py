m=max;x=min;l=len;r=range;s=set;T=tuple;a=abs
def c(e):A=e;B=[B for A in A for B in A]if isinstance(A,(T,list))else[A[0]for A in A];return m(s(B),key=B.count)
def n(lc):A,B=lc;return{(A-1,B-1),(A-1,B),(A-1,B+1),(A,B-1),(A,B+1),(A+1,B-1),(A+1,B),(A+1,B+1)}
def j(g):
	A=g
	if not A or not A[0]:return s()
	return{(B,C)for B in r(l(A))for C in r(l(A[0]))}
def ulcorner(P):A=k(P);return x(A for(A,B)in A),x(A for(B,A)in A)
def lrcorner(P):A=k(P);return m(A for(A,B)in A),m(A for(B,A)in A)
def k(P):
	A=P
	if l(A)==0:return s()
	B=next(iter(A))
	if isinstance(B,T)and l(B)==2 and isinstance(B[1],T):return{A for(B,A)in A}
	return A
def shift(P,t):
	A=P
	if l(A)==0:return A
	C,D=t;B=next(iter(A))
	if isinstance(B,T)and l(B)==2 and isinstance(B[1],T):return{(A,(B+C,E+D))for(A,(B,E))in A}
	return{(A+C,B+D)for(A,B)in A}
def o(P):
	A=P
	if l(A)==0:return A
	return shift(A,(-v(A),-y(A)))
def d(loc):A=loc;return{(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)}
def objects(g,u,i,w):
	A=g;H=c(A)if w else None;I=[];D=s();L,M=l(A),l(A[0]);N=j(A);O=n if i else d
	for B in N:
		if B in D:continue
		E=A[B[0]][B[1]]
		if E==H:continue
		J={(E,B)};F={B}
		while F:
			K=s()
			for C in F:
				G=A[C[0]][C[1]]
				if E==G if u else G!=H:J.add((G,C));D.add(C);K|={(A,B)for(A,B)in O(C)if 0<=A<L and 0<=B<M}
			F=K-D
		I.append(J)
	return I
def f(g):A=g;B=c(A);return[{(A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B}for B in q(A)-{B}]
def v(P):return x(A for(A,B)in k(P))
def y(P):return x(A for(B,A)in k(P))
def z(P):return m(A for(B,A)in k(P))
def h(a,b):return x(abs(A-C)+abs(B-D)for(A,B)in k(a)for(C,D)in k(b))
def q(element):
	A=element
	if isinstance(A,(T,list)):return{B for A in A for B in A}
	return{A[0]for A in A}
def rot90(g):return[list(A)for A in zip(*g[::-1])]
def hmirror(piece):
	A=piece;C=ulcorner(A)[0]+lrcorner(A)[0];B=next(iter(A))
	if isinstance(B,T)and l(B)==2 and isinstance(B[1],T):return{(A,(C-B,D))for(A,(B,D))in A}
	return{(C-A,B)for(A,B)in A}
def vmirror(piece):
	A=piece;C=ulcorner(A)[1]+lrcorner(A)[1];B=next(iter(A))
	if isinstance(B,T)and l(B)==2 and isinstance(B[1],T):return{(A,(B,C-D))for(A,(B,D))in A}
	return{(A,C-B)for(A,B)in A}
def dmirror(piece):
	A=piece;B,C=ulcorner(A);D=next(iter(A))
	if isinstance(D,T)and l(D)==2 and isinstance(D[1],T):return{(A,(E-C+B,D-B+C))for(A,(D,E))in A}
	return{(D-C+B,A-B+C)for(A,D)in A}
def cmirror(piece):return vmirror(dmirror(vmirror(piece)))
def paint(g,obj):
	A=g;E,F=l(A),l(A[0]);B=[list(A)for A in A]
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return B
def canvas(value,dimensions):A=dimensions;return[[value for A in r(A[1])]for B in r(A[0])]
def p(I):
	if not isinstance(I,T):I=T(T(A)for A in I)
	G=c(I);B=f(I);H=objects(I,True,False,True)
	def J(area):
		D=next(iter(area))[0];A=[A for A in H if next(iter(A))[0]==D]
		if A:B=m((z(A)-y(A)+1 for A in A),default=0)
		else:B=0
		E={h(C,B)for B in A for C in A};F={A for A in E if A!=0};C=x(F,default=0);G=C-1 if C>0 else-2;return-(2*B+G)
	K=sorted(B,key=J)
	def L(area):
		A=area
		def B(piece):return T(sorted(k(o(piece))))
		C=vmirror(A),dmirror(A),cmirror(A),hmirror(A);return x(C,key=B)
	M=[L(A)for A in K];N=T(o(A)for A in M);C=l(B);D=C if any(l(A)==1 for A in B)else C+1;O=T((A,A)for A in r(D));E=T(C for(A,B)in zip(N,O)for C in sorted(shift(A,B),key=lambda t:t[1]));F=2*D-1;A=canvas(G,(F,F))
	for _ in r(3):A=paint(A,E);A=rot90(A)
	A=paint(A,E);return A