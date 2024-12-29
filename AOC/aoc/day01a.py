from collections import Counter

def distance_between_lists(tuples):
    # Sort the numbers
    first_parts = sorted([t[0] for t in tuples])
    second_parts = sorted([t[1] for t in tuples])
    # Get the abs distances per object summed
    total_distance = sum(abs(l - r) for l, r in zip(first_parts, second_parts))
    return total_distance

def similarity_score(tuples):
    # Make a counter map of the right part
    rights_counts = Counter([t[0] for t in tuples])

    # Sum for everything in left part the number * count
    score = sum(num * rights_counts[num] for num in [t[1] for t in tuples])
    return score


with open(r'iti0102-2024\AOC\aoc\input.txt') as f:
    lines = f.read().splitlines()
    tuples_list = [tuple(map(int, item.split())) for item in lines]

print("Part 1, distance of two lists is",distance_between_lists(tuples_list))
print("Part 2, similarity score of two lists is",similarity_score(tuples_list))
