'''✅ Use this one regularly — every time you update your code:
bash
Copy
Edit
git add .
git commit -m "Added new practice files"
git push
git add . → Adds all your changed files.

git commit -m "..." → Saves a checkpoint with a message.

git push → Uploads it to GitHub.

This is your daily routine.



🔁 Daily Workflow (Now Super Simple):
Anytime you add/edit code:
'''
r'''
powershell
Copy
Edit
#cd "D:\Users\peerz\hardcore python practice"
git init
git add .
git commit -m "Your message here"
git push
Done. That’s your new daily dev ritual.
'''





#so this lession is going to be about  strings and numbers and  building a calculator and madlibs game 
#basically about varaibles as well
#lets get strated
#sitly we will assign value as 
my_name =  "faizan"
print(my_name)
#now we can apply multiple rules to this one varaible _lets dive in!
print(my_name + " is a boy")
#we can make it lower  case as 
print(my_name.lower())
#now with upper case
print(my_name.upper())
#we can also see if the statements of upper case and lowercase are true
print(my_name.isupper())
#now with lower case
print(my_name.islower())
#we can make a sting upper and lower acse then check true false statements
print(my_name.upper().isupper())
#similar with lowercase
print(my_name.lower().islower())
#now we can see the lnegth of a string as using len function
print(len(my_name))
#we can grab individual letters in s string using number assigned by python as 
print(my_name[0])
#we can go viceversa as well
print(my_name.index("f"))
#we can also replace a letter or string with other as 
print(my_name.replace("f","s"))
#this was the basics and medium stuff about strings!
'''
the next topic of this lesson1 is dealing with numbers 
'''
# so we dont use quotes while dealing with numbers 
#python mostly goes smooth with numbers as in terms of addition,subtraction,multiplication and division
print(5+2)
#similar is the case with sub and mult and dvivision as well!
#we can also use brackets to make sure the order of operations is correct
print(5+7*2)
print((5+7)*2)
#we can also use the power of a number as 
print(5**2)
#power is taken as double ** or we can just go with the function as pow
print(pow(2,3))
# if we add a % we will get remainder of a number
print(12 % 5)
#we can also use the floor division to get the whole number as 
print(12 // 5)
#now in numbers lets deal with different function as
my_num = 3
print(my_num)
#we can convert a number to string as
print(str(my_num))
#we add add our data or info as well
print(str(my_num) +" is less than 5")
#inorder to add more data to this we need to surely make it a string before adding otherwise it will throw an error!
#lets look at another funtion
great_number = -17.5
print(abs(great_number))
#so what it does it return to the absolute number of the value!
#if we want to know which number is max or min we can go with the follwoing functions as
print(max(5,-1))
#or min
print(min(-1,-8))
#we can also round of a number
print(round(7.589))
''' so in python there are surely inbuilt funtions but those function which arent inbuilt we can call them as import
speaking of importing some advanced functions in python 

'''
from math import *
# we will import func floor and ceil
print(floor(8.9))
#it brings the smallest number as 3
print(ceil(4.3))
#we can return square root as well
print(sqrt(625))

#lets get to the most impt topic of getting input from the user as
input("enter your bad luck month:")
# here we can assign a varaible as
bad_luck = input("enter your bad luck month:")
print( bad_luck + " i wish u gudluck")
getting_info1 = input("enter ur mums name")
getting_info2 = input("enter ur dads name")
print(getting_info1 + " is married to " +  getting_info2)

#now in this lesson we will proceed with buikding a basic calculator as well a as  a basic game

number1 = input("ur lucky number one")
number2 = input("ur lucky number two")
result= int(number1)+int(number2)
print(result)
# now the int function only deals with whole number not decimals to make it do so we use the function float instead of int
#lets create a basic madlibs game
#lets for ease create 4 varaibles of a poem twinkle twinkle little star
var1 = input("enter a star name")
var2 = input("enter what u are")
var3= input("world name")
var4 = input("sky name")
print("twinkle twinkle" + var1)
print("how i wonder" + var2)
print("up above the " + var3)
print("like a diamond" + var4)
