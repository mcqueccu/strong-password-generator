import math
import random

#Main Character List
charactersUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charactersLower = "abcdefghijklmnopqrstuvwxyz"
charactersSymbol = "!@#$%^&*"
charactersNumbers = "1234567890"

#Receive user input 
print("Enter Password Length: ")
passLength = int(input())

#TODO: validate password for number

print ("Should your password include Uppercase Letters? Y/N")
use_alpha_Uppercase = input()

print ("Do you want to use Lowercase Alphabets? Y/N ")
use_alpha_Lowercase = input()

print ("Should we include symbols as well? Y/N")
use_Symbols = input()

#build the character list
mycharacters = ""

if use_alpha_Uppercase.upper() == "Y":
	mycharacters = mycharacters + charactersUpper

if use_alpha_Lowercase.upper() == "Y":
    mycharacters = mycharacters + charactersLower

if use_Symbols.upper() == "Y":
    mycharacters = mycharacters + charactersSymbol

	
total_length = len(mycharacters)

final_password = ""

for y in range(0,passLength):	
	#gen_rand_num = math.floor(random.randrange(1,total_length))
	gen_rand_num = random.randrange(1,total_length)	

	#build the password with the random characters
	final_password = final_password + mycharacters[gen_rand_num]
		
print ("Your Password is: " , final_password)



