# Sets, Dictionaries and Tuples

Sets, Dictionaries and Tuples are 3 of the 4 common data structures in python. The 4th is Lists.

## Tuples

We'll start with the tuple. A tuple can be thought as a type of list with 2 major differences, 1) _tuples use ( and )_ while _list use [ and ]_; and 2) lists are mutable (you can change the value of data stored) while tuples are immutable (once defined, you cannot change the data stored).

With the exception of adding and removing items, tuples pretty much function just like a lists.

* Items a reference through an index
* Items are stored in the order they are created

### Defining a Tuple

Refresher:

```Python
my_list = [] # empty list
my_other_list = [1,2,3] # list containing numbers
```

When defining tuples we replace the [] with ().

```Python
dns_servers = ("1.1.1.1",'8.8.8.8")

print(dns_servers[0])
```

We created a tuple, `dns_servers` with two IP addresses. We then print the first index `[0]`.

If you try to change the values in the tuple, python throws an error.

```Python
dns_servers = ("1.1.1.1", "8.8.8.8")

dns_servers[1] = "8.8.4.4"
print(dns_servers)
```
If you run the above code, you will get an error (_TypeError_).

> [!NOTE]
> If you want to define a tuple with one item, you do so with the element followed by a comma, `dns_server = ("1.1.1.1",)`

### Working with Loops

The same principles apply for tuples when working loops.

_For loop_

```Python
c2_servers = ("10.10.1.24","172.33.23.45","53.51.53.2","34.12.69.2")

for server in c2_servers:
    print(server)

for i in range(len(c2_servers)):
    print(f"{i + 1}. {c2_servers[i]")
```

```Python
c2_servers = ("10.10.1.24","172.33.23.45","53.51.53.2","34.12.69.2")

x = 0

while x <= len(c2_servers):
    print(c2_servers[x])
    x += 1
```

### Overwritting tuples
As mentioned previously, we cannot change the items stored in a tuple. What we can do however is overwrite the values completely.

```Python 
c2_servers = ("8.8.8.8","1.1.1.1")

print(c2_servers)

c2_servers = ("1.1.0.1", "4.5.2.2")

print(c2_servers)
```

## Dictionaries

A Dictionary in Python is an interesting way to store data. Unlike the other common data structures that use indexes to reference values, dictionaries use keys and values (almost like a database). So it's stored in key-value pairs.

Because of this data is unordered but can be much more structured.

### Defining a dictionary

```Python

target_profile = {"domain":"example.local","subnets":['10.1.0.1/24','10.2.0.1/24','10.0.3.1/24'],"hosts":234,"address":"middle of NoWhere"}

print(target_profile)
```

From the above example, the first key-value pair is `domain:example.local` with the key being domain and the value being example.local. Notice that we can store different types of values (strings, numbers and even lists) but the keys be the same type. You can also store lists as values to keys or even tuples.

Here's another example

```Python
target_profile = {"domain":"example.local","subnets":['10.1.0.1/24','10.2.0.1/24','10.0.3.1/24'],"hosts":234,"address":"middle of NoWhere","users":{"user 1":"administrator","user 2":"sql admin","user 3","web admin"}}

print(target_profile)
```

In this example, we added a few more key-value pairs to the the dictionary including another dictionary, `"users":{"user 1","administrator","user 2","sql admin","user 3","web admin"}`. All a dictionary cares about is that it's a  key-value pair where the key is unique (no duplicate keys) and values are referenced by those keys. 

### Methods

Similar to Lists, Dictionaries come with pre-built methods that execute specific functions. Here's some of the more common methods:

1. clear()
2. update()
3. items()
4. pop()
5. keys()
6. values()

|Method|Desc|
|--|--|
|_clear()_|clear() empties the dictionary completely|
|_update()_|This updates the specified key with the provided value|
|_items()_|items() returns a tuple of the key-value pairs|
|_pop()_|Removes the value with the speified key|
|_keys()_|This returns a list of keys from the dictionary|
|_values()_|values() returns a list of all the values in a dictionary|

### Adding to a dictionary

```Python
groups = {}

groups["Akira"] = ["TSTT","random 1","random 2"]
groups["Play"] = ["Also Random","Also random 2"]

print(groups)
```
In the example above, we created an empty dictionary, `groups` then we assigned a key "Akira", `groups["Akira"]` and assigned it's value in the form of a list ["TSTT","random 1","random 2"]`. We repeated this process for the key "Play". Printing the group dictionary, we will have 2 key-value pairs.

### Updating values

```Python
c2_profile = {"proxies":["px.server.com","px2.server2.com","px3.drvr.net"],"dns1":"1.1.2.2","dns2":"192.168.1.1"}

print(c2_profile)

c2_profile["dns1"] = "172.16.3.2"
c2_profile["proxies"][1] = "prx2.server12.com"

print(c2_profile)
```

In this example, we have a dictionary called c2_profile that has 3 keys, _proxies_,_dns1_, and _dns2_. _proxies_ has a list of values.

It's simple enough to update the when it's single value. For lists, we need to reference the index as usual and just assign it a new value.

There's also an method called `update()` that comes with a dictionary.

_Using update()_

```Python
servers = {"dns":"192.168.1.1","proxy":"10.1.10.1"}

servers.update({"ad":"cdn.azureconnect.net"})
```

Using update(), you can update the dictionary by specifying the key with it's new value. If the key does not exist, python with create it as a new key-value pair. This works the same with the previous method. 

> [!IMPORTANT]
> If the value in the key-value pair was a list and you replace with with a single value, then it is *no longer* a list.

### Looping through a dictionary

You can use your regular for and while loops to go through the dictionary.

```Python
user_profile = {"user1":"Admin","user2":"Webmin","user3":"User"}

for x in range(len(user_profile)):
    print(x)
```

```Python
user_profile = {"user1":"Admin","user2":"Webmin","user3":"User"}

for item in user_profile:
    print(item,":",user_profile[item])
```

_Using items()_

Remember, dictionaries use key-value pair, therefore you're expecting 2 items everything.

```Python
user_profile = {"user1":"Admin","user2":"Webmin","user3":"User"}

for k,v in user_profile.items():
    print(k,v)
```

_Using get()_

get() takes two arguments:
 - 1: key to look up
 - 2: return if key not found

```Python
servers = {"primary":"1.1.1.1","secondary":"8.8.8.8"}

user = input("search key: ")

print(f"Lookup for {user}:",servers.get(user, "key not found"))
```

## Sets

Sets are an interesting data structure to work with in that, it's basically a list that does not allow for duplicate values as they guarantee uniqueness.

`user_profiles = {"Admin","User","Webmin"}`

For example:
```Python
my_list = [1,2,3,2,4,5,6,3,7,10]

my_set = set(my_list)

print(my_list)
print(my_set)
```

> [!NOTE]
> Pay attention to the difference between sets and dictionaries, as they both use {} but dictionaries take key-pair values (key:value) vs just values with sets.

### Declaring an empty set

```Python
my_ips = set()

my_ips.add("192.168.1.1) # adding a value to a set

print(my_ips)
```

_Adding values_
```Python
my_ips = set()

my_ips.add("192.168.1.1") # adding a value to a set
```

_Removing values_
```Python_
my_ips = {"10.10.1.1","192.168.2.45"}
print(my_ips)

my_ips.remove("10.10.1.1")
print(my_ips)
```

### Looping through a set

```Python
my_targets = {"google.com","example.net","target.co","not-a-real-target.gov"}

for target in my_targets:
    print(target)
```
