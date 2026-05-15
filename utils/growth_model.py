def predict_growth(business, platform, goal, budget, audience):

    # Base score
    score = 50

    # PLATFORM impact
    if platform == "Instagram":
        score += 15
    elif platform == "YouTube":
        score += 20
    elif platform == "WhatsApp":
        score += 10
    else:
        score += 5

    # BUDGET impact
    if budget == "Low":
        score += 5
    elif budget == "Medium":
        score += 15
    elif budget == "High":
        score += 25

    # BUSINESS TYPE impact
    if "Digital Creator" in business:
        score += 20
    elif "Food" in business:
        score += 15
    elif "Education" in business:
        score += 10

    # GOAL impact
    if goal == "Increase Followers":
        score += 10
    elif goal == "Increase Sales":
        score += 15

    # Clamp score
    if score > 100:
        score = 100

    # Prediction logic
    if score >= 80:
        level = "🔥 High Growth Potential"
        followers_min = 5000
        followers_max = 20000
        time_months = 1
    elif score >= 60:
        level = "📈 Medium Growth Potential"
        followers_min = 1000
        followers_max = 5000
        time_months = 2
    else:
        level = "⚠️ Slow Growth"
        followers_min = 0
        followers_max = 1000
        time_months = 3

    return {
        "score": score,
        "level": level,
        "followers_min": followers_min,
        "followers_max": followers_max,
        "time_months": time_months
    }