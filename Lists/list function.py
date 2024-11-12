#Function in Lists: Modify the list and get information about the list.

#list
roll_numbers = [4, 8, 6, 9, 10]
friends = ["David", "Mike", "pong", "Friker"]
print(friends)

#append: add another name
lucky_numbers = [4, 8, 6, 9, 10]
friends = ["David", "Mike", "pong", "Friker"]
friends.append("Morish") #add another name in the list without changeing the list
print(friends, "add another name in the list")

#insert has two parameter
lucky_numbers = [4, 8, 6, 9, 10]
friends = ["David", "Mike", "pong", "Friker"]
friends.insert(1, "jakey") #push all the element
print(friends, "insert")

#remove
lucky_numbers = [4, 8, 6, 9, 10]
friends = ["David", "Mike", "pong", "Friker"]
friends.remove("pong") #remove element
print(friends, "remove")

#clear or empty list
friends = ["David", "Mike", "pong", "Friker"]
friends.clear() #clear all element
print(friends)

#index
friends = ["David", "Mike", "pong", "Friker"]
print(friends.index("pong")) #print the index number of pong (his index number is 2) ["0" "1" "2" "3"]

#count
friends = ["David", "Mike", "Mike", "Mike", "pong", "Friker"]
print(friends.count("Mike")) #how many times mike in the list

#sort the list in the from of A-Z
lucky_numbers = [25, 10, 999, 500, 50]
friends = ["David", "Mike", "Mike", "Mike", "pong", "Friker"]
friends.sort() #print the list in alphabetical order
lucky_numbers.sort() #print the list in ascending order
print(friends) 
print(lucky_numbers)

#reverse
lucky_numbers = [25, 10, 999, 500, 50]
lucky_numbers.reverse() #reverse the list and start from 50,25, 10, 999, 500, 50
print(lucky_numbers)

#copy
lucky_numbers = [25, 10, 999, 500, 50]
friends = ["David", "Mike", "pong", "Friker"]
friends2 = friends.copy()
print(friends2)

#add two list together
lucky_numbers = [25, 10, 999, 500, 50]
friends = ["David", "Mike", "pong", "Friker"]
friends.extend(lucky_numbers)
print(friends, "add two list")


#THIS IS THE BASIC OVERVIEW OF THE LISTS FUNCTION.