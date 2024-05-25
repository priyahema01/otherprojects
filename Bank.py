print('Welcome to Bank')
acc_no = input('Enter account number :')
days = int(input('Enter number of days missed for loan repayment :'))
due_amount = 6879
print('--------Invoice-------')
print('Account number :',acc_no)
print('Days missed :',days)
print('Due missed :',due_amount)

#validate fine amt
if days == 0:
    fine_amount = due_amount*0/100
    print('Fine amount :',fine_amount)
    print('Total payable amount :',due_amount+fine_amount)
elif days>=1 and days<=5:
    fine_amount = due_amount*5/100
    print('Fine amount :',fine_amount)
    print("Total payable amount :",due_amount+fine_amount)
elif days>6 and days<10:
    fine_amount = due_amount*10/100
    print('Fine amount :',fine_amount)
    print('Total payable amount :',due_amount+fine_amount)
else:
    print('Due date passed more than 10 days contact admin!...')
print('---Thank you----')