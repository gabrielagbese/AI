m = 12
li = [1,3,5,7]
d = {}
d[0] = 'W' #last match is loser

for i in range(1,m+1) :
   di = []
   for j in li :
       if j <= i :
           a = i - j
           if d[a] == 'L' :
              di.append('L')
           else :
              di.append('W')
   if 'L' in di :
       d[i] = 'W'
   else :
       d[i] = 'L'

for i in d.items() :
   print(i)

print('-'*10)
print('the winner possition :')
for i in d.keys() :
   if d[i] == 'W' :   
       print(i,end='  ')