R=range;L=len;M=max;S=sum;T=list
Z=zip
def p(o):
 o=[T(i)for i in o];s=[]
 for i in[o,[*Z(*o)]]:e=L(i);k=[-1]+[k for k in R(e)if L({*i[k]})<2]+[e];s+=[([(a+1,m)for a,m in Z(k,k[1:])if m>a+1]),]
 m,m=s;g=L(m);t=R(g);d=[[o[i[0]][k[0]]for k in m]for i in m];i=S(d,[]);l=M(i,key=i.count);e=q=0;f=[-1,0,1]
 for i in R(1,g-1):
  for k in R(1,g-1):
   if(s:=d[i][k])!=l:
    if d[i][k-1]==d[i+1][k]==d[i-1][k]!=l:e=[[d[i+n][k+y]for y in f]for n in f];q=s;break
  if e:break
 for i in t:
  for k in t:
   if d[i][k]==q:
    for n in f:
     if 0<=(l:=i+n)<g:
      for y in f:
       if 0<=(s:=k+y)<g:d[l][s]=e[n+1][y+1]
 for k,(y,t)in Z(d,m):
  for s,(i,n)in Z(k,m):
   for k in R(y,t):o[k][i:n]=[s]*(n-i)
 return o