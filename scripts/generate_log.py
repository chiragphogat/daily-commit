from datetime import datetime
import os
import random

today = datetime.now().strftime("%Y-%m-%d")

os.makedirs("logs", exist_ok=True)

thoughts = [
    "Consistency compounds quietly.",
    "Small progress is still progress.",
    "Discipline beats motivation.",
    "Focus on systems, not goals.",
    "Learning never goes to waste."
]

focus = [
    "Problem solving",
    "Code readability",
    "Fundamentals",
    "Consistency",
    "Logical thinking"
]

content = f"""# Daily Log — {today}

## Focus
- {random.choice(focus)}

## Thought of the day
> "{random.choice(thoughts)}"
"""

with open(f"logs/{today}.md", "w") as f:
    f.write(content)

# Update README stats
with open("README.md", "w") as f:
    f.write(f"""# 📆 Daily Learning Tracker

This repository tracks my daily learning habit using automation.

## 📊 Stats
- 🟢 Last update: {today}
- ⏰ Runs daily at 12:00 PM IST
- ⚙️ Powered by GitHub Actions + Python

## Why this exists
Consistency matters more than intensity.
Some days are deep work, some are reflection —
but never zero progress.
""")
