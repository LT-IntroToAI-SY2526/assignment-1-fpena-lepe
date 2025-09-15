# Assignment 1: AI-Generated Python Problems
# Name: Franco Pena-Lepe

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class.
 I have some experience with Java, i took ap csa last year, but i havent coded in 3-4 months. 
 I have zero experience with python Can you create 5-7 practice problems that cover:
> - Variables and basic data types > - Conditionals (if/elif/else) > - Loops (for and while) > - Functions > - Basic list operations > > 
Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Variable Practice: Greeting Bot
Topic: Variables & strings
Description:
Create a program that stores your name in a variable and prints a greeting like "Hello, <name>!"
"""
name="Franco"
print("Hello "+ name)

"""
Problem 2: Odd or Even Checker
Topic: Conditionals
Description:
Ask the user to input an integer. Print "Even" if the number is even, and "Odd" if it’s odd.
Hint: Use the modulo operator %.
"""

num=int(input("Enter a number:"))
if num%2==0:
    print("even")

else:
    print("odd")


"""
    Problem 3:
    3. Countdown Timer
    Topic: Loops (while loop)
    Description:
    Write a program that asks the user for a starting number, then counts down to 0, printing each number.
    """
start=int(input("enter a starting number:"))
for num in range(start,-1,-1):
    print(num)


"""
Problem 4:
4. Multiples Printer
Topic: Loops (for loop)
Description:
Create a function print_multiples(n) that prints all multiples of 3 from 1 to n (inclusive).
"""
def print_multiples(n: int)-> None:
    for num in range(1,n+1,1):
        if num%3==0:
            print(num)


    """
Problem 5:
5. Grade Categorizer
Topic: Conditionals + Functions
Description:
Write a function categorize_grade(score) that takes a number 0–100 and returns a letter grade based on this scale:
90–100: A
80–89: B
70–79: C
60–69: D
Below 60: F
"""
def categorize_grade(score: int)-> str:
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    elif score<60:
        return "F"
    """
Problem 6:
6. Sum of List
Topic: Lists + Loops
Description:
Write a function sum_list(numbers) that takes a list of numbers and returns the total sum.
"""
def sum_list(numbers: list)-> int:
    total=0
    for i in numbers:
        total+=i
    return total

    """
Problem 7:
Find the Maximum
Topic: Lists + Loops + Conditionals
Description:
Write a function find_max(lst) that returns the largest number in a list without using the built-in max() function.
"""
def find_max(lst: list)-> int:
    big=lst[0]
    for i in lst:
        if i>big:
            big=i
    return big

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


