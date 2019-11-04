string1 = "Hello DarsH"

print ("String is ",string1)

#Printing it in reverse
#print ("Revere print "+string1[-1])


#String Slicing
print ("String Slicing "+string1[3:5])

#capitalize() method converts the first character of a string to capital (uppercase) letter
print("Capitalise method "+string1.capitalize())


#The casefold() method returns a string where all the characters are lower case.
#This method is similar to the lower() method,
#but the casefold() method is stronger, more aggressive, meaning that
#it will convert more characters into lower case, and will find more matches
#when comparing two strings and both are converted using the casefold() method.

print("Capitalise method "+string1.casefold())



#The center() method will center align the string,
#using a specified character (space is default) as the fill character.
print("Center method "+string1.center(20,"*"))


#The count() method returns
#the number of times a specified value appears in the string.
#Note: This method is case sensitive.
print("Count method ",string1.count("H"))

#In today’s world, security holds the key in many of the applications.
#Thus the need for secure storage of passwords in database is required and
#hence there is to save encoded versions of strings.
#Python in its language has defined “encode()” that encodes strings with the specified encoded scheme.
#There are several encoded schemes defined in the language.
print("Encode method ",string1.encode())


#The endswith() method returns True if the string ends with the specified value, otherwise False.
print("Endswith method ",string1.endswith("H"))


#Sometimes, there is a need of specifying the space in the string, but amount of space to be left is uncertain and depending upon the environment and conditions.
#For these cases, need to modify the string again and again is a tedious task
print("Expand tabs method",string1.expandtabs(2))


#Searches the string for a specified value and returns the position of where it was found
 
print ("Substring 'for ' found at index:", string1.find('sH')) 



