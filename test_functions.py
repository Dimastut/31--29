import pytest
from functions import add, get_user_full_name, divide, is_valid_password
# from pytest import markers 
@pytest.mark.math
def test_add():
 assert add(2, 3) == 5
 assert add(2, 2) == 4
 assert add(10, -5) == 5
 
@pytest.mark.user_profile
def test_get_user_full_name():
 user = {
 "first_name": "Dima",
 "last_name": "Vlasov",
 "email": "dimka.vlasov.452@gmail.com"
 }
 assert get_user_full_name(user) == "Dima Vlasov"


@pytest.mark.user_profile
def test_user_has_email():
 user = {
 "first_name": "Dima",
 "last_name": "Vlasov",
 "email": "dimka.vlasov.452@gmail.com"
 }
 assert "email" in user


@pytest.fixture
def sample_user_data():
  return {
 "first_name": "Dima",
 "last_name": "Vlasov",
 "email": "dimka.vlasov.452@gmail.com"
 }
@pytest.mark.user_profile
def test_get_user_full_name_with_fixture(sample_user_data: dict[str, str]):
 assert get_user_full_name(sample_user_data) == "Dima Vlasov"
@pytest.mark.user_profile
def test_user_has_email_with_fixture(sample_user_data: dict[str, str]):
 assert "email" in sample_user_data

 
test_cases = [
 (1, 2, 3), # Обычное сложение
 (-1, -1, -2), # Сложение отрицательных чисел
 (5, 0, 5), # Сложение с нулем
 (-1, 1, 0), # Противоположные числа
 (3.5, 2.5, 6.0) # Сложение чисел с плавающей точкой
]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
 assert add(a, b) == expected


from functions import divide
def test_divide_by_zero_raises_error():
 with pytest.raises(ValueError):
  (divide(10, 0))

@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
# Код теста для новой, еще не готовой функции
 assert False

@pytest.mark.xfail(reason="Известный точностью float, тикет #123")
def test_float_precision_bug():
  assert (0.1 + 0.2) == 0.3 

def test_password_valid():
 password = "1234567890"
 result = is_valid_password(password)
 assert result == True


def test_password_too_short():
  password = "12345"
  result =  is_valid_password(password)
  assert result == False


def test_password_boundary ():
   password = "12345678"
   result =  is_valid_password(password)
   assert result == True

