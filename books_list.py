# Write code below 💖
# list of methods that python has built in

#.append() adds an item to the end of a list (VERY USEFUL FOR LEETCODE)
#.insert() adds an item to a specific index
#.remove() removes an item from a list based on the value
#.pop() removes an item at a particular index

# Methods use the . notation syntax. Functions can be called by themselves by methods are always attached to a list variable
# from which they are being called from

books = ['Harry Potter', 1984, 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']
print(books)
books.append('Pachinko')
books.pop(1)
books.remove('The Fault in Our Stars')
print(books)