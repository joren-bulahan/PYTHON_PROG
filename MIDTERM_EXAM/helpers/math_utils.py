def area(l: float, w: float) -> float:
    """Return the area of a rectangle given length and width."""
    if l < 0 or w < 0:
        raise ValueError("Dimensions must be non-negative.")
    return l * w