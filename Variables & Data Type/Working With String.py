#String are basically just plan text. Any text that we want to have inside of our program we can store inside string.

#Example1
print("Example 1")
print("Python Is Awosem \n most well known programming languages") #(/n):insert a new line into the string

#Example2
print("Example 2")
pharse = "Learn Python" #(Variable_name-pharse) & (type-String)
print(pharse)

#Example3 
print("Concatenation")
phrase = "Learn python"
print(phrase + "is cool") #+ can add another string. Basically appending another string onto another one, they call that Concatenation.

#Example4
#Function perform a specific operation for us. Modify string and get information about our string.
print("Function")
phrase = "python is awosome"
print(phrase.lower())
print(phrase.upper()) #convert string in upper case 
print(len(phrase)) #lenth of the string
print(phrase[0]) #print first value of the string
#index function 
print(phrase.index("i"))
print(phrase.replace("awosome", "is a programming languages"))