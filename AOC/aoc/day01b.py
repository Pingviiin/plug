"""Häid jõule."""
from collections import Counter


def similarity_score(tuples):
    """Return the similarity of two tuples."""
    # Make a counter map of the right part
    rights_counts = Counter([t[0] for t in tuples])

    # Sum for everything in left part the number * count
    score = sum(num * rights_counts[num] for num in [t[1] for t in tuples])
    return score
