"""
Problem 2: Top Artists

Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. 

Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
        self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
	pass

Example Usage:

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)

Example Output:

{ "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}


"""

# Understand: Input: Linked List Head (Playlist) Output: Frequency Dictionary {"artist":"frequency_times_seen_in_playlist"}

# Plan: Create freq_dict traverse linked list playlist, and check current.artist if its in our dict += 1 the value if not set artist as key and value to 1 
# (first time seen in playlist)


# class SongNode:
# 	def __init__(self, song, artist, next=None):
# 		self.song = song
# 		self.artist = artist
# 		self.next = next

# Implement:

# def get_artist_frequency(playlist):
	
#     freq_dict = {} # O(n) || O(set(current.artist))
	
#     current = playlist # 1
	
#     while current: # O(n)

#         """
#         freq_dict[current.artist] = 1 + freq_dict.get(current.artist, 0)
#         """
		
#         if current.artist in freq_dict: # 1
            
#         	freq_dict[current.artist] += 1 # 1
#         else:
#             freq_dict[current.artist] = 1 # 1
			
#         current = current.next # 1

#     return freq_dict # 1

# playlist = SongNode("Saturn", "SZA", SongNode("Who", "Jimin", SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA"))))

# Saturn:SZA -> Who:Jimin -> Espresson:Sabrina Carpenter -> Snooze:SZA

#print(get_artist_frequency(playlist)) # { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}

"""
Problem 3: Glitching Out

The following code attempts to remove the first node with a given song
from a singly linked list with head playlist_head but it contains a bug!

Step 1: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so 
that the function correctly removes a node by value from the list.

v add print statements and test current code

Step 2: Evaluate the time and space complexity of the fixed solution. Define your variables and provide a rationale for why you 
believe the solution has the stated time and space complexity.

class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
        self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None

    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

Example Usage:

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

Expected Output:

('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')

"""


class SongNode:
     
	def __init__(self, song, artist, next=None):
          self.song = song
          self.artist = artist
          self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

#                        current.next: Dreams -> current.next = Lovely Day
#                        current: Simple Twist  -> current = Lovely Day
#                           |
# ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Dreams', 'Fleetwood Mac') -> ('Lovely Day', 'Bill Withers')
#                           |
#                         current.next(Dreams) = current.next.next(Lovely Day)
#                           ---------------------------------------------------------------> ('Lovely Day', 'Bill Withers')

# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None

    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    
    while current and current.next:
        
        if current.next.song == song:
        
            current.next = current.next.next
            current = current.next
            
        else:
            current = current.next
        
        print(f"{current.song}")

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))