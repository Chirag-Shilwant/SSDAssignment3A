import string
import sys

answer = []
year = None
month = None
day = None
formatDiya = False
days = []
mo = []
yr = []

inputStr = None

monthDays = {
  1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

monthMap = {
  "Jan": 1, "jan": 1, "Feb": 2, "feb": 2, "Mar": 3, "mar": 3, "Apr": 4, "apr": 4, "May": 5, "may": 5, "Jun": 6, "jun": 6, "Jul": 7, "jul": 7, "Aug": 8, "aug": 8,
  "Sep": 9, "Sep": 9, "Oct": 10, "oct": 10, "Nov": 11, "nov": 11, "Dec": 12, "dec": 12
}


def takeInput(formatDiya):
 n = len(sys.argv)
 inputStr = None
 if(n > 1):
  inputStr = str(sys.argv[1][0])
  formatDiya = True
 return inputStr,formatDiya 
 
def writeOutput(finalAns):
 file1 = open('output.txt', 'w')
 file1.write("Date Difference: ")
 file1.write(str(finalAns))
 if(finalAns == 1):
  file1.write(" Day")
 else:
  file1.write(" Days") 

 file1.close()   

def calculateKar(inputStr, formatDiya):
 if(inputStr == "d" or inputStr == "D" or formatDiya == False):
  getDays(days[0], mo[0], yr[0])
  getDays(days[1], mo[1], yr[1])

 else:
  getDays(mo[0], days[0], yr[0])
  getDays( mo[1], days[1], yr[1])
  
def getDays(d, m, y):
 year = y
 month = m
 day = d
 n1 = 0	
 n1 = day + (year*365)
 
 for i in range(1, month):
  n1 = n1 + monthDays[i] 
 
 if (month < 3): 
  year = year - 1
 	
 n1 = n1 + int(year / 4) + int(year / 400)  - int(year / 100) 
 answer.append(n1)    

def mainTask(inputStr, formatDiya):
 file1 = open('date_calculator.txt', 'r') 
 count = 0

 for line in file1: 
  count += 1
  dateStr1 = str(line.strip())
  dateStr = dateStr1[7:]
  
  d = int(dateStr[slice(2)])
  y = int(dateStr[-4:])
  days.append(d)
  yr.append(y)
  len1 = len(dateStr)
 
  if(len1 - 8 == 2):
   m = int(dateStr[3:5]) 
 
  elif(len1 - 8 == 1):   
   m = int(dateStr[3]) 
 
  else:
   splitList = dateStr.split( )
   monthStr = splitList[1]
   m = monthMap[monthStr[slice(3)]]
 
  mo.append(m)
 
 file1.close()

 calculateKar(inputStr,formatDiya) 

 finalAns = abs(answer[1] - answer[0]);
 writeOutput(finalAns)

if __name__=="__main__": 
 inputStr,formatDiya = takeInput(formatDiya)
 mainTask(inputStr, formatDiya)
