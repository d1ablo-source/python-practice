def validate_order(order: dict) -> None:
    for key in ("id", "user", "amount", "status"):
        if key not in order:
            raise ValueError(f"Нет ключа {key}")
    if not isinstance(order["amount"], (int, float)) or order["amount"] <= 0:
        raise ValueError("Нужно положительное число")
    if order["status"] not in ("paid", "cancelled", "pending"):
        raise ValueError("Некорректный статус")
    
def split_orders(orders: list[dict]) -> tuple[list[dict], list[dict]]:
    valid = []
    invalid = []
    for order in orders:       
        try:
            validate_order(order)
            valid.append(order)
        except ValueError:
            invalid.append(order)
    return valid, invalid

good = {"id": 1, "user": "anna", "amount": 120.5, "status": "paid"}
no_amount = {"id": 2, "user": "boris", "status": "paid"}
bad_amonut = {"id": 3, "user": "clara", "amount": -10, "status": "paid"}
assert split_orders([good, no_amount, bad_amonut]) == ([good], [no_amount, bad_amonut])



def safe_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None
assert safe_int("42") == 42
assert safe_int("  8  ") == 8
assert safe_int("asd") == None



def parse_ages(raw: list[str]) -> tuple[list[int], list[str]]:
    right = []
    invalid = []
    for item in raw:
        if safe_int(item) is not None and 0 <= safe_int(item) <= 120:
            right.append(safe_int(item))
        else:
            invalid.append(item)
    return right, invalid
assert parse_ages(["25", "abc", "130", "7", "0"]) == ([25, 7, 0], ["abc", "130"])
assert parse_ages([]) == ([], [])
assert parse_ages(["12", "31", "120"]) == ([12, 31, 120], [])



def is_valid_username(name: str) -> bool:
    allowed = "1234567890qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё_"#i.isalnum()
    if not (3 <= len(name) <= 16) or name[0].isdigit():
        return False
    for i in name.lower():#i.isalnum()
        if i not in allowed:
            return False
    return True
assert is_valid_username("123qwerty") == False
assert is_valid_username("_qwerty123") == True
assert is_valid_username("QwEr_ty_123") == True
assert is_valid_username("qwetertyuioasd____") == False
assert is_valid_username("") == False
assert is_valid_username("user-name") == False    # дефис
assert is_valid_username("user name") == False    # пробел
assert is_valid_username("ab") == False