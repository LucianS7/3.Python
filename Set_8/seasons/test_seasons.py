import pytest
from datetime import date
from seasons import age_in_minutes, get_birth_date


def main():
    test_correct_dob_format()
    test_incorrect_dob_format()
    test_age_in_minutes()


def test_correct_dob_format():
    assert get_birth_date("1990-05-05") == date(1990, 5 , 5)
    assert get_birth_date("1980-12-30") == date(1980, 12 , 30)


def test_incorrect_dob_format():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_birth_date("2024-05-05")
        get_birth_date("1990-15-12")
        get_birth_date("1990-05-32")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Invalid date"


def test_age_in_minutes():
    assert age_in_minutes(date.fromisoformat("1990-05-05")) == 17316000
    today = date.today()
    assert age_in_minutes(date(today.year - 1, today.month, today.day)) == 525600
    assert age_in_minutes(date(today.year - 2, today.month, today.day)) == 1051200