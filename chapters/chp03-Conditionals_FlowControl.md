# Conditionals and Flow Control

It is very uncommon for you to write a program in modern times and have it executive instructions line by line, all the way to the end. This is where flow control and conditions come into play.

These can decide on actions to be taken or where the program needs to go to in order to process some data. Think of flow control as the symbols in a flow chart and conditionals as the decisions between those symbols.

Before you learn about flow control statements and conditions, we need to learn how to represent those yes and no "decisions", and how to write those branches as Python.

We've already mentioned the Boolean data type already (True or False). Ideally, this is what Python looks for, in order to determine if a condition is met and that flow goes one way or if it is not met and flow goes another way.

## Operators

### Boolean operators

Boolean operators are similar to the Logic Gates in electronics. These are the basic foundations that allow bits to flow.

There are three (3) main Boolean operators:
* `or #logical OR`
* `and #logical AND`
* `not #logical NOT`

**OR**

With the `or` operator, any one of the conditions needs to be true for a task or output to occur.
Let's look at this Truth Table.

|Condition A|Condition B|Output C|
|------|-------|---------|
|True|False|True|
|False|True|True|
|True|True|True|
|False|False|False|

**AND**

The `and` operator, unlike the `or`, requires all conditions to be met.

|Condition A|Condition B|Output C|
|-|-|-|
|True|False|False|
|False|True|False|
|True|True|True|
|False|False|False|

**NOT**

The `not` operator just takes the opposite of whatever the state of the condition is.

|Condition A|Output C|
|-|-|
|True|False|
|False|True|

### Comparison operators

The Boolean operators simply look at whether something is True or False. Comparison operators compare the states of something, or the values between data sources and returns a Boolean result.

|Operator|Description|
|-|-|
|==|Equals to...|
|!=|Not equal...|
|>|Greater than...|
|<|Less than...|
|>=|Greater than _or_ equal to...|
|<=|Less than _or_ equal to...|

> [!NOTE]
> Pay attention to the _assignment operator (=)_ and the _equals to operator (==)_. They are not the same.

Some examples:
```Python
target1_port_a = 80
target2_port_a = 443

print(target1_port_a == target2_port_a)
print(target1_port_a != target2_port_a)
print(target1_port_a >= target2_port_a)
print(target1_port_a <= target2_port_a)
print(target1_port_a > target2_port_a)
print(target1_port_a < target2_port_a)
```

And of course, don't forget to combine the Boolean and Comparison operators:

```
target1_port_a = 80
target2_port_a = 443
target3_port_a = 3389

print((target1_port_a == target3_port_a) and (target2_port_b <= target1_port_a))
```

### Structure

Typical structure for flow control usually starts with the _condition_ followed by the _instructions or code block_ to execute based on the outcome of the condition.

For example:

```Python
port = 3389
target_os = "Windows 2008"

if target_os == "Windows 2008": # Condition to check
    print("Windows 2008 found") # code or instruction to execute
    if port == 3389: # condition is the instruction to execute
        print("Target vulnerable to BlueKeep!")
```

## Flow Control

### if statements

This is the most popular and widely used statment. The _if statement_ has 2 sections as seen in the previous example: the condition (starting with the _if_ keyword followed by the action or instruction to be executed.

> [!IMPORTANT]
> Please remember indentation is very important with python. You always indent the code relevant to the specific section.

```Python
if x <= 5:
    print(x)

if my_day == "Saturday":
    print("It's not Friday")
```

With the _if statement_, you typically exceute code if something is true, but you can also execute code for a false condition. This is done with the _else_ keyword.

```Python
if value <= 15:
    print(value)
else:
    print("Max value reached")

if to_day == "Friday":
    post_video = True
else:
    print("pending Friday")
    post_video = False
```

But what if we want to check multiple conditions?

Well, we can do the following:
1. Perform more than one conditional check in the opening statement, or
2. We can use nested if statments (if statements within if statements)

```Python
# Multiple checks
if x > 5 and x < 10:
    print(x)

# Nested if
if x > 5:
    if x < 10:
        print(x)
```

Introducing the _else-if statement (elif)_.

```Python
if x <= 5:
    print(f"{x} < 5")
elif <= 20:
    print(f"5 > {x} <= 20")
else:
    print("Value is big")
```

Yes you can combine _if statements_, _nested if statements_ and _elif statements_. When would you use them? Well, that depends on what your program requires and how you'd like to structure it.

_Match Case_

In Python we have an alternative to the _if_ statement, called _match-case_ that follows the same logic as an if statment but can be more concise. Look at the following example:

```Python
print("--= Menu =--")
print(f"[1] Add\n[2] Sub\n[3]Exit")
user_input = input("enter a menu selection: ")

# If statement
if user_input == "1":
    print("action 1")
elif user_input == "2":
    print("action 2")
elif user_input == "3":
    print("action 3")
else:
    print("invalid option")

# Match Case
match user_input:
    case "1":
        print("action 1")
    case "2":
        print("action 2")
    case "3":
        print("action 3")
    case _:
        print("invalid action")
```

The main thing that match-case provides is readability. Complex conditional checks are simpler to understand with the match case.

## Loops

_If statement_ execute instruction based on a condition being evaluate once. But what is we want to repeat the execution of code until a condition is no longer true. This is where Loops come in.

Loops, like _if statements_ evaluate a condition and executes code, the difference is _if statements_ do this evaluation step once, and loops continuously do it untill the condition is false.

In Python there are 2 basic loops:
1. While loop
2. For loop

### While Loops

A _while loop_ is a statement that executes it's code consistently for as long as the condition is true.

Similar to the _if statement_, the structure starts with the condition to evaluate followed by the instructions.

```Python
run = True # escape flag
counter = 0

# infinite loop
while run == True:
    print(counter += 1)

# escape the loop
while run:
    print(counter += 2)
    if counter == 15:
        run = False
```

You may have noticed that with the _while loop_ it is easy for a program to remain stuck in a loop...and you'd be right. That's why we set a mechanism to break out of the loop, by introducing a conditon that sets the variable to a false state, which breaks the loop.

Another way to break out of a loop is through the break function.

```Python
count = 0

while True:
    prompt = input("Enter IP: ")
    if prompt == "exit":
        break
    else:
        print(prompt)

while True:
    count += 1
    print(count)
    if count == 10:
        break  
```

#### Continue and Break

The `break` and `continue` functions are another way to control the follow of a loop or process.

_break_

With `break` you can break out of a loop or process if a condition is met.

```Python
while True:
    if user_input == "0":
        break
    else:
        print(user_input)
    
    user_input = input("enter a number: ")
```

_continue_

`continue` simply follows onto the next step of a process. This is best seen in an example:

```Python

for x in range(0,10):
    if x % 2 == 0: # checks to see if a number is even
        continue
    else:
        print(x)
```

### For loops

_While loops_ go until the condition fails. _For loops_ on the other repeat the execution of code for a predefined condition, or example, do something 5 times.

```Python
for x in range(5):
    print(x)
```

Yes, we introduced a new keyword, `in` and yes it does exactly what your thinking. And we introduced the `range` function which, again does exactly as you thing (generate a range of numbers to the indicated limit).

In the for loop example above, we are checking a range of numbers, starting from and including 0, assigning it to the variable x and our code block will print x until x becomes 5, then exits.

_What does `in` do_

`in` is a fucntion that checks to see if _value a_ is in some data source. The data source can be anything from a variable to a list of data. (Lists we will take about later). Think of `in` as doing the same thing that `==` does but instead of being limited to just comparing values, it checks if the value exists.

Here's an example:
```Python
port_list = [80,443,3389,1099]
port = 53

if port in port_list:
    print("Port already registered")
else:
    print(f"Port {port} is not registered")
```

```Python
dns = ["1.1.1.1","8.8.8.8"]
search = input("Search IP: ")

if search not in dns:
    print("IP not found")
else:
    print("IP Found")
```

_The range function_

The `range()` function generates numbers in order, based upon at least, the end point being defined. Note that the `range()` function returns the starting number and includes it, generates until the end number but does not including it: `range(0,5) will return 0,1,2,3,4 and range(0,6) will return 0,1,2,3,4,5`.

```Python
for x in range(5):
    print(x) # this will print 0,1,2,3,4

for y in range(0,5):
    print(y) # this will print the same as above

for z in range(0,10,2):
    print(z) # this will print every 2 numbers starting from 0, ie. 0,2,4,6,8
```

