def score_output(content):

    score = 0

    if "reel" in str(content).lower():
        score += 20

    if "hashtags" in str(content).lower():
        score += 20

    if "strategy" in str(content).lower():
        score += 30

    if len(str(content)) > 500:
        score += 30

    return min(score, 100)