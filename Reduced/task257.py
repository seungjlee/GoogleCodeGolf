def p(g,R=range(4)):
 for A in R:
  for B in R:
   if g[A][B]<1:
    if g[A][B+5]:g[A][B]=g[A][B+5]
   if g[A][B]<1:
    if g[A+5][B]:g[A][B]=g[A+5][B]
   if g[A][B]<1:
    if g[A+5][B+5]:g[A][B]=g[A+5][B+5]
 return[A[:4]for A in g[:4]]