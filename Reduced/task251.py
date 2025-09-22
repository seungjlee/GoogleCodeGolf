def p(j,R=range):
 c,E=len(j),len(j[0]);k=[[0]*E for c in R(c)];W=[]
 for l in R(c):
  for J in R(E):
   if l*J==0 or l==c-1 or J==E-1:
    if j[l][J]==0:k[l][J]=1;W+=[(l,J)]
 while W:
  a,C=W.pop(0)
  for(e,K)in[(-1,0),(1,0),(0,-1),(0,1)]:
   w,L=a+e,C+K
   if 0<=w<c and 0<=L<E and j[w][L]==0 and not k[w][L]:k[w][L]=1;W+=[(w,L)]
 b=[[j[c][E]if j[c][E]!=0 or k[c][E]else 1 for E in R(E)]for c in R(c)];return b