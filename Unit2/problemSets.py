

"""

Problem 1: Festival Lineup
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    pass
Example Usage:

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

Example Output:

{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}


"""

# Understand the problem: Given artist list and set time list where each ith artist and set time must be connected via key-value pair
# if artist list empty or set list empty, return empty dict 

# Plan a solution step-by-step: Create dict, iterate through artists using range, i iterator will map the set time to the artist, set will
# be the value, and artist will be the key, return result

# Implement the solution:

def lineup(artists, set_times):
    
    if not (artists or set_times):
        return {}
    
    results = {}

    for i in range(len(artists)):
        # map each artist to their respective set time
        results[artists[i]] = set_times[i]
    
    return results
    
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

print(lineup(artists1, set_times1))

artists2 = []
set_times2 = []

print(lineup(artists2, set_times2))

"""
Problem 2: Planning App
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    pass
Example Usage:

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
Example Output:

{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}"""

# Understand the problem: Were accepting a string artist, and given a dict festival_schedule where we want to know whether
# that artist is mapped in our festival_schedule, and if they are we want to return their value, otherwise if the artist doesn't
# exist we return a dict -> {'message': 'Artist not found'}.

# Plan a solution step-by-step: iterate festival schedule using key, value festival_schedule.items() then we want to check
# if "artist" is present -> return value, after the loop ends if we dont return we can assume the artist isn't present therefore
# we return -> {'message': 'Artist not found'}

# Implement the solution:

def get_artist_info(artist, festival_schedule):
    
    for key, value in festival_schedule.items():
        if key == artist:
            return value
    
    return {'message': 'Artist not found'}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))


"""

Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    pass
Example Usage:

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
Example Output:

{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}
"""

# Understand the problem: We take in two dicts with artists as keys and their set times as values. We need to find out
# if 2 key value pairs are the same add this key value pair to result dict.

# Plan a solution step-by-step: create result dict. keys = venue1.keys(), values = venue1.values() * 2 for venue 2. list1= zip(keys1, values1), list2 = zip(keys2, values2)
# make list1 a set using set(list1), iterate through list2 using a,b and check if value exits in our set. If it does match result[a] = b.
# return results


# Implement the solution:

def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}

    keys1, values1 = venue1_schedule.keys(), venue1_schedule.values()

    keys2, values2 = venue2_schedule.keys(), venue2_schedule.values()
    
    list1 = set(zip(keys1, values1))

    list2 = zip(keys2, values2)

    for a,b in list2:

        if (a,b) in list1:
            result[a] = b
        
    return result

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

"""
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflictions = {}
    for key in venue1_schedule: # iterate through venue 1 
        if key in venue2_schedule and venue1_schedule[key] == venue2_schedule[key]: # if in venue 2,  and times == for both venue 1 and venue 2
            conflictions[key] = venue1_schedule[key] #add to confliction dictioary
    return conflictions

"""


"""

Problem 5: Best Set
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    pass
Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
Example Output:

SZA
Ethel Cain
Note: SZA and Ethel Cain would both be acceptable answers for the second example
"""

# Understand the problem: we take in vote dictionary and return most voted for person.

# Plan a solution step-by-step: freq = {}, iterate through values from votes, for every value check if it is in the dict, if it is, increment its freq
# value by 1 if it hasnt been seen before we initialize our artist using key to 1. then return max(freq.values())

# Implement the solution:

def best_set(votes):

    freq = {}

    for value in votes.values():

        freq[value] = 1 + freq.get(value, 0)
    
    list1 = list(zip(freq.values(), freq.keys()))
    print(list1)
    print(max(list1))
    return max(zip(freq.values(), freq.keys()))[-1]
    


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
