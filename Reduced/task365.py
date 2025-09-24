R=range
def p(j):
 A,c=len(j),len(j[0]);E=-1
 for k in R(A):
  for W in R(c):
   if j[k][W]and(k<1or j[k-1][W]<1)and(W<1or j[k][W-1]<1):
    l=J=1
    while W+l<c and j[k][W+l]:l+=1
    while k+J<A and j[k+J][W]:J+=1
    a=[k[W:W+l]for k in j[k:k+J]];C=sum(k.count(2)for k in a)
    if C>E:E=C;e=a
 return e