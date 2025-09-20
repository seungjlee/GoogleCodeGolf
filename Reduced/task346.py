from collections import*
def p(n):
 for p in range(0,len(n)-3+1,1):
  for o in range(0,len(n[0])-3+1,1):
   r=n[p:p+3];r=[p[o:o+3]for p in r];o=[o for o in r for o in o];l=Counter(o).most_common(1)
   if min(o)>0and l[0][1]==8:return[[r[1][1]]]