def p(r):
	p=[[0]*len(r[0])for a in r];n=set()
	for o in range(len(r)):
		for s in range(len(r[0])):
			if r[o][s]and(o,s)not in n:
				m,g=[(o,s)],[(o,s)];n.add((o,s));s=r[o][s]
				while g:
					a,l=g.pop()
					for(t,i)in[(0,1),(1,0),(0,-1),(-1,0)]:
						if 0<=a+t<len(r)and 0<=l+i<len(r[0])and r[a+t][l+i]==s and(a+t,l+i)not in n:n.add((a+t,l+i));m.append((a+t,l+i));g.append((a+t,l+i))
				i=max(a for(a,l)in m)-min(a for(a,l)in m)+1
				for(a,l)in m:p[a-i][l]=s
	return p