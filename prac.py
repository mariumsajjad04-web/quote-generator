import random

def random_quote():
    quotes = [
        "Life is what happens when you're busy making other plans.",
        "The only way to do great work is to love what you do.",
        "In the middle of difficulty lies opportunity."
    ]
    print(random.choice(quotes))

random_quote()
