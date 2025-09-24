j=len
R=range
def p(c):
 I,J=j(c),j(c[0]);B=[]
 for E in R(I):
  for F in R(J):
   if c[E][F]>0:B+=[[E,F]]
 G=min([A[1]for A in B]);C=max([A[1]for A in B]);H=min([A[0]for A in B]);D=max([A[0]for A in B]);C=C-(C-G)//2;D=D-(D-H)//2;c=c[H:D];c=[A[G:C]for A in c];return c