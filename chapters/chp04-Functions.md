# Functions

When you're coding, you typically want to repeat certain tasks given some data input or otherwise. It's impractical to rewrite a new loop or test everytime. This is where functions comes into play. A function is a defined code block that allows you too write a piece of code to be called upon whenever you need it.

Using a function is called a _function call_.

Functions are denoted by the keyword `def` followed by its name and `():`. This is then followed by the instructions for the function.

> [!IMPORTANT]
> Don't forget the indentation.

Here's an example of a basic function:

```Python
def banner(): # defining the function
    print(f"Welcome user to the Application")

banner() # function call
```

In the above code we have function called `banner()` and its instruction is to print a message to the screen, `print(...)`. The last line is the actual function call. Until this point, the code inside of the function will never be used.

## Order of execution

Python executes its tasks linearly, meaning, line by line (in general and for our purpuses.).

When working with functions, Python only knows your function exists if it was able to include it in it's exection step, that is, if your code calls for function `add(a,b)` on line 10 but it is defined at line 25, Python will throw an error and your program will exit.

Therefore a rule of thumb is to always define your functions at the top of your program and then write the main instructions for your code after.

Why does this happen? Because python is interpreted at execution time line by line as opposed to other languages like C or Java where it is compiled completely and then executed.

## Arguments and Parameters

_Positional Arguments_

Functions may need input to execute its tasks. To accommodate this, Python functions accept _arguments_. Arguments are positional in a function and represent the number of inputs required for the function code. If a function requires 2 inputs, and you provide just 1, python throws an error indicating that an argument is missing.

Here's an example of a function that takes parameters:

```Python
def add(a,b): # function defined with 2 positional parameters
    ans = a + b
    print(ans)

add(1,2) # calling the function and passing 2 arguments
```

Parameters are the variables defined for a function to execute its task. Eg. `def add(a,b)`, both 'a' and 'b' are parameters.

When the function is called, and provided with data, it's called an argument, Eg. `add(1,2)`, 1 and 2 are the arguments passed to the function.

This is purely for theroectical knowledge. What is key, is the  understanding that the function requires information for it to execute its task and it must be provided in the defined order.

In the previous example the function `add` requires 2 input values (parameters) `a and b`. The instructions inside are simple. We have a variable called `ans` that is assigned the value of `a + b`, then prints it to screen.

Functions can also return a value instead of simply printing it. With returning a value, we use the `return` keyword followed by what we want to return. 

> [!NOTE]
> Remember if your function is returning a value, it should ideally return it to be stored somewhere or used as part of a conditional check.

```Python
def add(a,b):
    ans = a + b
    return ans

def multi(a,b):
    return a * b

print(add(1,2))

value = multi(2,4)
print(value)
```

## Default argument values

There may be instances when you'd want to provide a default value to the function if the user or program does not provide it.

```Python
def set_target(target_name, port=80):
    print("Target details")
    print(f"Target: {target_name}")
    print(f"Port: {port}")

target = input("Target name: ")
target_port = int(input("Target port: "))

set_target(target)
set_target(target, target_port)
```

Looking at the code above, we have a function `set_target` that takes 2 arguments `target_name and port`. We've set the default value for port as 80 as seen by the `port=80`. This means that if a second argument is not provided to the function call, it will automatically use 80.

> [!IMPORTANT]
> Parameters that have a default value must always be defined last in the function definition, that is, `def set_target(target_name, domain="google.com", port=80)`
