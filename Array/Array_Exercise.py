# Exercise: 1

expense_list = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?

print(expense_list[1] - expense_list[0])

# 2. Find out your total expense in first quarter (first three months) of the year.

print(sum(expense_list[:3]))

# 3. Find out if you spent exactly 2000 dollars in any month

print([i for i in range(len(expense_list)) if expense_list[i] == 2000] or "No value match")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense_list.append(1980)

# """5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this"""

expense_list[3] = expense_list[3] - 200
print(expense_list, "\n")


# Exercise: 2

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list

print(len(heros))

# 2. Add 'black panther' at the end of this list

heros.append("black panther")

# """3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'"""

heros.remove('black panther')
heros.insert(3, 'black panther')

#"""4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code."""

heros[2] = "doctor strange"

print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()

print(heros)