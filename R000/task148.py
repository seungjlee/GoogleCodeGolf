L=len
R=range
def p(g):
 A,C=[],0
 h,w=L(g),L(g[0])
 for i in R(2):
  g=[r[::-1] for r in g]
  if g[4][0]==2:
   for r in R(h):
    B=0
    for c in R(w):
     if g[r][c]>0 and B:g[r][c]=4;B=0
     elif g[r][c]==2 and g[r].count(8)>0 and g[r].count(4)<1:B=1
     if B and g[r][c]==0:g[r][c]=8
    if g[r][0]==2:
     if g[r].count(4)>0:A+=[1]
     else:A+=[0]
    if g[r][-1]==2:
     if A[C]:g[r]=[8]*(w-1)+[2]
     C+=1
 return g