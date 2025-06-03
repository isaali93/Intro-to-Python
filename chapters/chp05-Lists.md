# Lists

## What are Lists

If you've done programming before, you may have come across arrays. An _array_ is variable that can store a defined amount of date and if you remember, a variable is simply a defined memory location to holds a single value.

A _list_ is Python's answer to the traditional _array_. The differece is that traditionally, arrays must be defined with a predefined size however, lists can be defined as empty and items can be added or removed at will.

Each location of data stored in a list is referenced through an _index_ which represents the position of the value in the list. **_Indexes start from 0._**

_Typical layout_
|Data|80|531|254|23|443|5002|
|-|-|-|-|-|-|-|
|Index|0|1|2|3|4|5|

Looking at the above, each "block" represents a location to store data. In our case we're storing 6 items.

If we wanted to get the third item in the list, we'd reference index 2: `my_list[2]`

If we wanted the item in first position: `mylist[0]`

> [!IMPORTANT]
> Reminder, don't forget about scoping. A list created in a function is only accessible there and nowhere else

## Declaring lists

For lists we follow the same principle of variables in terms of naming conventions, but we include the square bracket `[]` and values are separated by `,`.

```Python
my_list = [] # empty list

print(my_list)

new_list = [1,2,3] # list with values
print(new_list)
```

## Working with Lists

Lists, like arrays, uses indexes to access the data stored in it. Let's look at basic example:

```Python
ports = [80,135,137,139,443,1099]

# Print the first port
print(ports[0])

# Print the third port
print(ports[2])
```

### Basic operations

_Getting the number of items_

We use the `len()` function:

```Python
ports = [80,135,137,139,443]

print(len(ports))
```

_Combining lists_

To combine to a list we can do list concatenation, similar to what we do with strings.

```Python
ports = [80,443,21]

new_ports = [23,25,53]

ports = ports + new_port

print(ports)
```

_Working with lists in a for loop_

```Python
ports = [80,135,137,139,443]

# index syntax
for x in range(len(ports)):
    print(f"{x}: {ports[x]}")

# Non-index syntax
for port in ports:
    print(f"port: {port}")
```

_Changing items in a list_

```Python
ports = [80,135,137,139,443]

print(ports)

# Changing 137 to 53
ports[2] = 53

print(ports)
```

_Taking input and storing in a list_
```Python
targets = []

while True:
    target = input("Enter target(type quit to exit): ")
    if target != "quit":
        targets.append(target)
    else:
        break

print(targets)
```

### Working with Indexes

We've mentioned the index is used to access the data in the list. Here are a few things we can do with indexes:

```Python
usernames = ["admin","test_user","sqladmin","root","www-data","webmin",]

# Print the first item
print(usernames[0])

# Print the third item
print(usernames[2])

# Print the first three items
print(usernames[0:2]) # option 1
print(usernames[:2]) # option 2

# Print the last item
print(usernames[-1])

# Print the last two items
print(usernames[-2:])

# Print every other item
print(usernames[::2]) # ascending order
print(usernames[::-2]) # descending order
```

### Deleting from a list

There are a few methods that come along with lists that we can use to remove items. These are:
1. `pop()`
2. `remove()`
3. `del()`

You may be wondering why can we just assign it nothing similar to this `usernames[2] = ""`. The thing is `""` is an empty string, therefore still has a value. The length is 0 however.

So what are the differences between the mentioned methods?

_pop()_

The `pop(x)` method removes the item at index 'x' and returns it. Think of it popping from the list and putting it aside.

For example:

```Python
my_list = ["mon","tues","wed","thur","fri","fridady","sat","sun"]

print(my_list.pop(5))
print(my_list)
```

_remove()_

The `remove(item)` method, removes the first occurence of an 'item' from the list.

```Python
# continuing with the my_list from the previous example

print(my_list.remove("mon"))
```

_del()_

`del(x)` removes the specified index 'x'.

```Python
del my_list[2]
print(my_list)
```

### Slicing lists

Python makes it easy to _slice_ lists which allows you to work on a specific section of a list.

The operator for this is `:`

With this operator, you can specify where to start and end a slice and how to step through.

We saw this in action in the working with indexes section.

Syntax:
`my_list = [start:stop:step]`

```Python
usernames = ["admin","test_user","sqladmin","root","www-data","webmin",]

print(usernames[1:4:2]
```

Let's breakdown the`print` statement:

We'll print from the usernames list, every _2nd_ index starting from index_1_, stopping at index _4_ but not including it.

Your result should be `['test user','root']`

> [!TIP]
> All sections are omittable, as we will see shortly.

Let's say, for example, we want every 2nd item in the list
`usernames[::2]`

This will return every other username from the usernames list.

How about printing the last item first the decending:
`usernames[::-1]`

Getting the last time:
`usernames[-1::]`

