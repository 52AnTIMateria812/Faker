import time
from functools import wraps

def timer(func):
    """Декоратор для замера времени выполнения"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️  Время генерации: {elapsed:.6f} секунд")
        return result
    return wrapper

def print_separator(title=""):
    """Удобный разделитель для секций"""
    print("\n" + "=" * 50)
    if title:
        print(f"🔹 {title}")
        print("=" * 50)
