name = ["sameer", "Akash", "pradeep"]
name.append("dhanush") # insert any input value to the last/end of the list
name.sort() # for sorting or arranging it in a ascending/descending order
print(name)

name1 = ["Sameer", "Akash", "Rilwan"]
name1.clear() # clear all the elements in the list
print(name1)

name2 = ["Sameer", "Akash", "Rilwan"]
name2.insert(1, "Dhanush") # insert at the specific position using the index value
name2.pop(2) # deleting/removing an input at the specific position using the index value
print(name2)

name3 = ["Sameer", "Akash", "Rilwan", "Dhanush"]
name3.remove("Rilwan") # specifically removes an input using the remove method
name3.reverse() # reverse the list values
print(name3)

name4 = ["Sameer", "Akash", "Rilwan"]
out =  name4.index("Sameer") # check the index value of the given input
print(out)

name5 = ["Sameer", "Akash", "Rilwan", "Dhanush", "Pradeep", "Dhanush"]
out = name5.count("Dhanush")
print(out)

dict_names = {"Sameer": "Brother", "Akash": "Dude", "Rilwan": "Heart", "Dhanush": "Love", "Pradeep": "Fun"}
out = dict_names.keys() # for printing keys only in the given input.
print(out)
# use (values()) of to printing values in the dictionary key value pair.

name5 = {"Sameer": "Sam", "Akash": "Kash", "Rilwan": "Ril", "Dhanush": "Dhan", "Pradeep": "Prad"}
out = name5.get("Pradeep") # get anything from the given input for getting an output.
print(out)


