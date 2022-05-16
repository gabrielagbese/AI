[[[k,l],[m,n]],[[o,p],[q,r]],[[s,t],[u,v]]] = [[[-2,-6],[-7,-5]],[[0,1], [5, -3]],[[3,-2],[4,6]]]
e = max([k,l])
f = m
if f > e :
   print('n',end=' ')
else :
   f = max([m,n])
b = min([e,f])
g = max([o,p])
c = g 
if c < b :
   print('h','q','r',end=' ')
else :
   h = q
   if h > g :
       c = min([g,h])
       print('r',end=' ')
   else :
       h = max([q,r])
       c = min([g,h])
i = max([s,t])
d = i
if i < c or i < b :
   print('j','u','v',end=' ')
else :
   j = u 
   if j > i :
       print('v')