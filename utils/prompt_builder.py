def get_business_prompt(business):
    
    if "Bakery" in business or "Food" in business:
        return """
        Focus on:
        - Visual appeal (aesthetic photos, reels)
        - Emotional triggers (cravings, freshness)
        - Offers and combos
        - Instagram reels & trending food content
        Tone: Warm, mouth-watering, engaging
        """

    elif "Salon" in business or "Beauty" in business:
        return """
        Focus on:
        - Before/After transformation
        - Client testimonials
        - Personal branding
        - Trust and hygiene
        Tone: Elegant, confident, premium
        """

    elif "Education" in business or "Coaching" in business:
        return """
        Focus on:
        - Value-based content
        - Tips, tricks, learning hacks
        - Problem-solving
        - Trust building
        Tone: Informative, helpful, clear
        """

    elif "Clothing" in business or "Fashion" in business:
        return """
        Focus on:
        - Trends and styling tips
        - Influencer-style content
        - Visual storytelling
        - Seasonal fashion
        Tone: Trendy, stylish, bold
        """

    elif "Fitness" in business:
        return """
        Focus on:
        - Motivation and transformation
        - Workout tips
        - Discipline and consistency
        Tone: Energetic, motivational
        """

    elif "Freelancer" in business:
        return """
        Focus on:
        - Portfolio showcasing
        - Client results
        - Case studies
        Tone: Professional, result-oriented
        """

    else:
        return """
        Focus on:
        - General business growth
        - Customer engagement
        Tone: Balanced and practical
        """
def get_budget_prompt(budget):

    if budget == "Low":
        return """
        Budget Level: LOW

        Focus on:
        - Organic growth only
        - Reels, trends, hashtags
        - No paid ads
        - DIY content creation
        - Engagement hacks
        """

    elif budget == "Medium":
        return """
        Budget Level: MEDIUM

        Focus on:
        - Mix of organic + small paid ads
        - Boosted posts
        - Micro influencer collaborations
        - Consistent posting strategy
        """

    elif budget == "High":
        return """
        Budget Level: HIGH

        Focus on:
        - Paid ads strategy
        - Professional content production
        - Influencer marketing
        - Brand positioning
        - Funnel optimization
        """

    else:
        return "Budget not specified"