orders = [
    {"id": 1, "user": "anna", "amount": 120.5, "status": "paid"},
    {"id": 2, "user": "boris", "amount": 80.0, "status": "cancelled"},
    {"id": 3, "user": "anna", "amount": 40.0, "status": "paid"},
    {"id": 4, "user": "clara", "amount": 300.0, "status": "paid"},
    {"id": 5, "user": "boris", "amount": 55.0, "status": "paid"},
]
def top_users(orders: list[dict], n: int) -> list[tuple[str, float]]:
    totals = {}
    for order in orders:
        if order["status"] == "paid":
            user = order["user"]
            totals[user] = totals.get(user, 0) + order["amount"]
    ranked = sorted(totals.items(), key=lambda pair: pair[1], reverse=True)
    return ranked[:n]
assert top_users(orders, 2) == [('clara', 300.0), ('anna', 160.5)]
assert top_users(orders, 3) == [('clara', 300.0), ('anna', 160.5), ('boris', 55.0)]
assert top_users(orders, 4) == [('clara', 300.0), ('anna', 160.5), ('boris', 55.0)]
assert top_users([], 3) == []



def summarize_by_status(orders: list[dict]) -> dict[str, dict]:
    results = {}
    for order in orders:
        status = order["status"]
        if status not in results:
            results[status] = {"count": 0, "total": 0}
        results[status]["count"] += 1 
        results[status]["total"] += order["amount"]
    return results
assert summarize_by_status(orders) == {
    "paid": {"count": 4, "total": 515.5},
    "cancelled": {"count": 1, "total": 80.0}
    }
assert summarize_by_status([]) == {}



def average(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Список не должен быть пустым")
    return sum(nums) / len(nums)
try:
    average([])
    assert False, "Ждали ValueError"
except ValueError:
    pass
assert average([4, 5, 6, 12]) == 6.75



def count_words(text: str) -> dict[str, int]:
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
assert count_words("кот пёс кот") == {'кот': 2, 'пёс': 1}
assert count_words("") == {}



def sort_by_length(words: list[str]) -> list[str]:
    sorted_list = sorted(words, key=lambda x: len(x))#лучше писать sorted(words, key=len)
    return sorted_list
assert sort_by_length(["pear", "fig", "apple"]) == ["fig", "pear", "apple"]
assert sort_by_length([]) == []
assert sort_by_length(["egg", "key", "abc"]) == ["egg", "key", "abc"]



def oldest_names(people: list[dict], n: int) -> list[str]:
    sorted_list = sorted(people, key=lambda person: person["age"], reverse=True)
    names = [p["name"] for p in sorted_list]
    return names[:n]
people = [{"name": "anna", "age": 25}, {"name": "boris", "age": 40}, {"name": "clara", "age": 31},{"name": "dima", "age": 19},]
assert oldest_names(people, 2) == ['boris', 'clara']
assert oldest_names([], 3) == []
assert oldest_names(people, 10) == ['boris', 'clara', 'anna', 'dima']



def rank_students(students: list[tuple[str, int]]) -> list[tuple[str, int]]:
    sorted_list = sorted(students, key=lambda s: (-s[1], s[0]))
    return sorted_list
ranking = [("bob", 90), ("dima", 70), ("anna", 90)]
assert rank_students(ranking) == [("anna", 90), ("bob", 90), ("dima", 70)]
assert rank_students([]) == []
assert rank_students([("bob", 90), ("dima", 90), ("anna", 90)]) == [("anna", 90), ("bob", 90), ("dima", 90)]



def min_max(nums: list[int]) -> tuple[int, int]:
    if not nums:
        raise ValueError("Список не должен быть пустым")
    smallest = nums[0]
    biggest = nums[0]
    for num in nums[1:]:
        if num > biggest:
            biggest = num
        elif num < smallest:
            smallest = num
    return smallest, biggest
assert min_max([3, 1, 4]) == (1, 4)
assert min_max([5]) == (5, 5)
try:
    min_max([])
    assert False, "Ждали ValueError"
except ValueError:
    pass



def split_by_sign(nums: list[int]) -> tuple[list[int], list[int]]:
    neg = []
    rest = []
    for num in nums:
        if num < 0:
            neg.append(num)
        else:
            rest.append(num)
    return neg, rest
assert split_by_sign([-1, 0, 5, -3]) == ([-1, -3], [0, 5])
assert split_by_sign([]) == ([], [])



def group_by_user(orders: list[dict]) -> dict[str, list[dict]]:
    groups = {}
    for order in orders: 
        key = order["user"]
        if key not in groups:
            groups[key] = []
        groups[key].append(order)
    return groups
assert group_by_user([
    {"id": 1, "user": "anna", "amount": 120.5},
    {"id": 2, "user": "boris", "amount": 80.0},
    {"id": 3, "user": "anna", "amount": 40.0},
]) == {
    "anna": [
        {"id": 1, "user": "anna", "amount": 120.5},
        {"id": 3, "user": "anna", "amount": 40.0},
    ],
    "boris": [
        {"id": 2, "user": "boris", "amount": 80.0},
    ],
}
assert group_by_user([]) == {}
assert group_by_user([
    {"id": 1, "user": "anna", "amount": 120.5},
    {"id": 2, "user": "anna", "amount": 80.0},
    {"id": 3, "user": "anna", "amount": 40.0},
]) == {
    "anna": [
        {"id": 1, "user": "anna", "amount": 120.5},
        {"id": 2, "user": "anna", "amount": 80.0},
        {"id": 3, "user": "anna", "amount": 40.0},
    ],
}



def find_duplicates(nums: list[int]) -> list[int]:
    counts = {}
    duplicates = []
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    for key, value in counts.items():
        if value >= 2:
            duplicates.append(key)
    d = sorted(duplicates)
    return d
assert find_duplicates([1, 2, 2, 3, 3, 3]) == [2, 3]
assert find_duplicates([1, 2, 3]) == []
assert find_duplicates([]) == []



def merge_stats(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    result = a.copy()
    for key, value in b.items():
        result[key] = result.get(key, 0) + value
    return result
assert merge_stats({"x": 1, "y": 2}, {"y": 3, "z": 4}) == {'x': 1, 'y': 5, 'z': 4}
assert merge_stats({}, {"y": 3, "z": 4}) == {"y": 3, "z": 4}
assert merge_stats({}, {}) == {}



def remove_evens(nums: list[int]) -> list[int]:
    return [x for x in nums if x % 2 != 0]
assert remove_evens([2, 5, 4, 7, 32]) == [5, 7]
assert remove_evens([2, 4, 6, 8, 10]) == []
assert remove_evens([3, 5, 7, 9]) == [3, 5, 7, 9]



def word_stats(text: str) -> dict:
    result = {}
    counts = {}
    words = text.lower().split()
    result["total"] = len(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    result["unique"] = len(counts)
    sorted_list = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    result["top"] = sorted_list[:3]
    return result
text = "the cat and the dog and the bird"
assert word_stats(text) == {"total": 8, "unique": 5, "top": [("the", 3), ("and", 2), ("bird", 1)]}
assert word_stats("") == {"total": 0, "unique": 0, "top": []}
assert word_stats("a a b") == {"total": 3, "unique": 2, "top": [("a", 2), ("b", 1)]}