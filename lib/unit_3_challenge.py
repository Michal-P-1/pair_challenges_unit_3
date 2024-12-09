import datetime
from dateutil import relativedelta

def allow_access(date_of_birth):
    example_date_list = date_of_birth.split("-")
    date_year = int(example_date_list[0])
    date_month = int(example_date_list[1])
    date_day = int(example_date_list[2])
    current_date = datetime.date.today()

    user_date_of_birth = datetime.date(date_year, date_month, date_day)
    age = relativedelta.relativedelta(current_date , user_date_of_birth)

    if age < 16:
        return f"No access. Your current age is {age} and the required age is 16"
    else:
        return "Access allowed"

allow_access("2020-01-12")