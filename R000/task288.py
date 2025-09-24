from collections import Counter
def p(c):
 l,D=len(c),len(c[0]);E=Counter(z for t in c for z in t);p=min(E,key=E.get);m=[(t-1,z)for t in range(l)for z in range(D)if c[t][z]==p]
 if not m:return[t[:]for t in c]
 o=min(t for(t,z)in m);u=min(t for(z,t)in m);m=max(t for(z,t)in m);e=set();t,z=o,u
 while 0<=t<l and 0<=z<D:e.add((t,z));t-=1;z-=1
 t,z=o,m
 while 0<=t<l and 0<=z<D:e.add((t,z));t-=1;z+=1
 M=max(E,key=E.get);o=[t[:]for t in c]
 for(t,z)in e:
  if 0<=t<l and 0<=z<D and o[t][z]==M:o[t][z]=p
 return o