L=len
def p(j):
 R=range;D,E=L(j),L(j[0]);B=[B for B in R(D)if all(j[B][A]==0 for A in R(E))];C=[B for B in R(E)if all(j[A][B]==0 for A in R(D))];B=[-1]+B+[D];C=[-1]+C+[E];G=[]
 for H in R(L(B)-1):
  F=[]
  for I in R(L(C)-1):
   for J in R(B[H]+1,B[H+1]):
    for K in R(C[I]+1,C[I+1]):
     if j[J][K]:F+=[j[J][K]];break
    else:continue
    break
  if F:G+=[F]
 return G