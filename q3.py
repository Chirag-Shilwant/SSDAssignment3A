import ast
import simplejson

file = open("Employee1.txt", "r")
content1 = file.read()
dictionary1 = ast.literal_eval(content1)
value1 = dictionary1.values()
keyy1 = dictionary1.keys()
file.close()

file = open("Employee2.txt", "r")
content2 = file.read()
dictionary2 = ast.literal_eval(content2)
value2 = dictionary2.values()
keyy2 = dictionary2.keys()
file.close()


Emp1 = []
Emp2 = []

keysEmp = []
startEmp1 = []
startEmp2 = []
endEmp1 = []
endEmp2 = []

freeEmp1 = []
freeEmp2 = []

Emp1Time = [True] * 481
Emp2Time = [True] * 481

tarik = None

for v in value1:
 key1 = v.keys()
 val1 = v.values()

for k in keyy1:
 keysEmp.append(k)
 
for v in val1:
 Emp1.append(v)
  
for k in key1:
 Emp1.append(k)

#print(Emp1)

for v in value2:
 key2 = v.keys()
 val2 = v.values()

for k in keyy2:
 keysEmp.append(k)
 
for v in val2:
 Emp2.append(v)
  
for k in key2:
 Emp2.append(k)

#print(Emp2)


if(Emp1[1] == Emp2[1]):
 tarik = Emp1[1]
 temp1 = Emp1[0]
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
 #print(startEmp1)
 
 
 temp2 = Emp2[0]
 for t in temp2:
  time = t[slice(5)]
  if(time[slice(2)]=="1:" or time[slice(2)]=="2:" or time[slice(2)]=="3:" or time[slice(2)]=="4:" or time[slice(2)]=="5:"):
   time = str(int(time[slice(1)]) + 12)
   time = time + ":" + t[slice(2,4)]
   startEmp2.append(time)
  else:
   startEmp2.append(time)    
 #print(startEmp2)
 
 
 temp3 = Emp1[0]
 for t in temp3:
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
 #print(endEmp1)
 
 
 temp4 = Emp2[0]
 for t in temp4:
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
 #print(endEmp2)

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
 #print("\n")
 
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
 
 #print("\n")
 #print(Emp2Time)
  
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
   
 #print("\n")
 
 
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
 #print(freeEmp1)
 #print(freeEmp2)
 
 f = open('output3.txt', 'w')
 f.write(str("Available\n"))
 f.write(str(str(keysEmp[0])+": "))
 simplejson.dump(freeEmp1, f)
 f.write(str("\n"))
 f.write(str(str(keysEmp[1])+": "))
 simplejson.dump(freeEmp2, f)
 f.write(str("\n\nSlot: "))
 
 i=0
 hours = float(input(""))
 f.write(str(str(hours)+" hour"))
 hours = int(hours * 60) 
 
 f.write("\n")
 while(i<len(Emp2Time)):
  if(Emp2Time[i]==True and Emp1Time[i]==True):
   if(i==0):
    strt = i
   else:
    strt = i-1
   while(i<len(Emp2Time) and i-strt != hours and Emp1Time[i]==True and Emp2Time[i]==True):
    i+=1
   end = i 
   
   strt += 540
   end += 540  
   
   if(end-strt == hours):
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
 
    
else:
 f = open('output3.txt', 'w')
 f.write("No Match")
 f.close()
