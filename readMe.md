# Week1:
## Q1 : 
Simple python program takes an input string given. Deletes the last two characters and prints the string in reverse order.
## Q2 : 
Simple python program takes a sentence as input and prints the same line by replacing python with pythons.
## Q3 : 
Simple python program takes the grade number as input and prints the grade letter from grade scale.

# Week2:
## Q1 :
fullname method:
It takes in two parameters, `fname` and `lname`, and concatenates them together with a space in between and returns the full name as a string.

string_alternative method:
It takes in one parameter, `fullname`, which is the full name returned by the fullname method and returns alternative characters from the first and last name.

## Q2 :

This program reads an input file named `input.txt` and performs word count on it, then it writes the output to an output file named `output.txt` in the same directory. The output contains the count of each word in the input file.

## Q3 :

This program converts a list of heights from inches to centimeters using both iterative and list comprehension methods and creates a new list. 

# Week3:

## Q1 :
We have class Employee with attributes `name`,`family`,list of `salaries` for consecutive years/months, `department`. We added a unique Id field to be able to store in DB as well as count the total no.of unique employees present. The Employee class has `printEmp()` method to print the details of employee and `avgsal()` method to to the average of salaries provided.

FulltimeEmployee class extends Employee class and has a `printFTEmp()` method to print all details of employee object.

The Employee constructor is called when a new Employee object, `emp2` is created and also when FulltimeEmployee object, `emp1` is created. We can also access method of parent class using child class objects while vice versa is not possible.

## Q2 :

This simple python file creates a random vector of length 20, with float values between 1-20. We reshape it to 4*5 matrix and replace the maximum value in each row by 0.0 using numpy where functionality.