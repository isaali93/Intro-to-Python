# Basic Syntax, Variables and Data Types

Like all other programming languages, Python follows a general structure when writing a program, this includes keywords reserved for Python, ways to define data, passing data, assigning data and values and much more.

## Syntax and Comments

### Syntax

Combining program logic, data assignments, computations and calculations that a computer can interpret and understand is called syntax. Syntax is just the industry term for valid code. The rules for how expressions and statements should be structured.

> Syntax is the rules for how expressions and statements should be structured in a language.

Here's an example of syntax:
Java
```Java
system.out.println("This is a line of code");
```

Python
```Python
print("This is also a line of code.")
```

Because syntax is the rules for valid code, you will get syntax errors or errors in your code. However, syntax errors aren’t the only type of errors you’d encounter. Other types of errors include:

* Logic errors (bugs) – code is valid but does something unexpected
* Performance errors – code is valid and works but does it slowly

**_Indentation Matters!_**

Most programming languages require your syntax to be indented depending on its process, however, indentation is used mostly as a visual indicator for the developer.

In Python, indentation matters and impacts the execution of your code. For example, function code must be indented within its function block.

**Valid Syntax**

```Python
def add_num(a,b):
    c = a + b
```

**Invalid Syntax**

```Python
def add_num(a,b):
c = a + b
```

There are other types of problems that we will encounter outside of syntax errors, and these include:
* Logic errors: your code is valid and runs but it does something unexpected or output the wrong data.
* Performance: everything works as expected, but it does it slow.

### Comments

Comments are annotations in the code that are ignored by Python. They are typically used by programmers to understand the code by providing  context or explanations.

There are 2 types of comments in Python:
1. Single-line comments
2. Multi-line comments (also known as docstrings)

- Single-line comments start with a #
- Multi-line comments begin and end with “”” or ‘’’ (3 single quotes to start and to end or 3 double quotes to start and to end)

Example code:

_Single line comment_
`# This is a comment`

_Multi-line comment_
```Python
'''
This is line 1 of the comment
This is line 2 of the comment
'''
```

## Variables and Constants

Programs in their execution take data in, process it and produce a result. But where is this data stored? That’s where variables and constants come into play.

Variables are how we store data as the program runs. The value of a variable can always change. Constants are variables that store data that isn’t intended to change.

### Variables

As mentioned before, variables are how we store data as the program runs. They are allocations in memory reserved to store the data and can be accessed by the program in order to be used in calculations or presenting of data to the user.

Unlike in other languages, Python does not require you to define a variable before you can use it. You can define a variable anytime you want to, use it calculations and never use it again.

Bear in mind, if you access that variable again, it takes on the value it has been assigned. For example, you can define `my_speed = 150` and later in code you can define `my_speed = “fast”`.

**Creating (Declaring) variables**

A variable, effectively, is a name we create to access the location in memory to store and read data.

`port_number = 80`
`service_name = "active directory"`

**Using variable**

`print(port_number)`
`print("Service: ", service_name)`

**Multiple variable declarations**

`port_number, service, ip_address = 443,"https","192.168.1.45"`

The above assigned the relative variable to the matching value. The equivalent would look like this:
```Python
port_number = 443
service = "https"
ip_address = "192.168.1.45"
```

#### Naming conventions

* Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.
* Spaces are not allowed in variable names. Use underscores to separate words in variable names.
* Avoid using Python keywords and function names as variable names. For example, do not use the word print as a variable name.
* Variable names should be short but descriptive. For example, name is better than n, target_name is better than t_n, and name_length is better than length_of_persons_name.

> [!TIP]
> _The accepted standard for python is snake_case._

|Name|Description|Code Example|
|----|-----------|------------|
| Snake Case | All words are lowercase and separated by underscores | my\_ip\_address |
| Camel Case | Capitalize the first letter of each word except the first one | myIpAddress |
| Pascal Case | Capitalize the first letter of each word | MyIpAddress |

#### Storing results

Let's look at some basic math.
```
sum = a + b
diff = a - b
multi = a * b
division = a / b
avg = (a + b + c) / 3
```

### Constants

As mentioned before, constants are just regular variables that do not change. This is a bit of smoke and mirrors. There is nothing stopping you from changing the value of a constant through code if it is used incorrectly.

To define a constant, it is convention in python to declare it in all capital letters. For example: `DEFAULT_PORT = 3389`

### _Throw away variable_

Python has the ability to define what's known as a throw away variable, `_` (underscore).

A throw away variable is one that takes data that you're not going to use. For example, accepting data from a user but you only want to store the first word and discard everything else.

We'll encoutner this more in loops and some 3rd party modules.

## Basic Data Types

Data types are a grouping or classification a set of data belongs to. For example, numbers, decimals or text. All variables take on the data type of the data assigned to it.

Basic data types include:
- Strings
- Numbers
- Boolean

**Strings**

In programming, snippets of characters are called strings. Essentially, these are a group or list of characters strung together.

To create a string, we simply wrap the text in single or double quotes (python convention usually prefers double quotes for strings).

For example:

`ip_address = '192.168.1.1'`

`hostname = "targetname"`

**Numbers**

Numbers are your typical numbers, and are written without the quotes. (NB. If you wrap a number in quotes it is treated as a string and therefore calculations will produce an error).

Numbers are further broken down into 2 main categories: *integer* and *float*.

- An integer is a number without the decimal.
- A float is a number with the decimal.

Both an integer and a float can be positive or negative.

For example:

```Python
postive_integer = 1
negative_integer = -53
postive_float = 3.14
negative_float = -65.4
```

You can use _ to denote the thousands in numbers:

```Python
cheque_acct = 1_000_000
save_acct = 1000000

print("Cheque account:", cheque_acct)
print("Saving account:", save_acct)
```

**Boolean**

Boolean variables can only have one of two valuesL *True* or *False*. That's it. It's the binary equivalent to 1 or 0.

For example:

`target_confirm = False`

**None type**

Python has an interesting type called the `None` type. This is a special type in Python that represents the absense of a value.

This is not to be mistaken for an empty value as an empty value is still technically has a _value of nothing_, and the None type has no value at all.

```Python
x_null = ""
y_None = None

print(x_null)
print(y_None)
```

### type function

The last thing we'd discuss here is a default function in Python and that the `type` function. This function can tell you the type of a data.

```Python
my_str = "This is a sentence"
my_int = 10
my_bool = False

print(type(my_str))
print(type(my_int))
print(type(my_bool))
```

This comes in handy when you're trying to debug your program, or trying to figure out how data is being stored in a variable so you can write the correct loop or flow control.

