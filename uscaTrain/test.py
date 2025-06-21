"""
ID: norkh121
LANG: PYTHON3
TASK: test
"""


fin = open('test.in','r')
fout = open('test.out', 'w')

x,y = map(int, fin.readline().split())
result = x+y
fout.write(str(result) + '\n')
fout.close()
