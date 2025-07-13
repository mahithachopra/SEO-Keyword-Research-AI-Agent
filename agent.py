import random

def expand_keywords(seed):
    modifiers = [
        "2024", "remote", "paid", "summer", "for students", "without experience",
        "with visa", "USA", "Canada", "Europe", "program", "portal", "deadline",
        "opportunities", "application", "requirements", "intern", "virtual", "online"
    ]

    keywords = []
    for mod1 in modifiers:
        for mod2 in modifiers:
            if mod1 != mod2:
                keywords.append(f"{seed} {mod1} {mod2}")

    random.shuffle(keywords)
    return list(set(keywords))[:200]  # return 200 unique keywords
