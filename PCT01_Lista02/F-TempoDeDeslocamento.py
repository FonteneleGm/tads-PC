Distance = int(input())
Speed = int(input())
TimeInHours = Distance / Speed
Hours = int(TimeInHours)
Minutes = int((TimeInHours - Hours) * 60)
print(f"{Hours:02d}:{Minutes:02d}")

