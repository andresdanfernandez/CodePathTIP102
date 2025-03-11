"""
Problem 1: Calculating Village Size

In the kingdom of Codepathia, the queen determines how many resources to distribute to a village based on its class. A village's class is equal to the number of digits in its population. Given an integer population, write a function get_village_class() that returns the number of digits in population.

Implement the solution iteratively.

Implement the solution recursively.

Discuss: what are the similarities between the two solutions? What are the differences?
def get_village_class_iterative(population):
    pass

Example Usage:

print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))
Example Output:

3
3
1
1
"""

# Understand: We are given an int we want to get the length of the digit example '432' -> 3. Do we have to convert from int to string? How do we handle negative ints? Avoid using len()

# Match:

# Plan: 
# [Iterative] Convert digit to string then iterate through chars till we reach end, keep track of "length" using a counter
# [Recursive] Base case: When list is empty we reached the end | Return condition: 1 + recursive(population[1:])

# [432] -> population[1:] -> [32] -> population[1:] -> 2 -> population[1:] -> []

'''
# iterative approach
def get_village_class_iterative(population):

    population = str(population)
    counter = 0

    for _ in population:
        counter += 1
    return counter
'''

# recursive approach
#def get_village_class_recursive(population):

    #population = str(population)!!!!!

   # if not population:
       # return 0

 #   return 1 + get_village_class_iterative(population[1:])


#Less cost approach

# recursive approach
def get_village_class_recursive(population):

    if population == 0:
        return 0

    return 1 + get_village_class_recursive(population // 10)
    

# iterative approach
def get_village_class_iterative(population):

    counter = 0

    while population // 10 != 0:
        counter += 1
        population = population // 10
    
    return counter


    # returning 1 + 1

# intitial call get_village_class_recursive(432) -> '432'

# get_village_class_iterative('32') = 1
# get_village_class_iterative('2') = 1 + 1
# get_village_class_iterative('') = 1 + 1 + 1 (3)

# get_village_class_iterative('')
# get_village_class_iterative('2')
# get_village_class_iterative('32')
# get_village_class_iterative('432')

print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))

# O Space # number of digs, O Time # of digits