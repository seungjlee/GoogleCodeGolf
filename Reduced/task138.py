def p(g):
	o=False;O=True;from collections import Counter as p,deque;I,J=len(g),len(g[0]);M=[[o]*J for A in range(I)];P=[]
	for A in range(I):
		for B in range(J):
			if g[A][B]==0 and not M[A][B]:
				Q=deque([(A,B)]);M[A][B]=O;D=[];R=A==0 or B==0 or A==I-1 or B==J-1
				while Q:
					a,b=Q.popleft();D.append((a,b))
					for(q,r)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=a+q,b+r
						if 0<=E<I and 0<=F<J and not M[E][F]and g[E][F]==0:M[E][F]=O;R=R or(E==0 or F==0 or E==I-1 or F==J-1);Q.append((E,F))
				if not R:P.append(D)
	if not P:return[A[:]for A in g]
	D=max(P,key=len);s,t,u,v=min(A for(A,B)in D),min(A for(B,A)in D),max(A for(A,B)in D),max(A for(B,A)in D);w,x,y,z=max(0,s-1),max(0,t-1),min(I-1,u+1),min(J-1,v+1);G=[A[x:z+1]for A in g[w:y+1]];c,d=len(G),len(G[0]);e=p(B for A in G for B in A);A0=max(e,key=e.get);f,S,T,h=set(),None,-1,-1;A1={A for B in G for A in B if A!=A0}
	for i in A1:
		C=[(A,B)for A in range(c)for B in range(d)if G[A][B]==i]
		if not C:continue
		K={}
		for(A,B)in C:
			if B in K:U,V=K[B];K[B]=min(U,A),max(V,A)
			else:K[B]=A,A
		A2={(D,A)for(A,(B,C))in K.items()for D in range(B,C+1)};L={}
		for(A,B)in C:
			if A in L:U,V=L[A];L[A]=min(U,B),max(V,B)
			else:L[A]=B,B
		A3={(A,D)for(A,(B,C))in L.items()for D in range(B,C+1)};A4,A5=min(A for(A,B)in C),max(A for(A,B)in C);j,k={B for(A,B)in C if A==A4},{B for(A,B)in C if A==A5};A6=j if len(j)>=len(k)else k;W={(B,A)for(B,A)in A2 if A in A6};A7,A8=min(A for(B,A)in C),max(A for(B,A)in C);l,m={A for(A,B)in C if B==A7},{A for(A,B)in C if B==A8};A9=m if len(m)>=len(l)else l;N={(A,B)for(A,B)in A3 if A in A9};X=o
		if len(W)>len(N):H=W
		elif len(N)>len(W):H=N;X=O
		else:H=N;X=O
		if X:
			AA=set(C);Y={};AB={A for(A,B)in C}
			for(A,_)in C:Y[A]=Y.get(A,0)+1
			if len(AB)<=2:H={A for A in H if not(A not in AA and Y.get(A[0],0)==2)}
		Z,n=len(H)-len(C),len(H)
		if Z>T or Z==T and n>h:T,h,S,f=Z,n,i,H
	if S is not None:
		for(A,B)in f:
			if 0<=A<c and 0<=B<d:G[A][B]=S
	return G
