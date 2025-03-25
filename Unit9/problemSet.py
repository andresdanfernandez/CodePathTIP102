"""
Problem 1: Space Crew
Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.

Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).

Hint: Introduction to dictionaries

def space_crew(crew, position):
    pass
Example Usage:

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))
Example Output:

{
    "Andreas Mogensen": "Commander",
    "Jasmin Moghbeli": "Flight Engineer",
    "Satoshi Furukawa": "Flight Engineer",
    "Loral O'Hara": "Flight Engineer",
    "Konstantin Borisov": "Flight Engineer",
}

{
    "Michael López-Alegría": "Commander",
    "Walter Villadei": "Mission Pilot",
    "Alper Gezeravcı": "Mission Specialist",
    "Marcus Wandt": "Mission Specialist"
}
"""
"""
def space_crew(crew, position):
    crew_dict = {}
    for i in range(len(crew)):
        crew_dict[crew[i]] = position[i]
    return crew_dict
"""

"""
Problem 2: Space Encyclopedia
Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, write a function planet_lookup() that accepts a string planet_name and returns a string in the form Planet <planet_name> has an orbital period of <orbital period> Earth days and has <number of moons> moons. If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".

def planet_lookup(planet_name):
    pass
Example Usage:

planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))
"""
"""
def planet_lookup(planet_name):
    planetary_info = {
        "Mercury": {
            "Moons": 0,
            "Orbital Period": 88
        },
        "Earth": {
            "Moons": 1,
            "Orbital Period": 365.25
        },
        "Mars": {
            "Moons": 2,
            "Orbital Period": 687
        },
        "Jupiter": {
            "Moons": 79,
            "Orbital Period": 10592
        }
    }
    
    if planet_name in planetary_info:
        planet_data = planetary_info[planet_name]
        moons = planet_data["Moons"]
        orbital_period = planet_data["Orbital Period"]
        return f"Planet {planet_name} has an orbital period of {orbital_period} Earth days and has {moons} moons."
    else:
        return "Sorry, I have no data on that planet.
"""
"""
Problem 3: Breathing Room
As part of your job as an astronaut, you need to perform routine safety checks. You are given a dictionary oxygen_levels which maps room names to current oxygen levels and two integers min_val and max_val specifying the acceptable range of oxygen levels. Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    pass
Example Usage:

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))
Example Output:

['Storage Bay']
"""

"""
def check_oxygen_levels(oxygen_levels, min_val, max_val):
    out_of_range_rooms = []
    for room, level in oxygen_levels.items():
        if level < min_val or level > max_val:
            out_of_range_rooms.append(room)
    return out_of_range_rooms
"""

"""
Problem 4: Experiment Analysis
Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.

def data_difference(experiment1, experiment2):
    pass
Example Usage:

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))
Example Output:

{'temperature': 22, 'humidity': 45}
"""

"""
def data_difference(experiment1, experiment2):
    result = {}
    for key in experiment1:
        if key not in experiment2 or experiment1[key] != experiment2[key]:
            result[key] = experiment1[key]
    return result
"""

"""
Problem 5: Name the Node
NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. Given a list of strings votes where each string in the list is a voter's suggested new name, implement a function get_winner() that returns the suggestion with the most number of votes.

If there is a tie, return either option.

def get_winner(votes):
    pass
Example Usage:

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))
Example Output:

Colbert
Serenity

Note: Colbert and Serenity would both be acceptable answers for the second example
"""
"""
def get_winner(votes):
    vote_count = {}
    for name in votes:
        if name in vote_count:
            vote_count[name] += 1
        else:
            vote_count[name] = 1
    max_votes = max(vote_count.values())
    winners = [name for name, count in vote_count.items() if count == max_votes]
    return winners[0]
    """
"""
Problem 6: Check if the Transmission is Complete
Ground control has sent a transmission containing important information. A complete transmission is one where every letter of the English alphabet appears at least once.

Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.

def check_if_complete_transmission(transmission):

    :type transmission: str
    :rtype: bool
Example Usage:

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))
Example Output:

True
False
"""
"""
def check_if_complete_transmission(transmission):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    transmission_letters = set(transmission)
    return transmission_letters.issuperset(alphabet)
"""
"""
Problem 7: Signal Pairs
Ground control is analyzing signal patterns received from different probes. You are given a 0-indexed array signals consisting of distinct strings.

The string signals[i] can be paired with the string signals[j] if the string signals[i] is equal to the reversed string of signals[j]. 0 <= i < j < len(signals). Return the maximum number of pairs that can be formed from the array signals.

Note that each string can belong in at most one pair.

def max_number_of_string_pairs(signals):
    pass
Example Usage:

signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))
Example Output:

2
1
0
"""

"""
def max_number_of_string_pairs(signals):
    used = set()
    count = 0
    for i in range(len(signals)):
        if signals[i] not in used:
            reversed_str = signals[i][::-1]
            for j in range(i + 1, len(signals)):
                if signals[j] == reversed_str and signals[j] not in used:
                    count += 1
                    used.add(signals[i])
                    used.add(signals[j])
                    break
    return count
"""

"""
Problem 8: Find the Difference of Two Signal Arrays
You are given two 0-indexed integer arrays signals1 and signals2, representing signal data from two different probes. Return a list answer of size 2 where:

answer[0] is a list of all distinct integers in signals1 which are not present in signals2.
answer[1] is a list of all distinct integers in signals2 which are not present in signals1.
Note that the integers in the lists may be returned in any order.

Below is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

1. Convert signals1 and signals2 to sets.
2. Find the difference between set1 and set2 and store it in diff1.
3. Find the difference between set2 and set1 and store it in diff2.
4. Return the list [diff1, diff2].
def find_difference(signals1, signals2):
    pass
Example Usage:

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))
Example Output:

[[1, 3], [4, 6]]
[[3], []]
"""
"""
def find_difference(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)
    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)
    return [diff1, diff2]
"""

"""
Problem 9: Common Signals Between Space Probes
Two space probes have collected signals represented by integer arrays signals1 and signals2 of sizes n and m, respectively. Calculate the following values:

answer1: the number of indices i such that signals1[i] exists in signals2.
answer2: the number of indices j such that signals2[j] exists in signals1.
Return [answer1, answer2].

def find_common_signals(signals1, signals2):
    pass
Example Usage:

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))
Example Output:

[2, 1]
[3, 4]
[0, 0]
"""
"""
def find_common_signals(signals1, signals2):
    set2 = set(signals2)
    answer1 = sum(1 for num in signals1 if num in set2)
    
    set1 = set(signals1)
    answer2 = sum(1 for num in signals2 if num in set1)
    
    return [answer1, answer2]
"""

"""
Problem 10: Common Signals Between Space Probes II
If you implemented find_common_signals() in the previous problem using dictionaries, try implementing find_common_signals() again using sets instead of dictionaries. If you implemented find_common_signals() using sets, use dictionaries this time.

Once you've come up with your second solution, compare the two. Is one solution better than the other? How so? Why or why not?

def find_common_signals(signals1, signals2):
    pass
Example Usage:

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))
Example Output:

[2, 1]
[3, 4]
[0, 0]
"""

"""
def find_common_signals(signals1, signals2):
    freq2 = {}
    for num in signals2:
        freq2[num] = freq2.get(num, 0) + 1
    
    answer1 = 0
    for num in signals1:
        if num in freq2:
            answer1 += 1
    
    freq1 = {}
    for num in signals1:
        freq1[num] = freq1.get(num, 0) + 1
    
    answer2 = 0
    for num in signals2:
        if num in freq1:
            answer2 += 1
    
    return [answer1, answer2]
"""

"""
Problem 11: Sort Signal Data
Ground control needs to analyze the frequency of signal data received from different probes. Given an array of integers signals, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.

Below is a buggy or incomplete version of the solution. Identify and fix the bugs in the code. Then, perform a code review and suggest improvements.

def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 0

    sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

    return sorted_signals
Example Usage:

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1)) 
print(frequency_sort(signals2)) 
print(frequency_sort(signals3))
Example Output:

[3, 1, 1, 2, 2, 2]
[1, 3, 3, 2, 2]
[5, -1, 4, 4, -6, -6, 1, 1, 1]
"""
"""
def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 1

    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))
    return sorted_signals
"""
"""
Problem 12: Final Communication Hub
You are given an array paths, where paths[i] = [hubA, hubB] means there exists a direct communication path going from hubA to hubB. Return the final communication hub, that is, the hub without any outgoing path to another hub.

It is guaranteed that the paths form a line without any loops, therefore, there will be exactly one final communication hub.

def find_final_hub(paths):
    pass
Example Usage:

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))
Example Output:

"Europa"
"Delta"
"StationZ"
"""
"""
def find_final_hub(paths):
    outgoing_hubs = set()
    all_hubs = set()
    
    for path in paths:
        outgoing_hubs.add(path[0])
        all_hubs.add(path[0])
        all_hubs.add(path[1])
    
    for hub in all_hubs:
        if hub not in outgoing_hubs:
            return hub
    return None
"""