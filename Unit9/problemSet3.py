# Problem 1

#def are_equivalent(word1, word2):
   #word1 = "".join(word1)
   #word2 = "".join(word2)
   #return word1 == word2

#word1 = ["bat", "man"]
#word2 = ["b", "atman"]
#print(are_equivalent(word1, word2))

#word1 = ["alfred", "pennyworth"]
#word2 = ["alfredpenny", "word"]
#print(are_equivalent(word1, word2))

#word1  = ["cat", "wom", "an"]
#word2 = ["catwoman"]
#print(are_equivalent(word1, word2))

# Problem 2

#def countEven(lst):
    #counter = 0
    #for word in lst:
        #if len(word) % 2 == 0:
            #counter += 1
    #return counter

#lst = ["na", "nana", "nanana", "batman", "!"]
#print(countEven(lst))

#lst = ["the", "joker", "robin"]
#print(countEven(lst))

#lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
#print(countEven(lst))

#def remove_name(people, secret_identity):
	#index = 0 
	#for person in people:
		#if person == secret_identity:
			#people.pop(index)
		#index += 1
	#return people

#people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
#secret_identity = 'Bruce Wayne'
#print(remove_name(people, secret_identity))

#def count_digits(n):
    #if n == 0: return 1 
    #counter = 0
    #while n != 0:
        #counter += 1
        #n = n // 10
    #return counter

#print(count_digits(9644))
#print(count_digits(0))

#def move_zeroes(lst):
    #result = []
    #zeroCount = 0 
    #for num in lst:
        #if num != 0:
            #result.append(num)
        #else:
            #zeroCount += 1
    #while zeroCount != 0:
        #result.append(0)
        #zeroCount -= 1
    #return result
    
#lst = [1, 0, 2, 0, 3, 0]
#print(move_zeroes(lst))

#def reverse_vowels(s):
    #vowels = []
    #for char in s:
        #if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            #vowels.append(char)

    #vowels = vowels[::-1]
    #result = []
    #vowel_index = 0

    #for char in s:
        #if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            #result.append(vowels[vowel_index])
            #vowel_index += 1
        #else:
            #result.append(char)
    #return ''.join(result)

#def highest_altitude(gain):
    #max_altitude = 0
    #current_altitude = 0
    #for g in gain:
        #current_altitude += g
        #if current_altitude > max_altitude:
            #max_altitude = current_altitude
    #return max_altitude

#def left_right_difference(nums):
    #n = len(nums)
    #left_sums = [0] * n
    #right_sums = [0] * n
    #answer = [0] * n
    
    #for i in range(1, n):
        #left_sums[i] = left_sums[i-1] + nums[i-1]
    
    #for i in range(n-2, -1, -1):
        #right_sums[i] = right_sums[i+1] + nums[i+1]
    
    #for i in range(n):
        #answer[i] = left_sums[i] - right_sums[i]
    
    #return answer

#def common_elements(lst1, lst2):
    #result = []

    #for n in lst1:
        #if n in lst2:
            #result.append(n)
    #return result

#print(common_elements(["super strength", "super speed", "x-ray vision"], ["super speed", "time travel", "dimensional travel"]))

#def expose_superman(trust, n):
    #trust_counts = [0] * (n + 1)  # Index 0 is unused, citizens are 1..n
    #trusts_someone = [False] * (n + 1)
    
    #for a, b in trust:
        #trusts_someone[a] = True
        #trust_counts[b] += 1
    
    #superman_candidates = []
    #for i in range(1, n + 1):
        #if not trusts_someone[i] and trust_counts[i] == n - 1:
            #superman_candidates.append(i)
    
    #if len(superman_candidates) == 1:
        #return superman_candidates[0]
    #else:
        #return -1
