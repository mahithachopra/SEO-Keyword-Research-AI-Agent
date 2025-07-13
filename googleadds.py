import random

def get_keyword_metrics(keyword):
    return {
        "keyword": keyword,
        "volume": random.randint(1000, 20000),
        "competition": round(random.uniform(0.1, 0.9), 2)
    }
