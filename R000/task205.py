L=len
R=range
S=sum
def p(g):
 if not g or not g[0]:return[]
 f,T=L(g),L(g[0]);M=set();e=[]
 for C in R(f):
  for z in R(T):
   if(C,z)in M:continue
   u=g[C][z];O=[(C,z)];p=[];M.add((C,z))
   while O:
    U,d=O.pop();p+=[(U,d)]
    for(Y,Z)in((1,0),(-1,0),(0,1),(0,-1)):
     n,J=U+Y,d+Z
     if 0<=n<f and 0<=J<T and(n,J)not in M and g[n][J]==u:M.add((n,J));O+=[(n,J)]
   if L(p)>L(e):e=p
 s=min(t for(t,_)in e);b=max(t for(t,_)in e);c=min(t for(_,t)in e);x=max(t for(_,t)in e);g=[t[c:x+1]for t in g[s:b+1]]
 if not g:return[]
 m=[t[:]for t in g];o=[e for t in m for e in t];H=max(set(o),key=o.count);t=[t[:]for t in m];K,l=L(t),L(t[0])
 while t and S(1 for t in t[0]if t==H)*2<=l:t.pop(0);K-=1
 while t and S(1 for t in t[-1]if t==H)*2<=l:t.pop();K-=1
 if not t:return[]
 e=list(zip(*t))
 while e and S(1 for t in e[0]if t==H)*2<=L(t):e.pop(0)
 while e and S(1 for t in e[-1]if t==H)*2<=L(t):e.pop()
 if not e:return[]
 m=[list(t)for t in zip(*e)];o=[e for t in m for e in t];H=max(set(o),key=o.count);g=min(set(o),key=o.count);K,l=L(m),L(m[0]);N=[[H]*l for t in R(K)];r=[(t,C)for(t,e)in enumerate(m)for(C,m)in enumerate(e)if m==g]
 if not r:return N
 t={t for(t,_)in r};e={t for(_,t)in r}
 for C in t:N[C]=[g]*l
 for z in e:
  for C in R(K):N[C][z]=g
 return N