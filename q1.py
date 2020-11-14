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
  if(emp1 == root):
   rootFound = True
  return emp1
 return lca(employeeTree[emp1][0], employeeTree[emp2][0])	  
      
def equalLevel(lev1,lev2,emp):
 while(lev1!=lev2):
  emp = employeeTree[emp][0]
  lev1-=1  
 return emp

def makeTree(data):
 for i in range(0, len(data)):
  key= "L"+str(i);
  for j in data[key]:
   if(key == "L0"):
    root = j['name']
    employeeTree[j['name']] = ["000",0]
   else:
    employeeTree[j['name']] = [j['parent'], i]

def printResult(inputList,rootFound):         
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
 
def checkRoot(inputList):
 for e in range(1, len(inputList)-1):
  if(e == root):
   return True
 return False  

def main(rootFound):
 f = open("org.json","r") 
 data = json.load(f)  
 makeTree(data)    	   

 inputList = input("").split()
 rootFound = checkRoot(inputList)
 
 if(rootFound == False): 
  for e in range(1, len(inputList)-1):
   emp1 = inputList[e] 
   emp2 = inputList[e+1]

   if(emp1 == emp2):
    lcaOfPairs.append(employeeTree[emp1][0])
    continue
   
   e1List = employeeTree[emp1]
   el1 = e1List[1]
   e2List = employeeTree[emp2]
   el2 = e2List[1]
  
   if(el1 == el2):
    temp = lca(emp1, emp2)
    lcaOfPairs.append(temp)
   
   elif(el1 > el2):
    emp1 = equalLevel(el1,el2,emp1)
    if(emp1 == emp2):
     lcaOfPairs.append(employeeTree[emp1][0])
     continue   
     
    temp = lca(emp1, emp2)
    lcaOfPairs.append(temp)
    continue
  
   emp2 = equalLevel(el2,el1,emp2) 
  
   if(emp1 == emp2):
    lcaOfPairs.append(employeeTree[emp1][0])
   else:
    temp = lca(emp1, emp2)
    lcaOfPairs.append(temp) 
   
  f.close()
  printResult(inputList,rootFound)
      
  
if __name__=="__main__": 
 main(False) 
  

