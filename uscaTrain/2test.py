"""
ID: norkh121
LANG: PYTHON3
TASK: ride 
"""


fin = open('ride.in','r')
fout = open('ride.out', 'w')

#comet = list(map(int,fin.readline().split()))
#group = list(map(int,fin.readline().split()))
commet = fin.readline().strip()
group  = fin.readline().strip()

num = list(range(1,28))
lett = []
for i in range(ord('A'),ord('Z')+1):
    lett.append(chr(i))

val_dec = {}
res =1
resx = 1
for x in range(len(lett)):
    val_dec[lett[x]] = num[x]
for x in commet:
    xx = val_dec[x]
    res = res * xx
for x in group:
    yy = val_dec[x]
    resx = resx * yy

if (res%47)==(resx%47):
    fout.write(str('GO') + '\n')
else:
    fout.write(str('STAY')+ '\n')

