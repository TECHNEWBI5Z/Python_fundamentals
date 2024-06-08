# ----------------------------------------------------------------------------
# Basics on inputs and type casting
# ----------------------------------------------------------------------------

# 1. Write a Program to input 2 numbers & print their sum
# Num_1 = int(input("youtr first number is: "))
# Num_2 = int(input("youtr secound number is: "))
# print(f"Total sum of your numbers are: {(Num_1 + Num_2 )}.")

# ----------------------------------------------------------------------------

# 2. WAP to input side of a square & print its area
# Side_A = int(input("what is the meassure of side A (in CM): "))
# print(f"the square area (CM2)= {Side_A**2} ")

# ----------------------------------------------------------------------------

# 3. WAP to input 2 floating point numbers & print their average.
# float_1 = float(input(" whats your first float num: "))
# float_2 = float(input(" whats your first float num: "))
# print(f"total mean value of given numbers are : {(float_1+float_2)/2}")

# ----------------------------------------------------------------------------

# 4. WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False
# a = int(input(" what is your 'a' number: "))
# b = int(input(" what is your 'b' number: "))
# print (f"if a >= b: '{a>=b}' or a < b: '{a < b}'")

# ----------------------------------------------------------------------------
#  Basic programmes on IF CONDITION problem
# ----------------------------------------------------------------------------

# 1. WAP to check if a number entered by the user is odd or even.
# Num = int(input("what is your number: "))
# if (Num % 2 == 0):
#     print(f"your given number {Num} is a even number")
# else:
#     print(f"your given number {Num} is a odd number")

# ----------------------------------------------------------------------------

# 2. WAP to find the greatest of 3 numbers entered by the user
# Num_1 = int(input("youtr first number is: "))
# Num_2 = int(input("youtr secound number is: "))
# Num_3 = int(input("youtr secound number is: "))

# if Num_1>=Num_2:
#     print(f"The number {Num_1} is greater")
# if Num_1>=Num_3:
#     print(f"The number {Num_1} is greater")
# if Num_2>=Num_3:
#     print(f"The number {Num_2} is greater")
# else:
#     print(f"The number {Num_3} is greater")

# or - else 

# if Num_1 >= Num_2 and Num_1 >= Num_3:
#     greatest = Num_1
# elif Num_2 >= Num_1 and Num_2 >= Num_3:
#     greatest = Num_2
# else:
#     greatest = Num_3

# print(f"The greatest number is {greatest}")

# ----------------------------------------------------------------------------

# 3. WAP to check if a number is a multiple of 7 or not
# Num = int(input("what is your number: "))
# if (Num % 7 == 0):
#     print(f"the given number {Num} 'is mutiple' of 7")
# else:
#     print(f"the given number {Num} 'is not mutiple' of 7")

# OR - ELSE

# ternery methods
# Num = int(input("what is your number: "))
# yes = (f"the given number {Num} 'is mutiple' of 7") if (Num % 7 == 0) else "the given number {Num} 'is not mutiple' of 7"
# print(yes)

# ----------------------------------------------------------------------------
# 4. WAP to check if a age is >= 18 he/she can vote 

# ternery methods
# age = int(input("what's your age is : "))
# vote =("yes", "no") [age < 18]
# print(vote)

# --OR ELSE 

# ternery method
# age = int(input("what's your age is : "))
# yes = f"yes you can vote" if age > 18 or age == 18 else f"no you cant vote your age lesser 18 i.e {age}"
# print(yes)
 
# ----------------------------------------------------------------------------

# 5. WAP to check calulate taxable amount for your salary 
# ternery method
# salary = int(input("your gross salary is about : "))
# taxable_amount = salary*(.1, .2) [salary >= 50000] # in list mention your else condiition and in tuple 1st is 'if' and 2nd is 'else'
# print (taxable_amount) 

# ----------------------------------------------------------------------------
# LISTS and TUPLE (Tuples are immutable we store the any kind of datatype but we can't modify it by using index as it is in LISTS)
# ----------------------------------------------------------------------------

# 1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# Movie_list = []
# Movie_list.append(input("Your favorite movie 1 is: "))
# Movie_list.append(input("Your favorite movie 2 is: "))
# Movie_list.append(input("Your favorite movie 3 is: "))

# print(Movie_list)

#  or 

# Movie_1 = (input("Your favorite movie 1 is: "))
# Movie_2 = (input("Your favorite movie 2 is: "))
# Movie_3 = (input("Your favorite movie 3 is: "))
# Movies_list = [Movie_1, Movie_2, Movie_3]
# print(Movies_list)

# ----------------------------------------------------------------------------

# 2. WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

# List = [1, 2, 3, 5, 3, 2, 1]
# list_copy = List.copy()

# if (List == list_copy): 
#     print(f"the given List {List} 'is palindromic' in nature")
# else:
#     print(f"the given List {List} 'is not palindromic' in nature")

# OR - ELSE 

# your_list = []
# for items in range(6):
#     List = input("add item into list: ")
#     your_list.append(List)

# List_copy = your_list.copy()

# if (your_list == List_copy):
#     print(f"the given List {your_list} 'is palindromic' in nature")
# else:
#     print(f"the given List {your_list} 'is not palindromic' in nature")

# ----------------------------------------------------------------------------

#  3. WAP to count the number of students with the “A” grade in the following tuple.
# [”C”,“D”,“A”,“A”,“B”,“B”,“A”]

# List = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
# results = List.count('A')
# print(f"letter 'A' has {results} times repeated")

# ----------------------------------------------------------------------------

# Store the above values in a list & sort them from “A” to “D”
# Array = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
# your_lsit= []
# for items in Array:
#     your_lsit.append(items)

# print(f"your actual list is {your_lsit}")
# your_lsit.sort()

# print(f"your actual sorted list is {your_lsit}")

 # ----------------------------------------------------------------------------
# DICTIONARIES AND SETS
 # ----------------------------------------------------------------------------

# 1. Store following word meanings in a python dictionary :
# your_dict = {}
# your_dict["table"]=["a piece of furniture","list of facts & figures"]
# your_dict["cat"]= "a small animal" 
# print(your_dict)

# ----------------------------------------------------------------------------

# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# 'python', 'java', 'C++', 'python', 'javascript', 'java', 'python', 'java', 'C++', 'C'

# LIST = ['python', 'java', 'C++', 'python', 'javascript', 'java', 'python', 'java', 'C++', 'C']
# your_list = []

# for item in LIST:
#     if item not in your_list:
#         your_list.append(item)

# print(f"total number of classes required for all students are: {len(your_list)}")

# ----OR -ELSE --
# DICTIONARY_LIST = ['python', 'java', 'C++', 'python', 'javascript', 'java', 'python', 'java', 'C++', 'C']

# DICT_set = set(DICTIONARY_LIST)
# TOTAL_CLASSES_NEEDED = len(DICT_set)
# print(f"Total number classes needed based on subjects are =", TOTAL_CLASSES_NEEDED)

# ----------------------------------------------------------------------------

# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value

# total_score_dict  = {}
# subject = " "

# for sub_score in range(3):
#     subject = input("your subject name : ")
#     score = int(input("your X subject score is: "))
#     total_score_dict[subject] = score

# print (total_score_dict)

# ----------------------------------------------------------------------------

# 4. Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
# assume 
# set_1 = {9, 9.0, 8.5}
# print(set_1)

# ---OR ELSE 

# unique_values = set()

# unique_values.add((9, type(9)))
# unique_values.add((9.0, type(9.0)))

# print(unique_values)

# ----OR- ELSE 

# set_2 = {9, '9.0', 8.5}
# print(set_2)

#  ---OR ELSE 
# set_3 = {9, 8.5}
# set_3.add(type(9.0))
# print(set_3)

# ----------------------------------------------------------------------------
# WHILEL LOOPS
# ----------------------------------------------------------------------------

# 1. Print numbers from 1 to 100.
# num = 1
# while num <=100:
#     print(num)
#     num +=1

# ----------------------------------------------------------------------------

# 2. Print numbers from 100 to 1.
# num = 100
# while num >= 1:
#     print(num)
#     num -=1

# ----------------------------------------------------------------------------

# 3. Print the multiplication table of a number n.
# Num = int(input("what number multiples you want : "))
# i = 1
# while i<=10:
#     tab = f"{i} * {Num} = {i * Num}"
#     print(tab)
#     i +=1

# ----------------------------------------------------------------------------

# 4. Print the elements of the following list using a loop
# List = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx = 0
# while idx < len(List):
#     print(List[idx])
#     idx +=1

# ----------------------------------------------------------------------------

# 5. Search for a number x in this tuple using loop:
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = int(input("whats ia your num : "))
# idx = 0
# while idx < len(tuple):
#     print(tuple[idx])
#     if num == tuple[idx]:
#         print("you got your results")
#     else:
#         print("sorry no resluts found")
#     idx +=1

# --OR ELSE

# NUMBER_TUP = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = int(input("whats ia your num : "))
# idx = 0
# FOUND = False
# while idx < len(NUMBER_TUP):
#     print(f"tuple index is: '{idx}', and the tuple value is : '{NUMBER_TUP[idx]}'")
#     if num == NUMBER_TUP[idx]:
#         print("you got your results")
#         FOUND = True
#         break
#     else:
#         print("sorry no resluts found")
#     idx +=1

# ----------------------------------------------------------------------------

# 6 .WAP to find the sum of first n numbers. (using while)

# Num = int(input("what is yout n natural number: "))
# start = 0
# total_sum = 0
# while start <= Num:
#     total_sum = total_sum+start
#     start +=1
# print(total_sum)

# ----------------------------------------------------------------------------

# 7. WAP to find the factorial of first n numbers. (using while)

# Num = 5
# start = 1
# factorial = 1
# while start <= Num:
#     factorial = factorial * start
#     start +=1
# print(factorial)

# ----------------------------------------------------------------------------
# FOR LOOP
# ----------------------------------------------------------------------------

# 1. Print the elements of the following list using a loop:
# NUMBER_LIST = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for num in NUMBER_LIST:
#     print(num)

# ----------------------------------------------------------------------------

#  2.Search for a number x in this tuple using loop:
# NUMBER_LIST = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# IDX = 0
# your_num = 81
# for num in NUMBER_LIST:
#     if your_num == num:
#         IDX += 1
#         print (f" your got your number is at {IDX} which is {your_num} ")
#     IDX += 1    

# ----------------------------------------------------------------------------

# 3. WAP to find the factorial of first n numbers. (using for)

# Num = 5
# factorial = 1
# for i in range(1, Num+1):
#     factorial *= i
# print(factorial)

# ----------------------------------------------------------------------------

# 4 .WAP to find the sum of first n numbers. (using while)
# Num = 5
# sum_total = 0
# for i in range(0, Num+1):
#     sum_total +=i
# print(sum_total)

# ----------------------------------------------------------------------------

# 5. Print numbers from 1 to 100.
# for i in range (1, 100+1):
#     print(i)
    
# ----------------------------------------------------------------------------

# 6. Print numbers from 100 to 1.
# for i in range(100, 0, -1):
#     print(i)

# ----------------------------------------------------------------------------

# 7. Print the multiplication table of a number n.
# NUM=5
# for i in range (1, 10+1):
#     table = i*NUM
#     print(table)    

# ----------------------------------------------------------------------------
#DIFINING FUNCTIONS AND CALLING FUUNCTION
# ----------------------------------------------------------------------------

# 1. WAF to print the length of a list. (list is the parameter)
# def print_list(list):
#     for i in list:
#         print(i)

# my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print_list(my_list)

# ----------------------------------------------------------------------------

# 2. WAF to print the elements of a list in a single line. (list is the parameter)

# def print_list(list):
#     store = ' '
#     for i in list:
#         store += str(i)+ ' '
#     print(store.strip()) 
# my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print_list(my_list)       
        
# ----------------------------------------------------------------------------

# 3. WAF to find the factorial of n. (n is the parameter)
# def facto(Num):
#     factorial = 1
#     for i in range(1, Num+1):
#         factorial = factorial * i
#     print(factorial)

# your_Num = int(input("whats your number "))
# facto(your_Num)

# ----------------------------------------------------------------------------

# 4. WAF to convert USD to INR.
# def convertor(USD):
#     print (f"the {USD} is equal to {USD * 82} rupees")
# USD = int(input("how much USD you want to convert int INR : "))
# convertor(USD)

# ----------------------------------------------------------------------------
# RECURSSION
# ----------------------------------------------------------------------------
# 1. WAR to print 100 to 1
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(100)

# ----------------------------------------------------------------------------

# 2. WAR to print 1 to 100
# def show(n):
#     if (n == 101):
#         return
#     print(n)
#     show(n+1)

# show(1)

# ----------------------------------------------------------------------------

# 3. Write a recursive function to calculate the sum of first n natural numbers.

# def sum(n):
#     if (n == 0):
#         return 0
#     else:
#         return n + sum(n-1)

# num = sum(10)
# print(num)

# ----------------------------------------------------------------------------

# 4. Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

# def print_list(list, idx =0):
#     if idx < len(list):
#         print (list[idx])
#         print_list (list, idx +1)

# my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print_list(my_list)

# ----------------------------------------------------------------------------
# ---FILE I/O
# ----------------------------------------------------------------------------
# before operating create a new file naming "  "

# 1. read file on line 1.
# f = open("sample.txt", "r")
# read_line = f.readline(2)
# print(read_line)
# f.close()

# ----------------------------------------------------------------------------

# 2. append text on file.
# f = open("sample.txt", "a+")
# write = f.write("\n the is me once again")

# ----------------------------------------------------------------------------

# 3. delete file.
# import os
# os.remove("sample.txt")

# ----------------------------------------------------------------------------

# 4. find word in file

# def check_for_word(word):
#     with open("sample.txt", "r") as f:
#         data = f.read()
#     if data.find(word) != -1:
#         print("yes")
#     else:
#         print("not found")

# check_for_word("python")

# ----------------------------------------------------------------------------

#  5. check word in which line number

# def check_for_line():
#     word = "bigginer"
#     data = True
#     line_no = 1
#     with open("sample.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()

# ----------------------------------------------------------------------------

# write as function align your coma seperated num into column
# overwrite your file with 123,456,789,101112,131415,
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
#     num =" "
#     for i in range(len(data)):
#         if (data[i]== ","):
#             print(int(num))
#             num =""
#         else:
#             num += data[i]
# print(type(num))

# ----------------------------------------------------------------------------
# CLASSES AND OBJECTS
# ----------------------------------------------------------------------------
# 1. Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

# class Student:
#     @staticmethod
#     def hello():
#         print("hello")

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for x in self.marks:
#             sum += x
#         print(f"Your total average score is {sum / len(self.marks)}")

# s1 = Student("faizan", [45, 56, 39])
# s1.get_avg()

# ----------------------------------------------------------------------------

# 2. Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

# class Account:
#     def __init__(self, balance, account_num):
#         self.balance = balance
#         self.account_num = account_num

#     def credit(self, amount):
#         self.balance = self.balance + amount
#         print(f"the total amount credit: {amount}")
#         print(f"your total balance is around {self.balance}")
    
#     def debit(self, amount):
#         self.balance = self.balance - amount
#         print(f"the total amount debit: {amount}")
#         print(f"your total balance is around {self.balance}")
    
#     def get_balance(self):
#         return self.balance
    

# acc1 = Account(10000, 8660602668)
# acc1.debit(1000)
# acc1.credit(10000)
# acc1.credit(59000)
# acc1.get_balance()

# ----------------------------------------------------------------------------
# @staticmethod - it is a type of decorator in which "a method which doesn't use any of parameters and 
# we can call directly ny using the class name instead of object name"
# because this method will be common for objects.
# ----------------------------------------------------------------------------

# WAP to show the use case of @staticmethod decorator

# class Student:
#     @staticmethod
#     def hello():
#         print("Hello dear student")

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for x in self.marks:
#             sum += x
#         print(f"Your total average score is {round(sum / len(self.marks))}")

#     @staticmethod
#     def greet():
#         print("Congratualations on your success....!")

# Student.hello()
# s1 = Student("faizan", [45, 56, 39])
# s1.get_avg()
# Student.greet()

# ----------------------------------------------------------------------------

#  del - DELETEING THE OBJECT BY DEL FUNCTION

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1= Student("faizan")
# print(s1.name)

# del s1
# print(s1)

# ----------------------------------------------------------------------------
# private attributes and methods- in which attributes and methods can't accessed directly insetead of 
# the can be accessed indirectly through some other 
# and the name of variable or method starts with double underscore in the begining  ex: __acc_pass
# ----------------------------------------------------------------------------

# class Account:
#     def __init__(self, acc_num, acc_pass):
#         self.acc_num = acc_num
#         self.__acc_pass = acc_pass

#     def reset_pass(self, new_pass):
#         self.__acc_pass = new_pass
#         return "Password reset successfully"

#     def get_pass(self):
#         return self.__acc_pass


# acc1 = Account("12345", "abcde")
# # Correct way to access the private variable through a method
# print(acc1.acc_num, acc1.get_pass())

# # # Resetting the password
# print(acc1.reset_pass("newpass123"))
# print(acc1.get_pass())

# ----------------------------------------------------------------------------
#  FOUR PILLERS OF OOPs
# ----------------------------------------------------------------------------

# 1. Encapsulation
# Definition: Encapsulation is the mechanism of restricting access to some of an object's components and 
# protecting the internal state of the object from unintended interference and misuse. 
# This is usually done by making some attributes private and providing public methods to access and modify them.

# class Account:
#     def __init__(self, acc_num, acc_pass):
#         self.acc_num = acc_num
#         self.__acc_pass = acc_pass  # Private attribute

#     def get_pass(self):
#         return self.__acc_pass

#     def set_pass(self, new_pass):
#         self.__acc_pass = new_pass


# acc1 = Account("12345", "abcde")
# print(acc1.acc_num)          # Accessible
# print(acc1.get_pass())       # Accessible through a method
# # print(acc1.__acc_pass)     # Not directly accessible, will raise an AttributeError

# ----------------------------------------------------------------------------

# 2. Abstraction
# Definition: Abstraction involves hiding the complex implementation details and showing only the essential features of the object.
#  This simplifies the interaction with the object and reduces complexity.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# rect = Rectangle(10, 20)
# print(f"Area: {rect.area()}")        # Only essential features exposed
# print(f"Perimeter: {rect.perimeter()}") # Implementation details hidden

# ----------------------------------------------------------------------------

# 3. Inheritance
# Definition: Inheritance is a mechanism where a new class (child class) inherits attributes and methods 
# from an existing class (parent class). This allows for code reuse and the creation of hierarchical relationships.

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")


# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"


# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())
# print(cat.speak())

#  ----------------------------------------------------------------------------

# 4. Polymorphism
# Definition: Polymorphism allows objects of different classes to be treated as objects of a common super class. 
# It is typically achieved through method overriding, where different classes implement the same method in different ways.

# class Bird:
#     def fly(self):
#         raise NotImplementedError("Subclass must implement abstract method")


# class Sparrow(Bird):
#     def fly(self):
#         return "Sparrow flies at low altitude."


# class Eagle(Bird):
#     def fly(self):
#         return "Eagle flies at high altitude."


# def make_bird_fly(bird):
#     print(bird.fly())


# sparrow = Sparrow()
# eagle = Eagle()
# make_bird_fly(sparrow)  # Output: Sparrow flies at low altitude.
# make_bird_fly(eagle)    # Output: Eagle flies at high altitude.

# ----------------------------------------------------------------------------

#  WAP TO EXHIBIT POLYMORPHISM CHARACTER OF CLASS IN YOUR LOGIC FOR COMPLEX NUMBERS

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def shownum(self):
#         print(f"{self.real} + {self.img}j")

#     # def addnum(self, num):
#     #     newreal = self.real + num.real
#     #     newimg = self.img + num.img
#     #     return Complex(newreal, newimg)
#     def __add__(self, other):
#         newreal = self.real + other.real
#         newimg = self.img + other.img
#         return Complex(newreal, newimg)

# c1 = Complex(1, 3)
# c1.shownum()
# c2 = Complex(2, 3)
# c2.shownum()

# c3 = c1 + c2
# c3.shownum()
# # num3 = c1.addnum(c2)
# # num3.shownum()


# ----------------------------------------------------------------------------

# WAP TO EXHIBIT POLYMORPHISM CHARACTER OF OOPS

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, other):
#         return self.price > other.price

# ord1 = ("chips", 200)
# ord2 = ("kara", 300)
# print (ord1<ord2)

# ----------------------------------------------------------------------------

# WAP TO EXHIBIT INHERITENCE PROPERTY OF OOPS
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetail(self):  
#         return self.role, self.department, self.salary
    
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
      
    
# emp1 = Employee("HR", "HRD", 26000)
# print(emp1.showDetail())  

# ----------------------------------------------------------------------------
# THANK YOU AND WISH YOU ALL THE BEST FOR CODING JOURNEY
# ----------------------------------------------------------------------------