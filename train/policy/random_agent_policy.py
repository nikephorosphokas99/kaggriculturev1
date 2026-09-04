import random

FARMER_OPS = ["NORTH", "SOUTH", "EAST", "WEST", "PASS", "WATER", "HARVEST", "FERTILIZE", "DIG"]
CROPS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON"]


def _random_farmer_action():
    op = random.choice(FARMER_OPS)
    return [op]


def agent(observation):
    player = observation["player"]
    me = observation["farms"][player]
    hands = me.get("hands", [])

    farmer_action = _random_farmer_action()
    hand_actions = [_random_farmer_action() for _ in hands]

    market_actions = []
    if me["money"] >= 10 and random.random() < 0.05:
        market_actions.append(["BUY_SEED", random.choice(CROPS), 1])

    return {
        "farmer": farmer_action,
        "hands": hand_actions,
        "market": market_actions,
    }
