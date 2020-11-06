import json 
employeeTree = {}
dfs =[]
dfs1 =[]
root = None
E1 = None
E2 = None
empCurr = None
rootFound = False
lcaOfPairs = []
def lca(emp1, emp2):
 if(emp1 == emp2):
  #print(emp1)
  #print(E1, " is ",int(employeeTree[E1][1])-int(employeeTree[emp1][0])," below ",emp1)
  #print(E2, " is ",int(employeeTree[E2][1])-int(employeeTree[emp1][0])," below ", emp1)
  if(emp1 == root):
   rootFound = True
   #print(rootFound)
  return emp1
 else:
  return lca(employeeTree[emp1][0], employeeTree[emp2][0])	  
      
f = open("org.json","r") 
data = json.load(f) 


for i in range(0, len(data)):
 key= "L"+str(i);
 for j in data[key]:
  if(key == "L0"):
   root = j['name']
   employeeTree[j['name']] = ["000",0]
  else:
   employeeTree[j['name']] = [j['parent'], i]    	   

#print(employeeTree)


inputList = input("").split()
#print(inputList)
#print("\n")
#emp1 = inputList[1]  
for e in range(1, len(inputList)-1):
 #E1 = emp1
 #E2 = inputList[e]
 emp1 = inputList[e] 
 emp2 = inputList[e+1]
 #print(emp1, emp2)
 #print("\n")
 if(emp1 == root or emp2 == root):
  #print("No LCA")
  rootFound = True
  break
 elif(emp1 == emp2):
  lcaOfPairs.append(employeeTree[emp1][0])
  #print()
  #print(E1, " is 1 level below ",employeeTree[emp1][0])
  #print(E2, " is 1 level below ",employeeTree[emp2][0]) 
 else:
  e1List = employeeTree[emp1]
  el1 = e1List[1]
  e2List = employeeTree[emp2]
  el2 = e2List[1]
  #print("\n")
  #print(el1,el2)
  if(el1 == el2):
   temp = lca(emp1, emp2)
   lcaOfPairs.append(temp)
   #print(emp1)
  elif(el1 > el2):
   while(el1!=el2):
    emp1 = employeeTree[emp1][0]
    el1-=1
   if(emp1 == emp2):
    lcaOfPairs.append(employeeTree[emp1][0])
    #print(ans)
    #print(E1, " is ",int(employeeTree[E1][1])-int(employeeTree[ans][0])," below ",ans)
    #print(E2, " is ",int(employeeTree[E2][1])-int(employeeTree[ans][0])," below ", ans)   
   else:  
    temp = lca(emp1, emp2)
    lcaOfPairs.append(temp)
  else:
   while(el1!=el2):
    emp2 = employeeTree[emp2][0]
    el2-=1
   if(emp1 == emp2):
    lcaOfPairs.append(employeeTree[emp1][0])
    #print(ans)
    #print(E1, " is ",int(employeeTree[E1][1])-int(employeeTree[ans][0])," below ",ans)
    #print(E2, " is ",int(employeeTree[E2][1])-int(employeeTree[ans][0])," below ", ans)  
   else:
    temp = lca(emp1, emp2)
    lcaOfPairs.append(temp) 

 f.close()
if(rootFound):
 print("No LCA")
 
else:
 level = 999999
 ansEmp = None 
 for emp in lcaOfPairs:
  if(int(employeeTree[emp][0]) < level):
   level = int(employeeTree[emp][0])
   ansEmp = emp
 print(ansEmp)  
 for e in range(1,len(inputList)):
  print(ansEmp, " is ",int(employeeTree[inputList[e]][1])-int(employeeTree[ansEmp][0])," level above ",inputList[e])
  
