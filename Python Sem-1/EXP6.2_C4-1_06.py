# Write a program to create a file employeedetails.txt" which stores the Employee details by adding their Employee Id, Name, and Department into it using the following format:
# EmpId  	Name	     Department
# 1601001          Abc          Computer
# 1601003          Xyz	     IT

with open("employeedetails.txt", "x") as f:
    f.write("EmpId  	     Name	       Department\n 1601001     Abc          Computer\n 1601003     Xyz	          IT\n")
   
