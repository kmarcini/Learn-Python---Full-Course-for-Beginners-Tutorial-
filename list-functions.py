
lucky_numbers = [42, 8, 917, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers) #adds the list "lucky_numbers" to the end of friends list
friends.append("Creed") # appends Creed to the end of the list
friends.insert(1, "Kelly") # inserts Kelly at index 1, pushes the rest of the list
friends.remove("Jim") # removes the named element
# friends.clear() #removes all items
friends.pop() # removes last item
friends.sort()
lucky_numbers.sort()

friends2 = friends.copy()
friends2.reverse()

print(friends2)

print(friends.index("Kevin"))
print(friends.count("Jim"))
print(friends)

print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
