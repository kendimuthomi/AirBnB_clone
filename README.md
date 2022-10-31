# AirBnB_clone
This project is the barebones and backend skeleton for an eventual clone of the
AirBnB site.
models
**base_model
Starting with the models we have the base class that is the BaseModel that contains the
methods and the preliminary attributes to the subsequent classes which will inherit
from it:
	*initialisation
		- Generate the model's UNIQUE id
		- Detail when it was created and updated
		- If you create a model based of an existing dictionary
		  it will use the dictionary values instead to initialise the dictionary
	*save
		- updates the time value of the instance detailing when it was updated
		- serializes the instance to a json file for storage
	*to_dict()
		- This method while innoucous at first is doubly important as a
		  critical part of the architecture.
		- You will be tempted to ask why not just discard this and use the instance's
		  __dict__ attribute don't.
		- The main thing it does is create a dictionary based on __dict__ and to it
		  add a class_name attribute.

The other models in this directory basically inherit from the BaseModel with the files
just detailing extra attributes it has to distinguish each from the other.

models.engine
**file_storage
This here class deals with serialization and deserialization of previously created instances
	*all
		- returns a dictionary object containing all previously saved instances
	*new
		- takes in a model instance and adds it to the dictionary of current objects
	*save
		- Using the dictionary of current objects it stores the dictionary representation
		  of them (using to_dict()) in a storage json file.
	*reload
		- Here is the tricky part, it deserializes the data from the json file and 
		  extract the class name (to_dict()
