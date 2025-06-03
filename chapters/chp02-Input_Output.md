# Input and Output

## Printing to the screen

So far all of our output has been to the terminal or console. This is common for your python program to make input from the user via the console and return data to the console.

For our purposes, we'll be focusing on the console and not a GUI (Graphical User Interface).

### The print function

This is nothing new as we've used it regularly so far:

```Python
port_number = 80
ip_address = "192.168.1.1"
print(port_number)
print("Port: ", port_number)
print("Port: ", port_number," IP: ", ip_address)
```

**Multi-line printing**

```Python
print('''Ransomware deployed

We haz all yur data

Sincerely,
haxors
''')
```

**Printing strings within strings**

This is where using double quotes ("") and single quotes ('') comes in handy.

```Python
print("A Trini once said: 'Yuh mudda'")
```

**Escaping special characters**

```Python
print("When you want to include the double quote \"")
```

**New lines and Tabs**

```Python
print("This is the first line.\nThis is the second line") # \n adds a new line similar to pressing enter
print("Col1\tCol2\tCol3") # \t adds a tab space similar to pressing tab
```

**f-strings**

f-strings is a way to “format” the print function.

f-strings, provide a concise and readable way to include variable values within strings. The f before the string denotes an f-string, and any expression inside curly brackets {} is evaluated and interpolated into the string at runtime. This feature is useful for creating dynamic strings with embedded variable values.

For example:

```Python
hostname = "target.com"
ip_addr = "192.168.1.45"
port = 80
print(f"Targeting {hostname} at {ip_addr} via port number {port}")
```

Another example:

```Python
var1 = 10
var2 = 5
print(f"Sum of {var} and {var2} is {var1 + var2}")
```

> [!TIP]
> f-strings are not limited to just printing. You can use f-strings to format the data of a variable, `my_str = f"target: {variable1}"`

> [!CAUTION]
> Avoid doing critical calculations in print statements. (Not a rule, just a best practice.)

f-strings a great way to format your data to be displayed.

Here are some other interesting things with the formatting data:

```Python
name = "haxor"
event = 50323.345
my_value = 1024.456
my_int = 139
print(f"{my_value:.2f}") # this will print the number with 2 decimal places
print(f"{my_value:.0f}") # this will print the number without any decimal places
print(f"{name:15} ==> {event:15:2f}") # putting a integer immediately after the ':' will specify the minimum number of characters to be displayed.
```

## Taking input

We’ve looked at variables and printing data to the screen via the console window. But at some point, you will need to take some form of user input. Thankfully, this is extremely simple to implement with Python.

To take input, we just use the keyword `input()`. The `()` allows you to put the prompt you’d like to display to the users.

```Python
input("Please enter IP Address: ")
```

To store the input from a user, we simply assign it to a variable:

```Python
target_ip = input("IP Addr: ")
print(f"IP: {target_ip})"
```

> [!IMPORTANT]
> By default, input passes everything as a string value, that is, if the user enters 45, it will be stored as a string and standard numerical calculations will be invalid. We will cover convering data types later.

### Working with numbers

Mathematical operations can be performed using arithmetic operators. These operators include:

- addition (+)
- subtraction (-)
- multiplication (\*)
- division (/)

They can be used to perform calculations on variables and store the results.

Some worked examples:

```
a = 10
b = 10
sum = a + b
diff = a - b
multi = a * b
divi = a / b
```

_Some more mathematical calculations_

- Exponents (powers): 3 \*\* 2 \= 9  
- Modulus: 10 % 2 \= 0 (returns the remainder of a division, 10 / 2 has a remainder 0)
- Floor: 15 // 2 = 7 (division that drops the fractional component)


Note on calculations:

- Adding numbers of the same type (for example integers) will return the result as the same data type (adding integers will produce an integer for its result).  
- The above  also applies to subtraction and multiplication as well.
- For adding and subtraction, and working with mixed numeric types (integer and float) the result will always be a float  
- *Standard division (/) always returns a float* for its result. No exceptions

_Converting to a number (integer or float)_

```Python
port_string = "123"
port = int(port_string)

ping_ttl = "127.3"
ping_value = float(ping_ttl)
```

### Working with strings

Remember, a string is a collection of characters, (0-9,a-z, etc.)

Python comes with a bunch of functions built right in, so that you do not need to figure out everything.

**Changing case**

One of the simplest tasks you can do with strings is change the case of the words in a string.

```Python
username = “jon snow”
print(username.title()) # Jon Snow
print(username.upper()) #JON SNOW
print(username.lower()) # jon snow
print(username.capitalize()) # Jon snow
```

And more formating:

```Python
fname, lname = “jon”, “snow”
print(fname + lname) # jonsnow
print(fname, lname) # jon snow
print(fname, lname, “is not dead.”) # jon snow is not dead.
print(fname.title(), name.title(), “is not dead.”) # Jon Snow is not dead.
print(fname,”\n”,lname) # \n adds a new line
print(fname + “\n” + lname)
print(f”{fname}\n{lname}”) 
print(f”{fname}\t{lname}”) # \t adds a tab character (4 spaces)
```

**Indexing and Spliting strings**

_Splitting/Slicing_

```Python
target = "example.com"
domain = target.split()
print(domain)
```

The split operator, default splits a string on the space “ “. The output is something called a list (which we will discuss later).
You can change what the function splits on by placing it in the braces, i.e my\_var.split(“e”. This will split the string wherever an “e” is encountered.

If we continue with the above, the `split()` function outputs a list (we will discuss later but it is the equivalent to an array), therefore `print(domain)` will print `['example','.com']`

So, if you remember multiple variable assignments:

```Python
reg, tld = domain[0],domain[1]
```

_Indexing_

```Pyton
username = "adminUser"
print(username[0])
```

Some things for you to try:

1. `print(username[3])`
2. `print(username[-1])`
3. `print(username[0:5])`
4. `print(username[:3])`
5. `print(username[2:])`

**String arithmetic**

```Python
username = "fakeuser"
domain = "fakedomain.com"
email = username + "@" + domain
print(email)
```

_Converting to a String_

```Python
port = 80 #integer
port_string = str(port)

ping_time = 127.4
ping_string = str(ping_time)

user_exists = True # boolean
user_string = str(user_exists)
```

