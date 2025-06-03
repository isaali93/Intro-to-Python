# File Handling

In this chapter we will work with opening and closing files.

Out of the box, Python comes with standard functionality built in to work with basic text files:
- .txt
- .csv
- any file that's not encoded (text file saved as a .log or .ini file)


## Reading from a file

Working with files can be as easy or as complex as you need/want it to be.

Why do I say this? Because Python comes with file handling built-in as well as it has several exeternal modules and packages that do the same as well as work on specialized file types such as SQL, PDF, Images, Audio, HTML, JSON, etc.

### The basics

_The _open()_ statement_

To open a text file in python is pretty straight forward with the `open()` function.

```Python
my_file = open("targets.txt", "r")
print(my_file.read())
```

The `open()` function, assigns the file to the variable my_file. We then use the `read()` function to read the files contents and assign it to the our variable. A major issue with this is that you have to include the `close()` function, as the file will remain perterually opened with can leave to dat corruption or process lock.

```Python
my_file = open("targets.txt","r")
my_file.read()
print(my_file)
my_file.close()
```

The `open()` function takes 2 arguments: the actual filename and its mode.

#### File modes

|Operator|Mode|Description|
|-|-|-|
|r|Read|Read-only. Throws an error if file is not found|
|r+|Read and Write|Open the file for reading and writing. Throws an error if it doesn't exist|
|w|Write|Write-only. Throws an error if the file is not found|
|w+| Read and Write| Opens the file for reading and writing. Overwrites the file if it already exists and creates the file if it doesn't exist|
|a|Append|Append data. If file does not exist, create the file|
|x|Create|Creates the file. If already exists, it throws an error|

_You can use the + symbol to modify the mode as you can see._

_The with() and open() statements_

Using the `open()` function with `with()`.

```Python
with open("targets.txt","r") as target_file:
    file_content = target_file.read()
    print(file_content)
```

> [!NOTE]
> Note the difference between with-open and just open - there's no close() used with with-open()

#### read() and readline()

You'd notice that Python has 2 functions for reading from a file, _read()_ and _readline()_.

_read()_ reads the content from the file, all at once.
_readline()_ read the content from the file line by line. This make readline great for working with loops.


## Writing to a file

We use `.read()` to read the content of a file, so we use........`.write()` to write content to a file.


_The write() function_

The `write()` function is part of the built-in file object in Python. To write to a file is just as simple as reading from the the file.

First we set the file in the write mode and simply pass the data we want to write to it.

```Python
message = "Message in a bottle"
with open("file.txt","w") as f:
    f.write(message)
    f.close()
```
In this example, we set the file mode to "write only". This means that if the file already exists with content, it will be overwritten.

It's a good idea to use the "append" or "a" option for writing to files and it just adds the new data to the end of the file.

## Relative and Absolute File Paths

__Relative File Paths__

A relative file path tell Python to look for a given location relative to the directory where the currently running program file is stored.

For example, your Python project is in *python_projects/* and the text file is in a sub-directory *text_files/* within the Python project, then relative path would be `'text_files/file1.txt'`.

__Absolute File Paths__

The absolute file path is the exact location of the file on your computers hard drive.

Using the same example from the relative file path, the absolute file path will something like this: `'C:/Users/User1/Documents/python_projects/text_files/file1.txt'`.

# File Modules

## os and pathlib

Keeping with the theme of "batteries included", Python also as a few third-party / external modules for file handling and these are:
* the os module
* the pathlib module

These modules do more or less the same thing, provides python access to the controls for working with directories and files (no the creation of the files however), with their major difference being that one provides a lower level access (os module) and the other providing a more abstracted, high-level access (pathlib).

In your development journey, you usually find yourself using both pathlib and os modules.

### pathlib Module

__Reading a file__

```Python
from pathlib import Path

path = Path('targets.txt')
contents = path.read_text()
print(contents)
```

> [!NOTE]
> When using read_text(), ypu may get a blank line appearing at the end of your output. This is because read_text() returns an empty string when it reaches the end of a file.

__Writing a file__

```Python
from pathlib import Path

path = Path('targets.txt')
path.write_text("192.168.1.1")
```

With the above example, if there is already content in the targets.txt file, it will be overwritten. The easiest way to deal with this is to read the content first and append the new data to it.

```Python
from pathlib import Path

path = Path("targets.txt")
read_data = path.read_text()

if read_data:
    read_data += "10.10.1.1\n"
    read_data += "172.16.23.2\n"
    path.write_text(read_data)
else:
    data = "10.10.1.1\n"
    data += "172.16.23.2\n"
    path.write_text(data)
```

__Get the system default home directory__

```Python
from pathlib import Path

print(f"Default path: {Path.home}")
```

__Get the current working document__

```Python
from pathlib import Path

print(Path.cwd())
```

### os module

The os modules help you as a programmer by providing a portable way of using operating system dependant functionality.

This module gives us options to manipulate file paths, make directories, and other operating system specific actions such as getting environment details, getting logged on user profile, etc.

Some key options to be aware of

|Function|Description|
|--|--|
|os.name|Get the current operating system|
|os.scandir()|Get the current directory listing|
|os.chdir(path)|Change directory|
|os.makedirs(d)|Make the provided directory|

__Get OS name__

Let's use the os module to get the os that the program is running on:

```Python
import os

if os.name == "nt":
    print("Current OS: Windows")
else:
    print("Current OS: Linux")
```

__Get the list of directories__

Now let's get the list of directoies in a folder

```Python
import os

total_listing = os.scandir()
print(total_listing)
```

