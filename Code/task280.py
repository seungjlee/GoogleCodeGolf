def p(I):
	def c(grid):A={};[A.__setitem__(B,A.get(B,0)+1)for C in grid for B in C];return max(A,key=A.get)
	O=c(I);H,J=len(I),len(I[0]);M=[[0]*J for A in range(H)];P=[]
	for A in range(H):
		for B in range(J):
			if M[A][B]or I[A][B]==O:continue
			Q=[(A,B)];M[A][B]=1;X=[]
			while Q:D,E=Q.pop();d=I[D][E];X.append((d,(D,E)));[Q.append((A,B))or M[A].__setitem__(B,1)for(A,B)in[(D-1,E),(D+1,E),(D,E-1),(D,E+1)]if 0<=A<H and 0<=B<J and not M[A][B]and I[A][B]!=O]
			P.append(X)
	K=lambda patch:list(patch)if not patch or not(isinstance(next(iter(patch)),tuple)and len(next(iter(patch)))==2 and isinstance(next(iter(patch))[1],tuple))else[A for(B,A)in patch]
	def F(patch):A=K(patch);B,C=[A for(A,B)in A],[A for(B,A)in A];return min(B),max(B),min(C),max(C)
	R=lambda patch:0 if not patch else F(patch)[1]-F(patch)[0]+1;S=lambda patch:0 if not patch else F(patch)[3]-F(patch)[2]+1;T=lambda patch:F(patch)[0];Y=lambda patch:F(patch)[1];U=lambda patch:F(patch)[2];Z=lambda patch:F(patch)[3];e=lambda patch:S(K(patch))==1 and R(K(patch))==len(K(patch))if K(patch)else 0
	def f(a,b):A,B,C,D=*a,*b;E,F,G,H=min(A,C),max(A,C)+1,min(B,D),max(B,D)+1;return{(A,B)for B in range(G,H)}if A==C else{(A,B)for A in range(E,F)}if B==D else{(A,B)for(A,B)in zip(range(E,F),range(G,H))}if C-A==D-B else{(A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1))}if C-A==B-D else set()
	g=lambda start,direction:f(start,(start[0]+42*direction[0],start[1]+42*direction[1]));V=[]
	for G in P:
		C={B for(A,B)in G if A==2}
		if not C:continue
		h,i,j,k=Y(C)==Y(G),Z(C)==Z(G),T(C)==T(G),U(C)==U(G);l,m=(1 if h else 0)+(-1 if j else 0),(1 if i else 0)+(-1 if k else 0);D,E=T(C)+R(C)//2,U(C)+S(C)//2;L=g((D,E),(l,m));V.append(L)
	n={B for A in V for B in A};N=[list(A)for A in I]
	for(A,B)in n:
		if 0<=A<H and 0<=B<J:N[A][B]=2
	W=set()
	for(G,L)in zip(P,V):
		o=e(L);a=min(R(G),S(G))
		for b in range(-(a-1),a):
			if o:W.update({(A,B+b)for(A,B)in L})
			else:W.update({(A+b,B)for(A,B)in L})
	for(A,B)in W:
		if 0<=A<H and 0<=B<J and N[A][B]==O:N[A][B]=3
	return N