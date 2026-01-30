from datetime import date
import random
import os

topics = {
    "DSA": [
        "Solved array manipulation problem",
        "Practiced binary search variants",
        "Reviewed time complexity patterns"
    ],
    "System Design": [
        "Read about scalability principles",
        "Studied load balancers and caching",
        "Explored high-level architecture patterns"
    ],
    "Python": [
        "Worked with list comprehensions",
        "Revisited decorators and generators",
        "Practiced clean code patterns"
    ],
    "Git": [
        "Reviewed git rebase vs merge",
        "Practiced resolving merge conflicts",
        "Explored GitHub Actions basics"
    ]
}

topic = random.choice(list(topics.keys()))
content = random.choice(topics[topic])

today = date.today().isoformat()
os.makedirs("logs", exist_ok=True)

with open(f"logs/{today}.md", "w") as f:
    f.write(f"# {today}\n")
    f.write(f"**Topic:** {topic}\n\n")
    f.write(f"- {content}\n")
