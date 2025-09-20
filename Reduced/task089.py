R=range
"Task 089: Compact non-DSL solution for ARC task 3e980e27.\n\nBehavior summary:\n- Find diagonal-connected objects of non-background pixels.\n- For color 2 and color 3 separately:\n  - Take the largest object that contains that color, vertically mirror it,\n    and normalize it so the upper-left of that color's pixels is at (0,0).\n  - Paste this template at the center of every other object that contains\n    that color.\n- Paint all pasted templates onto the original grid.\n"
from collections import deque
from typing import Iterable,List,Tuple
Grid=Tuple[Tuple[int,...],...]
Pixel=Tuple[int,Tuple[int,int]]
Object=Tuple[Pixel,...]
def mostcolor(grid):
	A={}
	for C in grid:
		for B in C:A[B]=A.get(B,0)+1
	return max(A,key=A.get)
def neighbors8(i,j):
	for A in(-1,0,1):
		for B in(-1,0,1):
			if A==0 and B==0:continue
			yield(i+A,j+B)
def objects_diag_nonbg(grid):
	A=grid;G,H=len(A),len(A[0]);L=mostcolor(A);D=[[False]*H for A in R(G)];M=[]
	for E in R(G):
		for F in R(H):
			if D[E][F]or A[E][F]==L:continue
			N=[];I=deque([(E,F)]);D[E][F]=True
			while I:
				J,K=I.popleft();N.append((A[J][K],(J,K)))
				for(B,C)in neighbors8(J,K):
					if 0<=B<G and 0<=C<H and not D[B][C]and A[B][C]!=L:D[B][C]=True;I.append((B,C))
			M.append(tuple(N))
	return M
def palette(obj):return{A for(A,B)in obj}
def bbox_indices(indices):A=indices;A=list(A);B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
def ul_lr(obj):return bbox_indices(A for(B,A)in obj)
def vmirror(obj):A,B,A,C=ul_lr(obj);D=B+C;return tuple((A,(B,D-C))for(A,(B,C))in obj)
def shift_obj(obj,delta):A,B=delta;return tuple((C,(D+A,E+B))for(C,(D,E))in obj)
def center(obj):A,B,C,D=ul_lr(obj);return A+(C-A)//2,B+(D-B)//2
def paint(grid,obj_pixels):
	A=grid;E,F=len(A),len(A[0]);B=[list(A)for A in A]
	for(G,(C,D))in obj_pixels:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def normalize_template_by_color(obj,color):
	A=[B for(A,B)in obj if A==color]
	if not A:return
	B,C,D,D=bbox_indices(A);return shift_obj(obj,(-B,-C))
def solve_3e980e27(I):
	G=objects_diag_nonbg(I);D=[]
	for A in(2,3):
		B=[B for B in G if A in palette(B)]
		if len(B)<=1:continue
		C=max(B,key=len);H=vmirror(C)if A==2 else C;E=normalize_template_by_color(H,A)
		if E is None:continue
		for F in B:
			if F is C:continue
			J,K=center(F);D.extend(shift_obj(E,(J,K)))
	L=paint(I,D);return L
def _to_list_grid(grid):
	A=grid
	if isinstance(A,tuple):return[list(A)for A in A]
	return A
def p(g):return _to_list_grid(solve_3e980e27(g))