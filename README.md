# AirBnB_clone
This project is the barebones and backend skeleton for an eventual clone of the
AirBnB site.
+ models


### base_model

Lets start with the super-model (pun intended) the BaseModel that contains the methods and the preliminary attributes to the subsequent classes which will inherit from it
Funcs:
- initialisation
	- Generate the model's UNIQUE id
	- Detail when it was created and updated
	- If you create a model based of an existing dictionary it will use the dictionary values instead to initialise the dictionary
- save
	- updates the time value of the instance detailing when it was updated
	- serializes the instance to a json file for storage
- to_dict()
	- This method while innoucous at first is doubly important as a critical part of the architecture.
	- You will be tempted to ask why not just discard this and use the instance's __dict__ attribute don't.
	- The main thing it does is create a dictionary based on __dict__ and to it add a class_name attribute.

The other models in this directory basically inherit from the BaseModel with the files
just detailing extra attributes it has to distinguish each from the other.

+ models.engine


### file_storage

This here class deals with serialization and deserialization of previously created instances
Functions:
- all
	- returns a dictionary object containing all previously saved instances
- new
	- takes in a model instance and adds it to the dictionary of current objects
- save
	- Using the dictionary of current objects it serializes the dictionary representation of them (using to_dict()) in a storage json file.
- reload
	- Here is the tricky part, it deserializes the data from the json file and using the class name attribute value serializes the objects into a variable by creating objects from the dictionary representations, this is done by calling new() on the dictionary representations (the code does a better explanation and that's what we call pythonic code boys and girls and the gentlefolk of course)

## Console

The console. Venture into the console.py file to its inner workings. Here we entail about how it works without getting into its mechanics.

If it has been a long time since working with python don't worry I got you, first execute the file console.py `$ ./console.py` (can't believe you had to be told this).

Now you are in the console.

Next you want to prompt help.
`(hbnb) help`

What you are seeing are the available methods that can be used with the exception of count.

Prompt help to any of the methods to find it's usage and the format/s it accepts, example:

`(hbnb) help create`

This console was advanced to now accept functions .all() .count()  .show() .destroy() and .update().

Basically they replicate the functions displayed in help but this time instead of spaces the functions takes in variables to execute the functions. Let me demostrate:

`(hbnb) User.destroy(231hkjh2kh3l12)`

is the same as typing in

`(hbnb) destroy User 231hkjh2kh3l12`

Use the same format for show.

To make it even fancier the () methods even accept the ids with/out the quotes and still works so:

`(hbnb) User.show("231hkjh2kh3l12")`

is the same as:

`(hbnb) User.show(231hkjh2kh3l12)`

Right!!! Fancy!!

The all() function is supposed to print all the instances of a certain specified model

`(hbnb) all User`

same as 

`(hbnb) User.all()`

Please note that this means that the `(hbnb) all` cannot be recreated by the all() func since it must take in a class name (same as count).

The count() method meanwhile is supposed to print the number of instances from a specific model that is stored in the json file.

`(hbnb) User.count()`

Prints out the number of instances that the model User has stored. Is handy when it comes to checking if a particular instance has been destroyed (I'll leave you to figure that out dummy).

#### update()
The update() method should get special attention first it has two ways in which you can use it to update or add attributes to an instance.

1. `<class name>.update(<id>, <attribute name>, <attribute value>)`

Use quotes as you please (I have already fancied it up) though it should be noted that the attribute value varies depending on the type of data it is if it is a string it SHOULD ALWAYS BE IN QUOTES, otherwise if not it SHOULD NOT be in quotes this is important as:

`(hbnb) User.update(2312312312sdfasdf, number, "4")`

is not the same as

`(hbnb) User.update(2312312312sdfasdf, number, 4)`

The first gives number a STRING attribute and the second gives it an INTEGER attribute value.


Next I'll give you another way to use update() but this time using a dictionary:

2. `<class name>.update(<id>, <dictionary representation>)`

Example:
`User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})`

Realise here that you can update/add more than one attribute of an instance, just make sure your dictionary is well formatted and structured.

And with that have fun kids and of course the gentlefolk who will review this.

This README was written by the ever humorous Vashow1 (Vashow wasn't available, damn you reddit).



Please optimize this code. We are but young developers u w u

