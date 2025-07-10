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

powershell
Copy
Edit
cd "D:\Users\peerz\hardcore python practice"
git init
git add .
git commit -m "Your message here"
git push
Done. That’s your new daily dev ritual.





git add .
git commit -m "Initial commit with W3Schools code"
git branch -M main
git push -u origin main
This longer version is used only ONCE when:

You're pushing the code to GitHub for the first time

You just created a new repo

Your folder is not yet connected to GitHub
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
