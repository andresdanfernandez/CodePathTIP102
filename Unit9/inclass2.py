'''
Problem 1: Graphing Flights
The following graph represents the different flights offered by CodePath Airlines. Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), and an edge between two vertices indicates that CodePath airlines offers flights between those two airports.

Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the airport's name (ex. "JFK").

flights graph

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here

Example Usage:

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

Example Output:
flight=
{
'JFK':['LAX', 'DFW'],
'LAX':['JFK'],
'DFW':['ATL', 'JFK'],
'ATL':['DFW']
}

['JFK', 'LAX', 'DFW', 'ATL']
[['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
['LAX', 'DFW']
'''

flight={
'JFK':['LAX', 'DFW'],
'LAX':['JFK'],
'DFW':['ATL', 'JFK'],
'ATL':['DFW']
}

"""
Problem 2: There and Back
As a flight coordinator for CodePath airlines, 

(you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination) and 


flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i] -> each destination in flights[i] is flights[j] ?.

Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j there also exists a flight from destination j to destination i. Return False otherwise.

def bidirectional_flights(flights):
    pass
Example Usage:

Example 1: flights1

'flights1' graph diagram

Example 2: flights2'flights2' graph diagram

ids:        0        1    2      3
flights1 = [[1, 2], [0], [0, 3], [2]]


flights1
{
    0: [1,2] -> key 1 and key 2 MUST have 0 as a value 
    1: [0]   -> key 0 MUST have 1 as a value
    2: [0,3] -> key 0 and key 3 MUST have 2 as a value
    3: [2]   -> key 2 MUST have 3 as a value
}

            0        1    2      3         
flights2 = [[1, 2], [], [0], [2]]


flights2
{ 
    0: [1,2],
    1: [],
    2: [0],
    3: [2]

}

print(bidirectional_flights(flights1))

print(bidirectional_flights(flights2))
Example Output:

True
False
"""

# Understand: We are given an adjacency list each flight must be bidirectional 

# Plan:


# flights1
# {
#     0: [1,2] -> key 1 and key 2 MUST have 0 as a value 
#     1: [0]   -> key 0 MUST have 1 as a value
#     2: [0,3] -> key 0 and key 3 MUST have 2 as a value
#     3: [2]   -> key 2 MUST have 3 as a value
# }

# Implement:

def bidirectional_flights(flights):

    flights_paths = {}

    for index, path in enumerate(flights):
        flights_paths[index] = path

    for key, value in flights_paths.items():
        # this iterates through our values -> ex: [1,2] -> 1, 2
        for val in value:
            # if 0 is not in 1:[0] and if 0 is not in 2:[0,3] 
            if key not in flights_paths[val]: 
                return False

    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

'''
Problem 3: Finding Direct Flights

Given an adjacency matrix flights of size n x n

Each of the n nodes in the graph represent a distinct destination 

n[i][j] = 1 indicates that there exists a flight from destination i to destination j 
n[i][j] = 0 indicates that no such flight exists.

Given flights and an integer source representing the destination a customer is flying out of, return a list of all destinations the customer can reach from source on a direct flight. You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of source.

def get_direct_flights(flights, source):
    pass
Example Usage:

'flights' graph diagram

flights = [
            0  1  2  3
         0 [0, 1, 1, 0],
         1 [1, 0, 0, 0],
         2 [1, 1, 0, 1],
         3 [0, 0, 0, 0]]

         2 -> col: [0] row: [0,1,3]

         

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))

Example Output:

[0, 1, 3]
[]
'''