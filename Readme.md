# Assignment 3c

**Github link for PartA -** https://github.com/Chirag-Shilwant/SSDAssignment3A/tree/main

**Github link for PartB -** https://github.com/Chirag-Shilwant/SSDAssignment3A/tree/PartB

**Github link for PartC -** https://github.com/Chirag-Shilwant/SSDAssignment3A/tree/PartC
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

**Lines Changed in PartB**
- Line 20-24 - Added a new function named equalLevel
- Line 27-34 - Added this part of code inside a function named makeTree
- Line 39-94 - Added this part of code in a function named main
- Line 94-108 - Added the print final result logic inside a new function named printResult
- Line 109 - Added the  if _ name _ == “_main_” statement to call main function

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

**Lines Changed in PartB**
- Line 4-44 - Shifted this part of code below
- Line 56-60 - Added this portion of code in a function named takeInput
- Line 61 - Defined 2 functions named writeOutput and calculateKar
- Line 82-109 - Added this portion of code in a function named mainTask
- Line 111-117 - Added this portion of code in a function named calculateKar
- Line 127-135 - Added this portion of code in a function named writeOutput

****
##### Question 3 :
**Assumptions**
1.  Assumed single employee and single date in all Employee`i`.txt files (where i=1,2...n)
2.  Assumed output file with name as **output3.txt**
3.  Assumed that all the input files (Employee1.txt, Employee2.txt, ..... ) in a directory named **Employee**. This directory must only contain input files of the above mentioned format.

**Approach**
1. Extracted the EmployeeName, Date and ListOfBusyTime from all the input files in a 2D list. Converted the Time in 24 hour format.
2. Then calculated Available time for all employees using a boolean list of size 481(since 9AM-5PM = 8hrs = 480 mins) where each position represents a minute slot. When a Employee is busy during a period then marked False in boolean array for that particular period. After that to get Available time for a Employee traversed the boolean list and stored all the range where the value is True. Repated this step for all the Employees.  
3. Then compared Dates of all employees. If Date are different then wrote "Dates Not Matching" in the output file.
4. Took a slot input from user in hour format.
5. If the dates are same then wrote the Available time list and input slot durationin the output file. Then traversed the boolean array of intersection of all Employees simultaneously and calculated the first free slot equal to the slot input.
6. If we found the slot we add it to the output file in the form of dictionary with key as Date and value as the first free slot. If not free slot found we write "No Match" in the output file(i.e output3.txt)

**Lines Changed in PartB**
- Line 36 - Defined few functions named takeInput, findSlothelp, slotMila, writeOutput and calculateFirstFreeSlot
- Line 380-382 - Added this portion of code in a function named takeInput
- Line 385-402 - Added this portion of code in a function named findSlothelp
- Line 370-384 - Added this portion of code in a function named writeOutput
- Line 404-441 - Added this portion of code in a function named slotMila
- Line 406 and 423 - Added this portion of code in a function named checkPM
- Line 403 and 443 - Added this line code in a function named calculateFirstFreeSlot
- Line 447 - Added the  if _ name _ == “_main_” statement to call writeOutput function

### Final Complexity of all 3 codes

![finalComplexity](https://user-images.githubusercontent.com/48115585/99146012-f825a300-2699-11eb-847e-15978b450e9f.png)
