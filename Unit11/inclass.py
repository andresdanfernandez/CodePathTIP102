"""Problem 1: Hollywood Stars
The following graph illustrates connections between different Hollywood stars. Each node represents a celebrity, and an edge between two nodes indicates that the celebrities know each other.

Create a variable hollywood_stars that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the celebrities's name (ex. "Kevin Bacon").

Celebrity Network Diagram

# No starter code is provided for this problem
# Add your code here
Example Usage:

print(list(hollywood_stars.keys()))
print(list(hollywood_stars.values()))
print(hollywood_stars["Kevin Bacon"])
Example Output:

['Kevin Bacon', 'Meryl Streep', 'Idris Elba', 'Laverne Cox', 'Sofia Vergara']


[['Laverne Cox', 'Sofia Vergara'], 
['Idris Elba', 'Sofia Vergara'], 
['Meryl Streep', 'Laverne Cox'], 
['Kevin Bacon', 'Idris Elba'], 
['Kevin Bacon', 'Meryl Streep']]

['Laverne Cox', 'Sofia Vergara']
"""

hollywood_stars = {
    'Kevin Bacon':['Laverne Cox', 'Sofia Vergara'],
    'Meryl Streep':['Idris Elba', 'Sofia Vergara'], 
    'Idris Elba':['Meryl Streep', 'Laverne Cox'], 
    'Laverne Cox':['Kevin Bacon', 'Idris Elba'], 
    'Sofia Vergara':['Kevin Bacon', 'Meryl Streep']
}

print(list(hollywood_stars.keys()))
print(list(hollywood_stars.values()))
print(hollywood_stars["Kevin Bacon"])


"""Problem 2: The Feeling is Mutual

You are given an insider look into the Hollywood gossip with an adjacency matrix celebrities where each node labeled 0 to n represents a celebrity. celebrities[i][j] = 1 indicates that celebrity i likes celebrity j and celebrities[i][j] = 0 indicates that celebrity i dislikes or doesn't know celebrity j. 

Write a function is_mutual() that returns True if all relationships between celebrities are mutual and False otherwise. A relationship between two celebrities is mutual if for any celebrity i that likes celebrity j, celebrity j also likes celebrity i.

def is_mutual(celebrities):
    pass
Example Usage:

Example 1: celebrities1

'celebrities1' graph diagram

Example 2: celebrities2'celebrities2' graph diagram

celebrities1 = [
                  0  1  2  3
              0  [0, 1, 1, 0],
              1  [1, 0, 1, 0],
              2  [1, 1, 0, 1],
              3  [0, 0, 1, 0]]

              0: [1,2]
              1: [0,2]
              2: [0,1,3]
              3: [2]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))
Example Output:

True
False
"""

# Understand: we want to figure out if each celebrity are mutual friends with eachother

# Match: directed, cyclic, unweighted

# Plan: convert the adjacency matrix to adjacency dict, then loop through items for val in key if key not in val return False

# Implement:


def is_mutual(celebrities):

    adj_dict = {}

    for i in range(len(celebrities)):
        for j in range(len(celebrities[i])):
            if celebrities[i][j] == 1:
                adj_dict[i] = adj_dict.get(i, [])
                if not i in adj_dict:
                    adj_dict[i] = [j]
                else:
                    adj_dict[i].append(j)

    for key, values in adj_dict.items():

        #  🎯
        #  0: [1,2]
        #      ⬇️  🎯
        #      1: [0,2] 

        #  🎯
        #  0: [1,2]
        #        ⬇️  🎯
        #        2: [0,1,3]
        for value in values:
            if key not in adj_dict[value]:
                return False
    return True
            
# celebrities1 = [
#                   0  1  2  3
#               0  [0, 1, 1, 0],
#               1  [1, 0, 1, 0],
#               2  [1, 1, 0, 1],
#               3  [0, 0, 1, 0]]

#               0: [1,2]
#               1: [0,2]
#               2: [0,1,3]
#               3: [2]


celebrities1 = [
                 
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))


'''
Problem 3: Closest Friends
You are a talented actor looking for your next big movie and want to leverage your connections to see if there are any good roles available. To increase your chances, you want to ask your closest friends first.

You have a 2D list contacts where contacts[i] = [celebrity_a, celebrity_b] indicates that there is a mutual relationship (undirected edge) between celebrity_a and celebrity_b. Given a celebrity celeb, return a list of the celebrity's closest friends.

celebrity_b is a close friend of celebrity_a if they are neighbors in the graph.

def get_close_friends(contacts, celeb):
    pass
Example Usage:

contacts = [["Lupita Nyong'o", "Jordan Peele"],
            ["Meryl Streep", "Jordan Peele"],
            ["Meryl Streep", "Lupita Nyong'o"], 
            ["Greta Gerwig", "Meryl Streep"],
            ["Ali Wong", "Greta Gerwig"]]

print(get_close_friends(contacts, "Lupita Nyong'o"))
print(get_close_friends(contacts, "Greta Gerwig"))
Example Output:

['Jordan Peele', 'Meryl Streep']
['Meryl Streep', 'Ali Wong']
'''

# Understand: we want to return a targets closest friend meaning that for each celebrity return its neighbors

# Plan: Create an adjacency dict
# key: Lupital values: Jordan Peele, Meryl Streep
# return list[key] -> 


def get_close_friends(contacts, celeb):
    friend_list = {} 

    for source, friend in contacts:
        
        if source not in friend_list:
            friend_list[source] = []
        friend_list[source].append(friend)

        if friend not in friend_list:
            friend_list[friend] = []
        friend_list[friend].append(source)

    return friend_list[celeb]

        # Lupita:[Jordan]
        # Meryl:[]
        # Greta:[]
        # Ali:[]
        # Jordan:[Lupita]

contacts = [["Lupita Nyong'o", "Jordan Peele"],
            ["Meryl Streep", "Jordan Peele"],
            ["Meryl Streep", "Lupita Nyong'o"], 
            ["Greta Gerwig", "Meryl Streep"],
            ["Ali Wong", "Greta Gerwig"]]

print(get_close_friends(contacts, "Lupita Nyong'o"))
print(get_close_friends(contacts, "Greta Gerwig"))

"""P
Problem 4: Network Lookup
You work for a talent agency and have a 2D list clients where clients[i] = [celebrity_a, celebrity_b] indicates that celebrity_a and celebrity_b have worked with each other. You want to create a more efficient lookup system for your agency by transforming clients into an equivalent adjacency matrix.

Given contacts:

Create a map of each unique celebrity in contacts to an integer ID with values 0 through n.
Using the celebrities' IDs, create an adjacency matrix where matrix[i][j] = 1 indicates that celebrity with ID i has worked with celebrity with ID j. Otherwise, matrix[i][j] should have value 0.
Return both the dictionary mapping celebrities to their ID and the adjacency matrix.

def get_adj_matrix(clients):
    pass
Example Usage:

'clients' graph diagram

clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)
Example Output:

{
  'Fred Armisen': 0,
  'Yalitza Aparicio': 1,
  'Margaret Cho': 2,
  'Bowen Yang': 3,
  'Ali Wong': 4,
  'Julio Torres': 5
}

[
  [0, 0, 0, 0, 1, 1],  # Fred Armisen
  [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
  [0, 0, 0, 1, 1, 0],  # Margaret Cho
  [0, 0, 1, 0, 1, 1],  # Bowen Yang
  [1, 0, 1, 1, 0, 0],  # Ali Wong
  [1, 1, 0, 1, 0, 0]   # Julio Torres
]

Note: The order in which you assign IDs and consequently your adjacency matrix may look different"""
