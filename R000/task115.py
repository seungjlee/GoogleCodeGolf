def p(n):
 def i(n):
  t=[]
  for n in n:
   if n not in t:t.append(n)
  return t
 d=[i(t)for t in n]
 if all(d[0]==t for t in d):return[d[0]]
 return[[n]for n in i([n for t in n for n in t])]