def outdated():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        try:
            user_input = input("Date: ")

            if len(user_input.split("/")) == 3:
                month, date, year = user_input.split("/")
                month, date, year = int(month), int(date), int(year)
                if month >= 1 and month <=12 and date >=1 and date <= 31:
                    print(f"{year}-{month:02}-{date:02}")
                    break

            if "," in user_input:
                months_dates = user_input.split(",")
                month_date = months_dates[0].strip()
                year = months_dates[1].strip()
                month, date = month_date.split(" ")
                date, year = int(date), int(year)
                if date >= 1 and date <=31:
                    if month in months:
                        index = int(months.index(month)) +1
                        print(f"{year}-{index:02}-{date:02}")
                    break


        except ValueError:
            continue

outdated()