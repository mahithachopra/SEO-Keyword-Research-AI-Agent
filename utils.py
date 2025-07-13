def score_keywords(keywords_data):
    for k in keywords_data:
        k["score"] = k["volume"] / (k["competition"] + 1)
    sorted_kw = sorted(keywords_data, key=lambda x: x["score"], reverse=True)
    return sorted_kw[:50]
