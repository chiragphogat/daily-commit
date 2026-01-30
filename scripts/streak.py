import os

count = len(os.listdir("logs"))

readme = f"""# Daily Learning Tracker 🚀

🔥 **Current Streak:** {count} days

## Badges
![Consistency](https://img.shields.io/badge/Consistency-Strong-green)

> Building habits, one day at a time.
"""

with open("README.md", "w") as f:
    f.write(readme)
