def p(u):
	o=range;y=set();u=[y[:]for y in u]
	def i(o,d):
		if(o,d)in y or not(0<=o<10 and 0<=d<10)or u[o][d]:return[]
		y.add((o,d));return[(o,d)]+sum([i(o+y,d+n)for(y,n)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
	for n in o(10):
		for b in o(10):
			if u[n][b]==0 and(n,b)not in y:
				a=i(n,b)
				for(p,r)in a:u[p][r]=abs(len(a)-4)
	return u