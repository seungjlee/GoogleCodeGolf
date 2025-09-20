from collections import*
def p(m,u=enumerate):
	u=[(i,o)for(i,o)in u(m)for(o,n)in u(o)if n]
	if not u:return[]
	n=Counter(m[i][o]for(i,o)in u).most_common(1)[0][0];u=[(i,o)for(i,o)in u if m[i][o]==n];i,t=min(i for(i,o)in u),min(o for(o,o)in u);n,o=max(i for(i,o)in u)+1,max(o for(o,o)in u)+1;return[m[i][t:o]for i in range(i,n)]