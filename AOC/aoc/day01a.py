"""Häid jõule."""


def distance_between_lists(tuples):
    """Check the distance between list elements."""
    # Sort the numbers
    first_parts = sorted([t[0] for t in tuples])
    second_parts = sorted([t[1] for t in tuples])
    # Get the abs distances per object summed
    total_distance = sum(abs(left - right) for left, right in zip(first_parts, second_parts))
    return total_distance
