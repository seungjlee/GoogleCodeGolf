E=enumerate
def p(g):g=[[v if(i and g[i-1][j]==v)+(i+1<len(g)and g[i+1][j]==v)+(j and r[j-1]==v)+(j+1<len(g)and r[j+1]==v)>1else 0 for j,v in E(r)]for i,r in E(g)];f=sum(g,[]);C=sorted([[f.count(c),c]for c in set(f)if c>0]);g=[[0 if c!=C[-1][1]else c for c in r]for r in g];return g
