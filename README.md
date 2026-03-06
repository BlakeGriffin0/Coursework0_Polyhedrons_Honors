# Coursework0_Polyhedrons_Honors
Polyhedron calculation from end user input that outputs to the terminal.

Project Report
Class: PROG 1003, Section:01
Project: HW1 – Polyhedrons
Name: Blake Griffin

Problem
•	The problem is I need a program to calculate the area, volume, circumscribed sphere, and mass when constructed of aluminum, iron, and uranium.
•	The program is designed to ask the end user for input of the side length of the polyhedron and validate that the user input is a numerical value. The program then calculates and outputs the area, volume, circumscribed sphere, and mass of various materials out to the user in the terminal. The results were testing with various values to ensure it only accepted numbers and output the correct results.
Analysis
•	I decided to ask the end user for the side length of the given polyhedron and to use the formula to calculate the previously listed desired outputs.
•	Some of the most challenging parts of the program were ensuring the formulas were correctly executed and that the values were defined as floats for the calculation and output. I also had some difficulty with programming the input validation because I had never done that myself, however I already understood the concept.
•	I tried to use the least number of variables after originally having so many that it became confusing to work with. I know that variables are updated to the most recently input value, but I needed some variables to remain the same value to work with a different calculation later. The final approach is the best approach for me at the time because I was able to define new. Variables to output that were calculated from a previously defined variable in an equation.
Design
•	At the beginning of the program, I imported math to work with exponents and square roots. I also had to ensure that variables input into equations were floating point values to be exact to the hundredths place and to reduce the amount memory used hopefully. The output incorporates the same concept to be exact and not a long ugly decimal that uses to much memory. 
Testing
•	I tested the calculations of my program’s normal operations with a calculator multiple times with different values. I tested a wide variety of numbers and digit / decimal length to find an edge case, and no numerical values threw an exception. Originally, the program had no input validation which caused an exception when a non-numeric value was entered. I was able to fix that by adding a “try:” loop to be sure the input was a number or decimal (float), otherwise the program will loop on the input portion and output a value error saying, “It must be a numerical value” basically. 
Reflection
•	I learned how to validate user input to prevent exceptions while writing this program for our homework assignment. I previously understood the difference between integers, floats, and strings, but I had never done user input validation myself. Learning to validate that the input / output is a float was very useful for future programming.
•	The most challenging part of this project was working with the variables and learning input validation as I said previously. 
•	If I had to do the project over again, I would spend more time on minimizing the number of variables and lines of code.
•	I think having less lines of code and a program that is easier to read and work with would improve the accuracy and consistency of the solution.
•	The solution would be easier to use with minimal things to work with and read as I said previously.
•	I think the solution could be more robust in future projects by using longer strings and doing more than a few calculations and outputting them in a single print statement one by one. 

