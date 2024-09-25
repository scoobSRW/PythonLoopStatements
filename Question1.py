import random

emotions = ["Happy", "Sad", "Energetic", "Calm",]

days_of_week = ["Monday", "Tuesday",
                "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    mood = random.choice(emotions)
    print(f"On {day}, you were feeling {mood}.")
