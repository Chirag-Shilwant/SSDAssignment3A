import ast,simplejson,fnmatch,os
empNum = len(fnmatch.filter(os.listdir("./Employee"),'*.txt'))

keysEmp = []
startEmp1 = []

endEmp1 = []


freeEmp1 = []

freeEmp12 = []

Emp1Time = [True] * 481

Emp12Time = [None]* 481

#sare emp ke free slots
allFreeSlots = []


tarik = None

# -------------------------------------------------sare kaam ke inputs iske aandar hai------------------------------
allLists = [] 


# yeh check kar raha hai ki dates ek hii hai ki nhi sare Emp ki
def checkDates(listFull):
 dateToCheck = listFull[0][1] 
 for l in listFull:
  if(l[1] != dateToCheck):
   return True
 
 return False 

# -------------------------------------------ye list of list (allLists) bana raha hai-------------------------------- 
for i in range(1,empNum+1):
 file = open("./Employee/Employee"+ str(i) + ".txt", "r")
 content1 = file.read()
 dictionary1 = ast.literal_eval(content1)
 value1 = dictionary1.values()
 keyy1 = dictionary1.keys()
 file.close()
 Emp1 = []
 #Emp2 = []
 for v in value1:
  key1 = v.keys()
  val1 = v.values()

 for k in keyy1: 
  keysEmp.append(k)
 
 for v in val1:
  Emp1.append(v)
  
 for k in key1:
  Emp1.append(k)

 allLists.append(Emp1)

#print("All inputs")
#print(allLists)



#---------------------------------------check kar raha hai ki dates same hai ya nahi-------------------------------
if(checkDates(allLists)):
 f = open('output3.txt', 'w')
 f.write(str("Dates Not Matching\n"))
 

else:
 #print("\n")
 #print("Same Dates go ahead\n")
 temp1 = allLists[0][0]
 tarik = allLists[0][1]
 #print(temp1)
 #startEmp1 ka
 for t in temp1:
  time = t[slice(5)]
  if(time[slice(2)]=="1:" or time[slice(2)]=="2:" or time[slice(2)]=="3:" or time[slice(2)]=="4:" or time[slice(2)]=="5:"):
   time = str(int(time[slice(1)]) + 12)
   time = time + ":" + t[slice(2,4)]
   startEmp1.append(time)
  else:
   if(time[slice(1)]=="9"):
    startEmp1.append(time[slice(4)])
   else:
    startEmp1.append(time)     
 #print("emp1 ka start time") 
 #print(startEmp1)
 
 #end Emp1 ka
 for t in temp1:
  time = t[-7:]
  if(time[-2:] == "PM" and (time[1:3]=="1:" or time[1:3]=="2:" or time[1:3]=="3:" or time[1:3]=="4:" or time[1:3]=="5:")):
   time = str(int(time[1:2]) + 12)
   tp = t[-4:]
   time = time + ":" + tp[slice(2)]
   endEmp1.append(time)
  else:
   if(time[slice(2)] ==" 9"):
    endEmp1.append(time[1:5])
   else:
    endEmp1.append(time[slice(5)]) 
 #print("emp1 ka endtime")       
 #print(endEmp1)
 
 #480 bool Emp1 ka
 for i in range(0, len(endEmp1)):
  time1 = startEmp1[i]
  time2 = endEmp1[i]
  T1 = time1.replace(':', ':').split(':')
  T2 = time2.replace(':', ':').split(':')
  minutesStrt = int(T1[0])*60 + int(T1[1]) - 540
  minutesEnd = int(T2[0])*60 + int(T2[1]) - 540
  #print(minutesStrt, minutesEnd)
  for i in range(minutesStrt, minutesEnd+1):
   Emp1Time[i] = False
 #print(Emp1Time)
 
 #emp1 ka free slot in time format from 480 ka bool  
 i=0
 while(i<len(Emp1Time)):
  if(Emp1Time[i]==True):
   if(i==0):
    strt = i
   else:
    strt = i-1
   while(i<len(Emp1Time) and Emp1Time[i]==True):
    i+=1
   end = i 
   strt += 540
   end += 540
   temp  = int(strt/60)
   if(temp>12):
    temp-=12
   strhr = str(temp)
   strmin = str(strt%60)
   
   strhr = strhr + ":"
   if(len(strmin)==1):
    strhr += "00"
   else:
    strhr += strmin  
   
   temp1 = int(end/60)
   if(temp1>12):
    temp1-=12
    
   endhr = str(temp1)
   endmin = str(end%60)
   
   endhr = endhr + ":"
   if(len(endmin)==1):
    endhr += "00"
   else:
    endhr += endmin
   
   if(strhr[slice(2)] == "9:" or strhr[slice(2)] == "10" or strhr[slice(2)] == "11"):
    strhr += "AM - "
   else:
    strhr += "PM - "
    
   if(endhr[slice(2)] == "9:" or endhr[slice(2)] == "10" or endhr[slice(2)] == "11"):
    endhr += "AM"
   else:
    endhr += "PM"  
   
   freeEmp1.append(strhr+endhr)
    
  else:
   i+=1
 
 allFreeSlots.append(freeEmp1)
 #print("emp1 ka free") 
 #print(freeEmp1) 
 #print("\n")
 
 # ------------------------------------------------Loop started----------------------------------------------------
 for index in range(1, len(allLists)): 
  freeEmp2 = [] 
  Emp2Time = [True] * 481
  startEmp2 = []
  endEmp2 = []
  temp2 = allLists[index][0]
 	
  #EmpIndex ka start
  for t in temp2:
   time = t[slice(5)]
   if(time[slice(2)]=="1:" or time[slice(2)]=="2:" or time[slice(2)]=="3:" or time[slice(2)]=="4:" or time[slice(2)]=="5:"):
    time = str(int(time[slice(1)]) + 12)
    time = time + ":" + t[slice(2,4)]
    startEmp2.append(time)
   else:
    if(time[slice(1)]=="9"):
     startEmp2.append(time[slice(4)])
    else:
     startEmp2.append(time)
  #print("emp "+ str(index+1)+" ka start")     
  #print(startEmp2)

  #EmpIndex ka end
  for t in temp2:
   time = t[-7:]
   if(time[-2:] == "PM" and (time[1:3]=="1:" or time[1:3]=="2:" or time[1:3]=="3:" or time[1:3]=="4:" or time[1:3]=="5:")):
    time = str(int(time[1:2]) + 12)
    tp = t[-4:]
    time = time + ":" + tp[slice(2)]
    endEmp2.append(time)
   else:
    if(time[slice(2)] ==" 9"):
     endEmp2.append(time[1:5])
    else:
     endEmp2.append(time[slice(5)]) 
  #print("emp " + str(index+1)+ " ka end")      
  #print(endEmp2)
 
  #EmpIndex ka 480 ka bool
  for i in range(0, len(endEmp2)):
   time1 = startEmp2[i]
   time2 = endEmp2[i]
   T1 = time1.replace(':', ':').split(':')
   T2 = time2.replace(':', ':').split(':')
   minutesStrt = int(T1[0])*60 + int(T1[1]) - 540
   minutesEnd = int(T2[0])*60 + int(T2[1]) - 540
   #print(minutesStrt, minutesEnd)
   for i in range(minutesStrt, minutesEnd+1):
    Emp2Time[i] = False  
 
  
  #print(Emp2Time) 
 
  #----------------------------empIndex ka free slot in time format from 480 ka bool-----------------------   
  i=0
  while(i<len(Emp2Time)):
   if(Emp2Time[i]==True):
    if(i==0):
     strt = i
    else:
     strt = i-1
    while(i<len(Emp2Time) and Emp2Time[i]==True):
     i+=1
    end = i 
   
    strt += 540
    end += 540
   
    temp  = int(strt/60)
    if(temp>12):
     temp-=12
    strhr = str(temp)
    strmin = str(strt%60)
   
    strhr = strhr + ":"
    if(len(strmin)==1):
     strhr += "00"
    else:
     strhr += strmin  
   
    temp1 = int(end/60)
    if(temp1>12):
     temp1-=12
    
    endhr = str(temp1)
    endmin = str(end%60)
   
    endhr = endhr + ":"
    if(len(endmin)==1):
     endhr += "00"
    else:
     endhr += endmin
   
    if(strhr[slice(2)] == "9:" or strhr[slice(2)] == "10" or strhr[slice(2)] == "11"):
     strhr += "AM - "
    else:
     strhr += "PM - "
    
    if(endhr[slice(2)] == "9:" or endhr[slice(2)] == "10" or endhr[slice(2)] == "11"):
     endhr += "AM"
    else:
     endhr += "PM"  
   
    freeEmp2.append(strhr+endhr)
    
   else:
    i+=1
 
  allFreeSlots.append(freeEmp2) 
  #print("emp "+ str(index+1)+" ka free") 
  #print(freeEmp2)
 
 
 #------------------------------dono ke 480 ka intersection----------------------------------
  i=0
  while(i<len(Emp1Time)):
   if(Emp1Time[i] == True and Emp2Time[i] == True):
    Emp12Time[i] = True
  
   else:
    Emp12Time[i] = False
  
   i+=1 
 
  Emp1Time = Emp12Time  
  #print("\n")
  
  
  
 i=0
 while(i<len(Emp12Time)):
  if(Emp12Time[i]==True):
   if(i==0):
    strt = i
   else:
    strt = i-1
   while(i<len(Emp12Time) and Emp12Time[i]==True):
    i+=1
   end = i 
   strt += 540
   end += 540
   temp  = int(strt/60)
   if(temp>12):
    temp-=12
   strhr = str(temp)
   strmin = str(strt%60)
  
   strhr = strhr + ":"
   if(len(strmin)==1):
    strhr += "00"
   else:
    strhr += strmin  
   
   temp1 = int(end/60)
   if(temp1>12):
    temp1-=12
    
   endhr = str(temp1)
   endmin = str(end%60)
   
   endhr = endhr + ":"
   if(len(endmin)==1):
    endhr += "00"
   else:
    endhr += endmin
   
   if(strhr[slice(2)] == "9:" or strhr[slice(2)] == "10" or strhr[slice(2)] == "11"):
    strhr += "AM - "
   else:
    strhr += "PM - "
    
   if(endhr[slice(2)] == "9:" or endhr[slice(2)] == "10" or endhr[slice(2)] == "11"):
    endhr += "AM"
   else:
    endhr += "PM"  
   
   freeEmp12.append(strhr+endhr)
    
  else:
   i+=1
 
 #allFreeSlots.append(freeEmp1) 
 #print("\n")
 #print("sab emp ka intersection")
 #for i in range(0, len(Emp12Time)):
  #print(i,Emp12Time[i] ) 
 #print(freeEmp12) 
 
 f = open('output3.txt', 'w')
 f.write(str("Available\n"))
 for i in range(0,len(allFreeSlots)):
  f.write(str(str(keysEmp[i])+": ")) 
  simplejson.dump(allFreeSlots[i], f)
  f.write(str("\n"))

 f.write(str("\n\nSlot: "))
 
 i=0
 hours = float(input(""))
 f.write(str(str(hours)+" hour"))
 hours = int(hours * 60) 
 
 f.write("\n")
 while(i<len(Emp12Time)):
  if(Emp12Time[i]==True):
   if(i==0):
    strt = i
   else:
    strt = i-1
   while(i<len(Emp12Time) and i-strt != hours and Emp12Time[i]==True):
    i+=1
   end = i 
   #print(strt,end)
   strt += 540
   end += 540  
   
   if(end-strt == hours):
    #print(strt, end)
    break
  else:
   i+=1
 
 if(end-strt == hours):
  temp  = int(strt/60)
  if(temp>12):
   temp-=12
  strhr = str(temp)
  strmin = str(strt%60)
   
  strhr = strhr + ":"
  if(len(strmin)==1):
   strhr += "00"
  else:
   strhr += strmin
     
  if(strhr[slice(2)] == "9:" or strhr[slice(2)] == "10" or strhr[slice(2)] == "11"):
   strhr += "AM - "
  else:
   strhr += "PM - "
 
  temp1 = int(end/60)
  if(temp1>12):
   temp1-=12
    
  endhr = str(temp1)
  endmin = str(end%60)
   
  endhr = endhr + ":"
  if(len(endmin)==1):
   endhr += "00"
  else:
   endhr += endmin
    
  if(endhr[slice(2)] == "9:" or endhr[slice(2)] == "10" or endhr[slice(2)] == "11"):
   endhr += "AM"
  else:
   endhr += "PM" 
  
  final = {tarik : [strhr+endhr]}
  simplejson.dump(final, f) 
 
 else:
  f.write(str("Not Available\n"))
 
f.close()
