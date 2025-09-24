C=range(10)
def p(j):
 u,v=j[0][0],j[0][9];D=[A[:]for A in j];E=u==v;F,G=(u,j[9][0])if E else(u,v);I=next(A for B in j for A in B if A and A not in[F,G])
 for A in C:
  for B in C:
   if j[A][B]==I:H=(A,9-A)if E else(B,9-B);D[A][B]=F if H[0]<H[1]else G
 return D