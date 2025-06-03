# Python Modules and Packages

Modules and Packages are what makes python so extensible.

Modules and Packages are ways that you can make large projects easier to manage, speed up development time, simplifies your program, encourages reusability, and improves maintainability.

## Modules

A module can be considered as a file or files that contain code that can be used by your program.

Take for example, you've written a calculator application before that does sum, difference, multipcation and division and you need to use those functions in another program. Instead of rewriting the code in your new program, you can simply import your calculator program and call the the functions from there.

In actually, all the programs we;ve written so far, can be used as a module. All we need to do is use the `import` statement in our code and that's it. We'd have access to the any of the functions.

But what separates our programs from actual modules is that generally, speaking, "production" modules can't stand on their own. meaning, you can't run them like you'd run one your programs. This is because "production" modules just contain a class (which we will talk about later in the course) and a bunch of functions defined. That's it.

## Packages

Packages are just complete software bundles that a typically made up of multiple modules. Packges are generally complex applications with several function calls, memory management components, and distribution and setup configurations defined.

We woont be writing any packages as that's beyond the scope of the beginner series. But you will know of the more populer packages, such as:

1. NumPy (Extended mathimatical functions)
2. Matplotlib (Extension for NumPy for plotting charts, etc)
3. Tensorflow (Machine Learning and AI)
4. Pandas (Data manipulation and Analysis)
5. PyGame (Game development framework)
6. PyTorch (Machine Learning) 

## Working with Modules and Packages

In most cases, the popular modules are preinstalled by default. Packages, you typically download, configure and install based on their requirements.

If a module is not installed, that's where the `pip` command comes in. In your terminal (command prompt, linux terminal, VS Code terminal) you can simply put `pip3 install <module name>` and on other occasions, you may be able to download from GitHub and follow the setup instructions (this is typical for packages however) using `pip3 install -r requirements` (there is usually a requirements file and this command just tells pip3 to install and configure based on the requirements.txt file).

### import

We'll work with a pretty basic but powerful module, _random_. The random modules introduces functions for the generation of pseudo-random numbers. [Details here](https://docs.python.org/3/library/random.html)

If we look at the documentation, the random module has a function called `randint` which takes an lower limit, an upper limit and generates a random number the can be as low as the lower limit or as high as the upper limit.

```Python
import random # import the random module

rand = random.randint(1,6)

print(rand)
```
First we import the module, `import random`, declare a variable, `rand`, and use it to store the output of the function call `random.randint(1,6)` which will return a number from 1 - 6.

_import as_

Python gives us a way to import modules in a more user-readible way by using the _as_ option.

```Python
import random as rd

rand = rd.randint(1,6)
print(rand)
```

The above does exactly the same as the previous example but we use an 'alias' of sorts to access the random module.

### from

As you can see, modules and packages can have many functions, and once your import the module, all its functions are loaded into memory. If you only need one function for a module, we can use the `from` function to load exactly what function from the module we want.

```Python
from random import randint

rand = randint(1,6)
print(rand)
```

And, we can always combine it with _as_

```Python
from random import randint as ri

rand = ri(1,6)
print(rand)
```

> [!TIP]
> It helps to read the documentation for python as it breaks down the built-in modules and extended modules including all functions, how they work and and parameters needed.
 
