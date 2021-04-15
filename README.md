# Loops and Classes
> **Hint:** Make sure you are printing something out with the `print` statement! Otherwise, you won't see any output from running your program!


## Requirements

By the end of this, you should have:
* Two different `.py` files (one for each code challenge).
* One text file with answers to the five reading comprehension questions.

---

# Code Challenges

## Problem 1: IOU!

### Skill you're practicing: Writing `for` loops to iterate over a list.

You have a list of Disney characters and you want to find out if each of them contain `i`, `o`, or `u` in their names. Loop through each character in the list and print out the following:

```
If the name contains a "u," print out the name plus "U are so Uniquely U!"
Otherwise if the name contains an "i," print out the name plus "I bet you're Impressively Intelligent!"
Otherwise if the name contains an "o," print out the name plus "O My! How Original!"
Otherwise, print the name plus "Ehh, a's and e's are so ordinary."
```

#### Starter Code

```python
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]

```

#### Expected Output

```
simba I bet you're Impressively Intelligent!
ariel I bet you're Impressively Intelligent!
pumba U are so Uniquely U!
flounder U are so Uniquely U!
nala Ehh, a's and e's are so ordinary.
ursula U are so Uniquely U!
scar Ehh, a's and e's are so ordinary.
flotsam O My! How Original!
timon I bet you're Impressively Intelligent!
```


> **Hint**: You can determine whether or not a string contains a particular character with an `if` statement. For example, `if "b" in my_string:` will be true if `my_string` contains any b's.

---

## Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

### Skill you're practicing: Writing `while` loops.

Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

```
While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" and subtract 3 degrees from the temperature.

Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better."
```

#### Starter Code

```python
temperature = 90
```

#### Expected Output

```
Temperature is 90 — crank the AC!
Temperature is 87 — crank the AC!
Temperature is 84 — crank the AC!
Temperature is 81 — crank the AC!
Temperature is 78 — crank the AC!
75. Ahh, that's better.
```

> **Hint:** Make sure that your loop conditional is being updated each iteration. Otherwise you'll end up with an infinite loop!

---

## Reading Material

Read through the examples in these two articles about [`for` loops](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3) and [`while` loops](https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3) from Digital Ocean. Then, answer the following questions.

1. What is a nested loop?
Using loops in computer programming allows us to automate and repeat similar tasks multiple times. In this tutorial, we’ll be covering Python’s for loop.

A for loop implements the repeated execution of code based on a loop counter or loop variable. This means that for loops are used most often when the number of iterations is known before entering the loop, unlike while loops which are conditionally based

Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept.



2. Which kind of loop is based on a conditional statement: `while` loops or `for` loops?
a while loop 
3. When you want to iterate a specific number of times, would you typically use a `while` loop or a `for` loop?
for loop
4. Is it possible to loop through a string one letter at a time? What is the example given in the article?
Yes ,It is poosible 

5. Extrapolate from what you learned in the articles: Do you think a `for` loop can be nested inside a `while` loop? Why or why not?
yes
---

# Classes and OOP in Python
Use your knowledge of Python Classes to create a homework tracker!

Create your classes in the provided `classroom.py` file.

> **Hint:** You may need to import the copy module to solve this section. [Here is an article about copying objects in Python](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)

## Exercise: Write the following classes
Let's practice writing classes with useful functionalities

* Create an **Assignment** class
  * Assignments have `name`, `github_url`, `completed`, and `grade` properties
  * `completed`'s initial value should be set to `False`
  * `grade`'s initial value should be set to `None`
  * Assignments have a `mark_done` method that take in the grade as an argument, and sets `grade` and `completed`

* Create a **Student** class
  * Students have `name`, `pending_homeworks` and `completed_homeworks` properties
  * Students have a `assign_homework` method
  * Students have a `complete_homework` method 
  * Students have a `print_outstanding_homeworks` method
  * The `assign_homework` method takes in an `Assignment` object, and adds it to its `pending_assignments` list
  * The `complete_homework` method takes in the name of the homework, and the grade as an argument. It finds the specified homework in the `pending_homeworks` list and calls it's `mark_done` method. The method removes the `Assignment` from `pending_homeworks` and adds it to `completed_homeworks` 
    * Returns `True` if assignment was found and modified, `False` if not found
  * `print_outstanding_homeworks` prints out the name of each of the `pending_homeworks`


* Create a **SeiClass** class
  * SeiClass has `name`, and `students` properties
  * SeiClass has an `add_student` method that takes in a `Student` object
  * SeiClass has an `assign_homework` method that takes in an `Assignment` object and assigns that assignment to every student
  * BONUS - What would need to be changed in our classes to facilitate a `print_avg_grade` function? Implement it!

    
Sample Input:

```py
nick = Student('Nick')
sarah = Student('Sarah')
brandi = Student('Brandi')

sei30 = SeiClass('sei30')
sei30.add_student(nick)
sei30.add_student(sarah)
sei30.add_student(brandi)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei30.assign_homework(assignment1)

nick.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

nick.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
brandi.print_outstanding_homeworks()
```

Sample Output

```
Nick has no outstanding homeworks!
Sarah has no outstanding homeworks!
Brandi still needs to turn in: Bounty Hunters
```
