import datetime

year_birth = int(input("What year you was born: "))
month_birth = int(input("What month you were born: : "))
day_birth = int(input("What day you were born: "))
hour_birth = int(input("Type the your hour you were born (in 24 hours format): "))

birth_date = datetime.datetime(year_birth, month_birth, day_birth, hour_birth)

atual_date = datetime.datetime.now()

difference_in_seconds = (atual_date - birth_date).total_seconds()

days_lived = int(difference_in_seconds / 86400)
months_lived = days_lived // 30
years_lived = months_lived // 12

print(f"You have lived {years_lived} years, {months_lived % 12} months and {days_lived % 30} days.")

print("Think about enjoying or least improving the time you have here and add love to this world.")
