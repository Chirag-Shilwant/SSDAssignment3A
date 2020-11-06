# Assignment 3a

**Note** - `In SSD part 3A, I had uploaded a zip file on Github. Hence I was not able to modify the existing .py files by creating a new branch. Hence after consulting a TA, I deleted my Old Repo of SSD part 3A and created a new repo of part 3A and used this new repo for creating a branch for PartB`.

**New Github link for PartA -** https://github.com/Chirag-Shilwant/SSDAssignment3A/tree/main
**Github link for PartB -** https://github.com/Chirag-Shilwant/SSDAssignment3A/tree/PartB
****
##### Question 1 :
**Assumptions**
1. Assumed that the input json file will form a valid n-ary tree
2. Assumed that **L0** will always be present in the input json file
3. Assuming all inputs will be in range "000" and "999" and on seperate lines 
4. Assuming that all user inputs will always be present in the json file 

**Approach**
1. Extracted the input from json file and stored it in the form of dictionary with key as name and value as a tuple with two values ([parentName, levelOfSelf]). 
2. After that took N inputs from user and calculated the lowest common ansector for each neighbouring input and stored the result of it in a list.
3. Finally printed the common leader from the list (which has the lowest level) along with the difference in level between common leader with input1 and input2.

**Lines Changed in PartA**
- Line 8 - Added few data structures and variables
- Line 9-18 - Modified the LCA to return the answer instead of printing it in the function itself
- Line 35 - Stored the input in a list instead of variables
- Line 48-74 - Modified the code to iterate it over the input list 
- After Line 78 - Added a new logic to calculate the common leader and print the desired results.

****
##### Question 2 :
**Assumptions**
1.  Assumed that the input would have date in DD format, month in MM format and year in YYYY foramt. Date/Month with single digit(x) should be represented as **0x**.
2.  Assumed dates with format as 
`DDth Month, YYYY`
`DD/MM/YYYY` 
`DD-MM-YYYY` 
`DD.MM.YYYY`
`DDth Mon, YYYY` 
`MM/DD/YYYY` 
`MM-DD-YYYY` 
`MM.DD.YYYY`
3.  Assumed that command line input will also be provided for fromats like 
    `DD/MM/YYYY; DD-MM-YYYY; DD.MM.YYYY;MM/DD/YYYY; MM-DD-YYYY; MM.DD.YYYY`

**Approach**
1. Extracted both dates from input file (i.e "date_calculator.txt")
2. Then depending on the input format called the helper function
3. Then converted both dates in the form of **day**   
4. Finally subtracted both dates to get the final result
5. Wrote the output in a file named **output.txt** 

**Lines Changed in PartA**
- Line 2 - Imported `sys` for command line input
- Line 48 - Added a boolean variable 
- Line 52 - Added the code to input command line argument
- Line 99 - Modified the function calls depending on the format of input in command line

****
##### Question 3 :
**Assumptions**
1.  Assumed single employee and single date in all Employeei.txt files (where i=1,2...n)
2.  Assumed output file with name as **output3.txt**
3.  Assumed that all the input files (Employee1.txt, Employee2.txt, ..... ) in a directory named **Employee**. This directory must only contain input files of the above mentioned format.

**Approach**
1. Extracted the EmployeeName, Date and ListOfBusyTime from all the input files in a 2D list. Converted the Time in 24 hour format.
2. Then calculated Available time for all employees using a boolean list of size 481(since 9AM-5PM = 8hrs = 480 mins) where each position represents a minute slot. When a Employee is busy during a period then marked False in boolean array for that particular period. After that to get Available time for a Employee traversed the boolean list and stored all the range where the value is True. Repated this step for all the Employees.  
3. Then compared Dates of all employees. If Date are different then wrote "Dates Not Matching" in the output file.
4. Took a slot input from user in hour format.
5. If the dates are same then wrote the Available time list and input slot durationin the output file. Then traversed the boolean array of intersection of all Employees simultaneously and calculated the first free slot equal to the slot input.
6. If we found the slot we add it to the output file in the form of dictionary with key as Date and value as the first free slot. If not free slot found we write "No Match" in the output file(i.e output3.txt)

**Lines Changed in PartA**
- Line 1 - Imported `fnmatch` and `os` for calculating the number of .txt files in Employee directory
- Line 4 - Moved the code below and iterated it over all the input files in Employee directory
- Line 24 - Added few data structures such as lists
- Line 49 - Added a function checkDates which checks similarity in all the dates from all the input files
- Line 62 - Extracted the date and busylist for each employee in the form of list and appended it to another list
- Line 70 to 126 - Modified the code to iterate it over all employees busy list and calculate the intersection of the free times for all the employees
- Line 267 - Changed the write format to print freeSlots of all Employees by iterating over the extracted input list
- Line 280 to 337 - Modifed the code to calculate first Free slot from the boolean array founded by intersection of boolean array of all employees
