
from collections import deque
from copy import deepcopy
print("============================================= Task 01 output =============================================")

def max_region(affected):
    max_aff = 0
    for row in range(0,len(affected)):
        for col in range(0,len(affected[0])):
            if affected[row][col]=='Y':
                victim = DFS(affected,row,col)
                max_aff = max(max_aff,victim)
    return max_aff

def DFS(affected,row,col):
    if row<0 or col<0 or row>=len(affected) or col>=len(affected[0]):
        return 0
    if affected[row][col] == "N":
        return 0

    count = 1
    affected[row][col]="N"

    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if r!=row or c!=col:
                count+=DFS(affected,r,c)
    return count 



affected=[]
with open("input_1.txt",'r') as a:
    lines = a.readlines()[:]
for line in lines:
    affected.append(line.split())   

print(max_region(affected))


print("============================================= Task 02 output =============================================")

def alien_attack(list):
    survived = 0
    q = deque()
    for row in range(0,len(list)):
        for col in range(0,len(list[0])):
            if list[row][col]=='A':
                q.append((row,col,0))
            if list[row][col]=='H':
               survived+=1
    time = 0
    
    while q:
        row, col, time = q.popleft()
        if list[row][col]=='A':
            for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
               if 0<=r<len(list) and 0<=c<len(list[0]) and list[r][c]=="H":
                    list[r][c]='A'
                    survived-=1
                    q.append((r,c,time+1))
    
    
    result = 'Time: '+str(time)+' minutes'+'\n'+str(survived)+' survived'
    
    return result

list=[]
with open("input_2.txt",'r') as f:
    lines = f.readlines()[2:]
  
for line in lines:
    list.append(line.split())   

print(alien_attack(list))