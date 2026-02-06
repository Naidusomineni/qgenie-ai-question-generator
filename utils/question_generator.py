import json
import random
import os

def load_questions():
    path = os.path.join("models", "sample_questions.json")

    with open(path, "r") as f:
        return json.load(f)


def generate_questions(topic):
    questions_data = load_questions()

    base = questions_data.get("default", [])
    topic_specific = questions_data.get(topic.lower(), [])

    all_questions = base + topic_specific

    random.shuffle(all_questions)

    return all_questions[:5]
