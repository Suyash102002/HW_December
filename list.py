grocery_list = ["Milk", "Orange", 1, 2, 3, True, 2+4j, 2.3]
print(type(grocery_list))
print(grocery_list[0])
print(grocery_list[-1])
print(grocery_list[1:])
print(grocery_list[1:4])
print("")

lis1 = ["Apple", "Banana"]
print(lis1)
lis1.append("orange")
print(lis1)
print("")

playlist = []
playlist.append("Sare jhan se acha")
playlist.append("Ae mere watan ke logo")
print(playlist)
print("")

bookshelf = []
bookshelf.append("book1")
bookshelf.append("book2")
print(bookshelf)
print("")

lis2 = ["brinjal"]
print(lis2)
lis2.insert(1, "banana")
print(lis2)
print("")

bus_seat = ["Ajay", "Bob", "Sanjay"]
bus_seat.insert(2, "Ram")
print(bus_seat)
print("")

my_list = ["Apple", "Banana", "orange"]
brothers_list = ["brinjal", "potato"]
my_list.extend(brothers_list)
print(my_list)
