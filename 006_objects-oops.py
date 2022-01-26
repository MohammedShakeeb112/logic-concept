# Objects and Oops

studentDetails = [
	{
		'roll': "1",
		'name': "Rohan Singh",
		'maths': 86,
		'science': 90,
		'english': 75,
		'computer': 85
	},
	{
		'roll': "2",
		'name': "Ritvik Patel",
		'maths': 27,
		'science': 30,
		'english': 35,
		'computer': 30
	},
	{
		'roll': "3",
		'name': "Neha Maurya",
		'maths': 75,
		'science': 69,
		'english': 40,
		'computer': 75
	},
	{
		'roll': "4",
		'name': "Mohit Verma",
		'maths': 21,
		'science': 31,
		'english': 45,
		'computer': 40
	},
	{
		'roll': "5",
		'name': "Karan Trivedi",
		'maths': 70,
		'science': 80,
		'english': 35,
		'computer': 60
	}
]
dic = {}
for i in studentDetails:
    dic[i['name']] = i['maths']+i['science']+i['english']+i['computer']
# Print the name and total marks of each student.
# for i in dic.items():
#     print(i[0],'got scored', i[1])
# Print the name of student whose total marks is highest.
maxMarks = sorted(dic, key=dic.__getitem__, reverse=True)[0]
# print(maxMarks)
# Print the name of student whose total marks is lowest.
minMarks = sorted(dic, key=dic.__getitem__)[0]
# print(minMarks)
# Print the average marks of the class in computer subject
totalcomputermarks = []
for i in studentDetails:
    totalcomputermarks.append(i['computer'])
avgMarksComputer = sum(totalcomputermarks)/len(totalcomputermarks) 
# print(avgMarksComputer)

# Print the grades of all students:
# Grade A if total marks is higher than or equal to 75%,
# Grade B if higher than or equal to 60%,
# Grade C if higher than or equal to 35%,
# Grade D if lower than 35%.

# for i in dic.items():
#     # print(i[0], i[1]/4)
#     dic[i[0]] /= 4    
#     if dic[i[0]] >= 75:
#         print('Grade A')
#     elif dic[i[0]] >= 60 and dic[i[0]] < 75:
#         print('Grade B')
#     elif dic[i[0]] >= 35 and dic[i[0]] < 60:
#         print('Grade C')  
#     else:
#         print('Grade D')  
# # Print the total number of students passed and their names. Pass when total marks is greater than 35%.
#     if dic[i[0]] >= 35:
#         print('Passed Students',i[0])
# print(dic)

# Salary calculation using OOPS concept.
#     Create a Class using ES6 in JavaScript named Employee and assign necessary
#     data members and methods such as name, id, basic salary, HRA, Allowances; define getSalary method which will return the net salary.
#     Create two Instances of Employee with all necessary details.
#     Call the getSalary method of each instance and return the net salary based on your computation.
class Employee:
    def __init__(self, name, id, basic_salary, hra, allowances):
        self.name = name
        self.id = id
        self.basic_salary = basic_salary
        self.hra = hra
        self.allowances = allowances

    def get_salary(self):
        return self.basic_salary+self.hra+self.allowances

emp1 = Employee('Rohan', 125, 30000, 15, 2000)
emp2 = Employee('Marriet', 124, 62000, 42, 3500)
# print(emp1.get_salary())
# print(emp2.get_salary())

# Bank Account (Object Oriented Programming in JavaScript)
#     Create a class and define data members such as name, bank account number,
#     account balance, account type, ifsc and name it as BankAccount.
#     Create three Instances(three customers) of BankAccount with all necessary details.
#     Print the name of customers and their account balances.
#     Calculate the average account balance from all the instances.
class Bank:
    def __init__(self, bn, ac, accBal, accType, ifsc, benificiary_name):
        self.bank_name = bn
        self.account_num = ac
        self.account_bal = accBal
        self.account_type = accType
        self.ifsc = ifsc
        self.benificiary_name = benificiary_name
        self.average = []

    def get_details(self):
        return self.benificiary_name + ' ' + self.account_bal
    
    def add_emp(self, ben):
        self.average.append(ben.account_bal)

    def get_average(self):
        return sum(self.average)/len(self.average)

ben1 = Bank('HDFC', 20041658723, 80000, 'Salary', 'HDFCIN2021', 'Rohan Shetty')
ben2 = Bank('ICICI', 20041658649, 62900, 'Salary', 'ICICIIN2021', 'Karl Michael')

# Bank.add_emp(ben1)
# Bank.add_emp(ben2)

# Given an array of objects of items in cart, print:
#     the total No. of items
#     the total cart value
#     the total discounted value(sum of dicounted values on each item) based on the given discount
#     total tax amount (18% tax, calculated on total cart value)
cartItems = [
	{
		'id': 101,
		'name': "Oreo",
		'count': 2,
		'price': 30.0,
		'discount': 0.18
	},
	{
		'id': 102,
		'name': "Red Bull",
		'count': 1,
		'price': 99.0,
		'discount': 0.15
	},
	{
		'id': 103,
		'name': "Dairy Milk Silk",
		'count': 3,
		'price': 175.0,
		'discount': 0.05
	},
	{
		'id': 104,
		'name': "Pulse Candy Pack",
		'count': 1,
		'price': 135.0,
		'discount': 0.2
	}
]
print(len(cartItems))
totalCartvalue = 0
totalDiscount = 0
for i in cartItems:
    totalCartvalue += i['price']
    totalDiscount += i['discount']
print(totalCartvalue)
print(totalDiscount)
totalTaxAmount = totalCartvalue *18/100
print(totalTaxAmount)