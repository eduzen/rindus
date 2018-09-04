import pytest
from faker import Faker

from crud.forms import UserProfileForm


def test_valid_iban():
    fake = Faker()
    form_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "iban": "AL35202111090000000001234567"
    }
    user_form = UserProfileForm(data=form_data)
    assert user_form.is_valid()


@pytest.mark.parametrize("iban", ("1.0", "1", 1, "abc.01", "AL3520211109000000000123456", True))
def test_invalid_iban(iban):
    fake = Faker()
    form_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "iban": iban
    }
    user_form = UserProfileForm(data=form_data)
    assert not user_form.is_valid()
