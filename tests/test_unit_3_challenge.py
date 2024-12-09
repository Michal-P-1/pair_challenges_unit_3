import datetime
# from dateutil import relativedelta
from lib.unit_3_challenge import allow_access

def test_age_calculation():
    assert allow_access("2006-12-12") == "No access. Your current age is 18 and the required age is 16"