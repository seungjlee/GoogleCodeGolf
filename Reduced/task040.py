def p(j):
 C=range(10);D=[A[:]for A in j];E=j[0][0]==j[0][9];F,G=(j[0][0],j[9][0])if E else(j[0][0],j[0][9]);I=next(A for B in j for A in B if A and A not in[F,G])
 for A in C:
  for B in C:
   if j[A][B]==I:H=(A,9-A)if E else(B,9-B);D[A][B]=F if H[0]<H[1]else G
 return D