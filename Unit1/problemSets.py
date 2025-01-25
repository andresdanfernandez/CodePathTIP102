"""


UNIT 1


Problem 1: Batman
Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".

def batman():
	pass
Example Usage:

batman()
Example Output:

I am vengeance. I am the night. I am Batman!


"""

def batman():
    print("I am vengeance. I am the night. I am Batman!")

batman()

"""
Problem 2: Mad Libs
Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".

def madlib(verb):
	pass
Example Usage

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)
Example Output:

"I have one power. I never give up. - Batman"
"I have one power. I never nap. - Batman"

"""

def madlib(verb):
    print(f"I have one power. I never {verb}")

madlib("nap")
madlib("give up")

"""
Problem 3: Trilogy
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."

def trilogy(year):
	pass
Example Usage:

year = 2008
trilogy(year)

year = 1998
trilogy(year)
Example Output:

"The Dark Knight"
"Christopher Nolan did not release a Batman movie in 1998."
"""

def trilogy(year):
    if year == "2005":
        print("Batman Begins")
    elif year == "2008":
        print("The Dark Knight")
    elif year == "2012":
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}")

trilogy("2008")
trilogy("1998")

"""
Problem 4: Last
Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.

def get_last(items):
	pass
Example Usage

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
Example Output:

"black adam"
None
"""

def get_last(items):
    if not items:
        return None
    return items[-1]

print(get_last(["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]))
print(get_last([]))

"""Problem 5: Concatenate
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

def concatenate(words):
	pass
Example Usage

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
Example Output:

"vengeancedarknessbatman"
"""""

def concatenate(words):
    result = ""
    for word in words:
        result += word
    return result

print(concatenate(["vengeance", "darkness", "batman"]))
print(concatenate([]))

"""
Problem 6: Squared
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

def squared(numbers):
	pass
Example Usage

numbers = [1, 2, 3]
squared(numbers)
Example Output:

[1, 4, 9]
"""

def squared(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    
    return result

print(squared([1, 2, 3]))

"""
Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
	pass
Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
Example Output:

"nananananana batman!"
"batman!"
"""

def nanana_batman(x):
	
    for _ in range(x):
        print("na", end="")
    print(" batman!")

nanana_batman(6)


"""
Problem 8: Find the Villain
Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices
 where the villain is found hiding in the crowd.

def find_villain(crowd, villain):
	pass
Example Usage

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
Example Output:

[1, 4, 6]
"""
def find_villain(crowd, villain):
    result = []

    for i in range(len(crowd)):
        if crowd[i] == villain:
            result.append(i)
    return result

print(find_villain(['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker'], 'The Joker'))

"""
Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

def get_odds(nums):
	pass
Example Usage

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
Example Output:

[1, 3]
[]

"""

def get_odds(nums):
    result = []

    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result

print(get_odds([1, 2, 3, 4]))
print(get_odds([2, 4, 6, 8]))


"""
Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter.
 The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
	pass
Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4
"""

def up_and_down(lst):
    oddCount = 0
    evenCount = 0

    for num in lst:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    
    return oddCount - evenCount

print(up_and_down([1, 2, 3]))
print(up_and_down([1, 3, 5]))
print(up_and_down([2, 4, 10, 2]))

"""
Problem 11: Running Sum
    Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman
    has stopped each month in Gotham City. The function should modify the list to return the running sum such that
    superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). You must modify the list in place; 
    you may not create any new lists as part of your solution.

def running_sum(superhero_stats):
	pass
Example Usage

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)
Example Output:

[1, 3, 6, 10]
[1, 2, 3, 4, 5]
[3, 4, 6, 16, 17]
"""

def running_sum(superhero_stats):
    for i in range(1, len(superhero_stats)):
        superhero_stats[i] += superhero_stats[i - 1]
    return superhero_stats

print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))


"""
Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
	pass
Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
Example Output:

['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]
"""

def shuffle(cards):
    n = len(cards) // 2
    shuffled = []
    for i in range(n):
        shuffled.append(cards[i])
        shuffled.append(cards[i + n])
    return shuffled

print(shuffle(['Joker', 'Queen', 2, 3, 'Ace', 7]))
print(shuffle([9, 2, 3, 'Joker', 'Joker', 3, 2, 9]))
print(shuffle([10, 10, 2, 2]))