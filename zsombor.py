def star_end_string(string):
    if len(string) < 2:
        return ''
    return string[:2] + string[-2:]

print(star_end_string("hola amigos"))

# Task 2 - Change characters
def swap_string(string):
    character = string[0]
    string = string.replace(character, '$')
    return string

print(swap_string('restart'))

# Task 3 - First repeated character
def first_repeated(string):
    temp = {}
    for char in string:
        if char in temp:
            return char, string.index(char)
        else:
            temp[char] = 0
    return 'None'

print(first_repeated('abcabc'))
print(first_repeated('abccba'))

myList = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
print(myList)

def matrix_to_list(lis):
    myTempList = []
    for items in lis:
        for value in items:
            myTempList.append(value)
    return myTempList

myList = matrix_to_list(myList)
print(myList)

# Task 5 - Remove item from tuple
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def remove_tuple_item(tup, val):
    print(tup)
    myList = list(tup)
    myList.remove(val)
    tup = tuple(myList)
    return tup

print(myTuple)
myTuple = remove_tuple_item(myTuple, 5)
print(myTuple)

# Task 6 - Sort a dictionary
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}

def sort_dictionary(dic, reverse=False):
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict
print(f"Colors dictionary:\n {colors}")
print("\nSort (ascending) the said dictionary elements by value:")
print(sort_dictionary(colors))
print("\nSort (descending) the said dictionary elements by value:")
print(sort_dictionary(colors, True))

# Task 7 - Remove every 3rd item
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist_2 = mylist.copy()
counter = 1
while len(mylist_2) != 0:
    for num in mylist[:]:  # Iterate over a copy to avoid issues with removals
        if num not in mylist_2:
            continue
        elif counter % 3 == 0:
            mylist_2.remove(num)
            print(num)
        counter += 1
# Task 8 - Mixing values
def permutations(nums):
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
    return result_perms

my_nums = [1, 2, 3, 4]
print("Original Collection: ", my_nums)
print("Collection of distinct numbers:\n", permutations(my_nums))