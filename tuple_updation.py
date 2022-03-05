tuple1 = ("Sameer", "Dhanush", "Pradeep", "Akash", "Rilwan")
tuple2 = list(tuple1)
tuple2[2] = "Abinandhan"
tuple1 = tuple(tuple2)
print(tuple1)
 # this is for the updation of the tuple to change or add an input with converting into a list with creating of another variable.
 # and to add it with the help of list conversion method and convert into tuple to add it in the same tuple input that helps us to change or add an input with the list creation.
 # this is for remove and then paste it in the given index location of the given tuple.

tuple1 = ("Sameer", "Dhanush", "Pradeep", "Akash", "Rilwan")
tuple2 = list(tuple1)
tuple2.append("Abinandhan")
tuple1 = tuple(tuple2)
print(tuple1)
# this is also an another method for adding an input through the append method with converion process of list and tuple.

tuple1 = ("Sameer", "Dhanush", "Pradeep", "Akash", "Rilwan")
tuple2 = ("Abinandhan",)
tuple1 += tuple2
print(tuple1)
# added in the last of the tuple in the new tuple creation and added it with ( tuple1 = tuple1 + tuple2 )