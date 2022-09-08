""" Some tender, loving functions."""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string"""
    return f"I love you {subject}!"

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    count: int = 0
    while count < n:
        love_note += love(to) + "\n"
        count += 1
    return love_note

print(spread_love("Mom", 100))