p=lambda g:[[C if any(g[A+C][B+D]==0 for(C,D)in[(0,1),(1,0),(0,-1),(-1,0)]if 0<=A+C<len(g)and 0<=B+D<len(g[0]))and C!=0 else 0 for(B,C)in enumerate(B)]for(A,B)in enumerate(g)]
