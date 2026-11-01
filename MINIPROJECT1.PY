Name = input("Enter the name :")
Salary = float(input("Enter the monthly salary :"))
Food_expense = float(input ("Food expense :"))
Travel_expense = float(input ("Travel expenses :"))
Study_material = float(input ("Study material :"))
Mobile_expense = float(input ("Mobile / internet expenses :"))
Other_expense = float(input (" Other expenses :"))




print("=======MONTHLY BUDGET REPORT=======")




print("Name is :",Name)
print("Salary is :",Salary)
print("Food expense is :",Food_expense)
print("Travel expense :",Travel_expense)
print("Study materal is :",Study_material)
print("Mobile expense is :",Mobile_expense)
print ("Other expense is :",Other_expense)





Total_expense =  Food_expense + Travel_expense + Study_material + Mobile_expense + Other_expense
print("Total expense :",Total_expense)
remaining_balance = Salary - Total_expense
print("Remainag balance :",remaining_balance)

Saving  = remaining_balance / Salary *100
print("Savings rate :",Saving) 



