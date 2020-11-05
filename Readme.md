## Assignment 3a
**Github Repo -** https://github.com/Chirag-Shilwant/SSDAssignment3A
##### Question 1 :
**Assumptions**
1. Assumed that the input json file will form a valid n-ary tree
2. Assumed that **L0** will always be present in the input json file
3. Assuming all inputs will be in range "000" and "999" and on seperate lines 
4. Assuming that both user inputs will always be present in the json file 

**Approach**
1. Extracted the input from json file and stored it in the form of dictionary with key as name and value as a tuple with two values ([parentName, levelOfSelf]). 
2. After that took 2 input from user and then checked if they are on same level in tree. If yes then recursively travelled untill their parentName are same. If no then first brought both inputs on same level and then applied the same approach as mentioned earlier.   
3. Finally printed the common leader along with the difference in level between common leader with input1 and input2.

##### Question 2 :
**Assumptions**
1.  Assumed that the input would have date in DD format, month in MM format and year in YYYY foramt. Date/Month with single digit(x) should be represented as **0x**.
2.  Assumed dates with format as DDth Month, YYYY; DD/MM/YYYY; DD-MM-YYYY; DD.MM.YYYY; DDth Mon, YYYY

**Approach**
1. Extracted both dates from input file (i.e "date_calculator.txt")  
2. Then converted both dates in the form of **day**   
3. Finally subtracted both dates to get the final result.
4. Wrote the output in a file named **output.txt** 

##### Question 3 :
**Assumptions**
1.  Assumed single employee and single date in both Employee1.txt and Employee2.txt
2.  Assumed output file with name as **output3.txt**

**Approach**
1. Extracted the EmployeeName, Date and ListOfBusyTime from both the input files. Converted the Time in 24 hour format.
2. Then calculated Available time for both employees using a boolean list of size 481(since 9AM-5PM = 8hrs = 480 mins) where each position represents a minute slot. When a Employee is busy during a period then marked False in boolean array for that particular period. After that to get Available time for a Employee traversed the boolean list and stored all the range where the value is True.  
3. Then compared Dates of Both employees. If Date are different then wrote "No Match" in the output file.
4. Took a slot input from user in hour format.
5. If the dates are same then wrote the Available time list and input slot durationin the output file. Then traversed the boolean array of both Employees simultaneously and calculated the first free slot equal to the slot input.
6. If we found the slot we add it to the output file in the form of dictionary with key as Date and value as the first free slot. If not free slot found we write "No Match" in the output file(i.e output3.txt)

