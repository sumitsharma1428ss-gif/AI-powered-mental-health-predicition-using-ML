import pandas as pd
import random

data = []

for _ in range(500):   # 500 records = good dataset size
    sleep = random.randint(3, 9)
    stress = random.randint(1, 5)
    mood = random.randint(1, 5)
    sleep_quality = random.randint(1, 5)
    activity = random.randint(1, 5)
    screen_time = random.randint(1, 10)
    social = random.randint(1, 5)
    pressure = random.randint(1, 5)

    # 🔥 Target logic (mental health risk)
    risk_score = (
        (9 - sleep) +
        stress * 1.5 +
        (5 - mood) +
        (5 - sleep_quality) +
        (5 - activity) +
        screen_time * 0.8 +
        (5 - social) +
        pressure * 1.2
    )

    mental_health = 1 if risk_score > 18 else 0

    data.append([
        sleep, stress, mood, sleep_quality,
        activity, screen_time, social,
        pressure, mental_health
    ])

df = pd.DataFrame(data, columns=[
    "sleep_hours",
    "stress_level",
    "mood",
    "sleep_quality",
    "activity",
    "screen_time",
    "social",
    "pressure",
    "mental_health"
])

df.to_csv("dataset/mental_health.csv", index=False)

print("✅ Upgraded dataset generated successfully")
