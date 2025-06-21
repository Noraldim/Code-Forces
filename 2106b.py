t = int(input())

for _ in range(t) :
    size , color = map(int, input().split()) 
    if size == 1 :
        print(0)
        continue
    if color == 0:
        nlist = list(range(1,size)) + [0]
        print(*nlist)
        continue
    if color >= size:
        xx =  list(range(size))
        print(*xx)
        continue
    
    llm = list(range(size))
    llm.remove(color)
    llm.append(color)
    print(*llm)
   
