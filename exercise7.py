from datetime import date

day_today = date.today().strftime("%A %d %B %Y")
print(day_today)
day = str(input("Enter todays day:"))
if day == day_today:
    print(f"Today is{day_today} /ncorrect")
elif day != day_today:
    print("Your answer is incorrect!/n..Enter correct day/n:")

