# Write a Python program that generates a list of Pythagorean triplets (a, b, c) from a given list of integers, using lambda, filter(), and map(). The program should filter out invalid triplets and display valid ones.
def is_pythagorean_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2

def generate_triplets(nums):
    triplets = map(lambda triplet: triplet, [(a, b, c) for a in nums for b in nums for c in nums if a < b < c])
 
    valid_triplets = filter(lambda triplet: is_pythagorean_triplet(triplet), triplets)
    
    return list(valid_triplets)

nums = [3, 4, 5, 6, 8, 10, 12, 15, 20]
pythagorean_triplets = generate_triplets(nums)
print("Valid Pythagorean Triplets:", pythagorean_triplets)
