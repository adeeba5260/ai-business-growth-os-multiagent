import json
import os

MEMORY_FILE = "user_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_memory(user_id, key, value):
    memory = load_memory()

    if user_id not in memory:
        memory[user_id] = {}

    memory[user_id][key] = value
    save_memory(memory)

def get_memory(user_id):
    memory = load_memory()
    return memory.get(user_id, {})