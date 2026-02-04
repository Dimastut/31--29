def add(x, y):
     return x + y

def get_user_full_name(user_data):
 first_name = user_data.get("first_name", "")
 last_name = user_data.get("last_name", "")
 return f"{first_name} {last_name}".strip()

def divide(a, b):
 """Делит число a на b."""
 if b == 0:
    raise ValueError("Деление на ноль невозможно")
 return a / b

def is_valid_password(password: str) -> bool:
 return len(password) >= 8
def test_password_too_short(password:str) -> bool:
  return len(password)>= 5
def test_password_boundary(password: str)-> bool:
  return len(password)>= 8