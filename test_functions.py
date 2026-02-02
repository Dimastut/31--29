import pytest
from functions import add, get_user_full_name
def test_add():
 assert add(2, 3) == 5
 assert add(2, 2) == 4
 assert add(10, -5) == 5
 

def test_get_user_full_name():
 user = {
 "first_name": "Dima",
 "last_name": "Vlasov",
 "email": "dimka.vlasov.452@gmail.com"
 }
 assert get_user_full_name(user) == "Dima Vlasov"
6
def test_user_has_email():
 user = {
 "first_name": "Dima",
 "last_name": "Vlasov",
 "email": "dimka.vlasov.452@gmail.com"
 }
 assert "email" in user

# ШАГ 1: Создаем фикстуру
@pytest.fixture
def sample_user_data():
 """Фикстура, которая возвращает словарь с данными пользователя."""
 return {
 "first_name": "Dima",
 "last_name": "Vlasov",
 "email": "dimka.vlasov.452@gmail.com"
 }
def test_get_user_full_name_with_fixture(sample_user_data: dict[str, str]):
 assert get_user_full_name(sample_user_data) == "Dima Vlasov"
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