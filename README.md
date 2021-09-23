# Password_Generator
*Sundeep Mistry - (23/09/2021)*

A password generator created in python using the randint() and shuffle() functions found in the random package. 
This script takes 4 user entered numbers between 1 and 5, each representing how many capitals, lower case, numbers and 
symbols to generate. 

Using randint() a random integer is generated, which in turn is converted to its Ascii
equivalent using the chr() function. The shuffle() function then takes the string of all the generated characters and 
shuffles them before printing the final password.

This was a small project I challenged myself to make in a day to test my abilities. While creating this I learned more 
about the chr() function and got more practice with Try and Except blocks. 
