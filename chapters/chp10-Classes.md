# Classes

Let's talk classes.

This is where start dipping into some of the advanced concepts of programming known as Object Oriented Programming (OOP).

## OOP

Object Oriented Programming, "OOP" is a way of writing clean and maintainable code. 

The idea behind OOP and functional programming is to make code easier to work with and understandable. Easier to read and understand generally means easier to debug issues, easier to walkthrough and understanding underlying operations.

It does not make your code faster or function correctly or even reduce the number of bugs but it does make it easier to find and fix bugs, develop faster and maintain sanity.

With objected oriented programming, an unspoked concept is writing easier maintainable code means writing code without repeating yourself, "DRY" - Don't Repeat Yourself. This is where functions comes into play.

### OOP Thinking ###

Classes in Object Oriented Programming are all about grouping data and behaviour together in one place, aka, an object.

From a video game perspective, items you pick up within the game has a class assigned such Health class, Ammo class, Armor class, etc.

The difference between OOP and functional programming is OOP tries to hold data abd simulate a specfic behaviour while functional programming tends to think of their code as how inputs are processed to produce an output.

```Python
human Class
human.walk()

human function
next_human = walk(prev_human)
```

### DRY Code

Don't Repeat Yourself, "DRY", code just means that whenever possible, you should avoid writing the same code in multiple places as this can cause:

- If you need to change it, you have apply the changes in multiple places
- If you forget a place, bugs are introduced into your code
- It's unnecessary work to continuously rewrite the same code over and over

The process of taking your code and refining in to be simpler or cleaner or more manageable is called _refactoring_.

> [!IMPORTANT]
> DRY code **does not** improve your program's performance but it can make your code shorter and easier to read, easier to update and improves the ability to fix bugs.

## The Basics

A class is special type of value as it is similar to a dictionary as it store other types within itself. The major difference is that instead of your working with built-in types and functions, classes allow you to define those yourself.

When you create a new instance of a class, this is called an object. Interestingly, you've already been working with classes. Every time you've imported a module and call a function from it, you've been calling a class with an associated function ("method").

```Python
import random #import module

rand_int = random.randint(0,5) # class the random called followed by its associate method
print(rand_int)
```

### Defining a Class

```Python
class Target: # Defining the class
    def add_target(self,target): # Class specific method
        self.target = target # Instance variable
```

It's general practice to name your class files the same name as the class, for example in this case, we'd save it as `target.py`.

### Instantiating a Class (Creating an instance)

Continuing from `target.py` class file, let's make a `main.py` file.

```Python
from target import Target # Import the class file

target_1 = Target() # Create a new instance
target_1.add_target("192.168.1.1") # Class method call

print(target_t.target)
```

Here's another look at the same.
```Python
class Target:
    default_ip = "10.10.1.1" # Class variable

    def update_ip(self,ip):
        self.default_ip = ip # Instance variable

comp = Target()
comp.update_ip("192.168.1.1")
print(comp.default_ip)
print(Target.default_ip)
```

> [!NOTE]
> Class variables that are accessible through instances like what is shown above are called _attributes_.

_Accessing Attributes_

To access attributes in the instance of a class, we use 'dot notataion'.

```Python
class Device():
    def __init__(self):
        self.hostname = "Target" # hostname's default value is set to "Target"

comp_1 = Device()
comp_1.hostname = "Target 2" # Accessing the hostname attribute
```

#### Modifying attribute values ####

You can change an attribute’s value in three ways:
1. Change the value directly through an instance
2. Set the value through a method
3. Increment the value (add a certain amount to it) through a method.

_Change the value directly_

This we've already seen: `comp_1.hostname = "Target 2"`

_Using a method_

We can define a method within the class to directly alters the value as opposed to the user having to do it

```Python
class Target:
    def __init__(self)
        self.default_ip = "10.10.1.1" # set default ip

    def update_ip(self,ip): # Method to update default_ip
        self.default_ip = ip

comp = Target()
comp.update_ip("192.168.1.1") # Call method to update the default_ip
```

_Increment the value through a method_

This is similar to using a method to update the attribute, the difference is we do not pass any information to the method. Instead we only need to call the method and it executes its instructions.

```Python
class Target:
    def __init__(self)
        self.default_ip = "10.10.1.1" # set default ip
        self.allowed_connections = 1

    def update_ip(self,ip): # Method to update default_ip
        self.default_ip = ip

    def update_connections(self):
        self.allowed_connections += 1 # this updates the allowed_connections by 1

comp = Target()
comp.update_connections() # method call to update the number of allowed connections
```

## Methods

This is one of the things that makes classes cool in that we can define _methods_ specifically for them. Remember a method is just a function but in this case it is tied to the class and has access to all its properties.

`comp.update_ip(ip)`

_self_

Method are nested within the _class_ declaration. Their first parameter is always the instance of the class that the method is being called on.

By convention, it's called self, and `self` is a reference to the object (hence self), therefore you can use it to read and update properties of the object itself (basically have the object talk to itself).

_Calling Methods_

After we create an instance of a class, we can use the same 'dot notation' as we do with accessing attributes to call any method defined within it. (For example, comp.update_ip("192.168.1.1")

### Constructors
A constructor is a special defined type of method that is called when a class is instantiated. Ideally, it creates the new object for use and often accepts pre-defined arguments that are used to set any required variables.

```Python
class Target:
    def __init__(self,ip,hostname,os):
        self.ip = ip
        self.hostname = hostname
        self.os = os

comp = Target("192.168.1.25","WINSERV1","Windows 2022")
print(comp.ip)
print(comp.hostname)
```

## Encapsulation

Encapsulation is, in a nutshell, the practice of obfuscating or hiding comlexity. A very simple example of this is functions. The caller of the fucntion doesn't need to worry much about what happens inside the function, they only need to understand the functions input requirements and what it outputs.

```Pyton
def is_url(url):
    if url.startswith("http"):
        print(f"{url} is a URL"}

is_url("https://www.google.com")
```

Looking that the above example, we've defined a function `is_url` that requires an input, `url`. The output of the function is to print if it is an URL or not. The caller doesn't need to know how it does the checks, just that it requires a single input value.

Encapsulation is more about organization. It's like storing folders in an unlocked cabinet, in that it does not stop anyone from peeking inside, but it does keep everything organized, neat, tidy and easy to find.

### Public vs Private
By default, all properties and methods in a class are _public_. That means that you can access them with the `.` operator

```Python
target.ip_addr = "10.10.1.10"
print(target.ip_addr)
```

_Private_ data members are a way to encapsulate logic and data within a class definition.

To make a property or method private, just prefix it with double underscores (__)

```Python
class Target:
    def __init__(self,ip,hostname,os):
        self.__ip = ip
        self.__hostname = hostname
        self.__os = os

    def get_ip(self):
        return self.__ip

target = Target("10.1.23.1","WINSERV","WINDOWS")

print(target.__ip) # This will return an error

print(target.get_ip()) # This will call the function that can access the private variable.
```

We do this to make it easier to use our class.

> [!IMPORTANT]
> Encapsulation and the concepts of private and public members have NOTHING to do with security. Kind of like how your computer or laptop's case hides all the internal components but you still can pop it open and see how it works - encapsulaion doesn't block anyone from lookig in and understanding your code, but it just keeps it all neatly organized.

Also Important!
> [!IMPORTANT]
> Encapsulation in Python is achieved mostly by convention rather than by force. This is due to Python being a dynamic langauge and this makes it difficult enforce the safeguards that other langauges allow.

## Abstraction

Let's talk _abstraction_.

Abstraction is the idea of handling complexity while hiding the unnecessary details.

This should feel pretty familiar. Right? Right??? This feels like encapsulation all over again and you'd be right to think that. In fact, knowing the difference between the two in most cases is not worth knowing in most cases.

* Abstraction is all about _creating a simple interface for complex behaviour_.
* Encapsulation is about _hiding internal states_.

Here's a clearer way to understand the concepts of Encapsulation and Abstraction:

Think about a complex problem, say drawing graphics on the screen. In Python we have a module called _tkinter_. Being able to draw a window on a screen along with adding text, buttons and functionality to the buttons is not easy. So the developers of the _tkinter_ library have _abstracted_ away the complextity and _ecapsulated_ it into simple functions calls; as simple as `window = tkinter.Tk()` and you'd have a very basic window.

## Inheritance

With classes, programmers get to define, attempt to define real world objects. But sometimes, it is impractical to define a class for every object. In this instance, we can use inhertiance to define a base class that has properties shared by all the objects and then define only the necessaray bits for the individual objects.

Here's a quick example:

Let's say we want to create a class of road vehicles a transport company owns. Since all vehicles share some common traits, such as wheels, colour and engine, we can define base class that has the common traits, then define what's necessary for the specific vehicle.

```Python
class Vehicle:
    def __init__(self,colour,engine_size):
        self.wheels = 4
        self.colour = colour
        self.engine_size = engine_size
        self.driver = ""
        self.total_mileage = 0

    def register_driver(self,name):
        self.driver = name

    def change_colour(self,colour):
        self.colour = colour

class Car(Vehicle):
    def __init__(self,colour,engine_size,fuel_type):
        super().__init__(colour,engine_size)
        self.fuel_type = fuel_type

honda = Car("White",1.8,"Gas")
print(honda.driver)
```
