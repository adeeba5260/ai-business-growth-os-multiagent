from agents.market import market_agent
from agents.audience import audience_agent
from agents.content import content_agent
from agents.strategy import strategy_agent
from agents.reels import reels_agent
from agents.refiner import content_refiner_agent   # ✅ FIXED IMPORT

from utils.memory import update_memory, get_memory
from utils.scoring import score_output
from utils.growth_model import predict_growth


def run_system(business, audience, age, location, platform, goal, budget):

    user_id = "default_user"

    # 🧠 MEMORY SYSTEM
    update_memory(user_id, "business", business)
    update_memory(user_id, "audience", audience)

    past_memory = get_memory(user_id)

    # 1. Market Analysis
    market = market_agent(business, audience, age, location, platform, past_memory)

    # 2. Audience Analysis
    audience_data = audience_agent(audience, age, location)

    # 3. CONTENT (v1)
    content_v1 = content_agent(business, audience_data, platform, budget)

    # 🔁 REFINEMENT LOOP
    content_v2 = content_refiner_agent(content_v1, market, audience_data)

    # 4. Reels
    reels = reels_agent(business, audience, age, location, platform)

    # 5. Strategy (uses refined content)
    strategy = strategy_agent(market, content_v2, goal, budget, business)

    # 📊 SCORE SYSTEM
    content_score = score_output(content_v2)
    growth = predict_growth(business, platform, goal, budget, audience)

    return {
    "market": market,
    "audience": audience_data,
    "content": content_v2,
    "reels": reels,
    "strategy": strategy,
    "score": content_score,
    "growth": growth
}