from datetime import date
import os

# Only run on Sunday
if date.today().weekday() != 6:
    exit(0)

files = sorted(os.listdir("logs"))[-7:]

summary = "# Weekly Learning Summary\n\n"
for file in files:
    summary += f"- {file.replace('.md','')}\n"

with open("WEEKLY_SUMMARY.md", "w") as f:
    f.write(summary)
