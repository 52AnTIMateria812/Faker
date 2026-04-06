from core import generate_profile, generate_address, generate_company_info, generate_credit_card
from utils import timer, print_separator

@timer
def demo_profile(count=1):
    """Демонстрация генерации профилей"""
    print_separator("Генерация профилей пользователей")
    for i in range(count):
        profile = generate_profile()
        print(f"Имя: {profile['name']}")
        print(f"Пол: {'Мужской' if profile['sex'] == 'M' else 'Женский'}")
        print(f"Дата рождения: {profile['birthdate']}")
        print("-" * 25)

@timer
def demo_address(count=3):
    """Демонстрация генерации случайных адресов"""
    print_separator("Генерация случайных адресов")
    for i in range(count):
        print(f"🏠 Адрес {i+1}: {generate_address()}")

@timer
def demo_company(count=2):
    """Демонстрация генерации данных о компаниях"""
    print_separator("Генерация данных о компаниях")
    for i in range(count):
        info = generate_company_info()
        print(f"🏢 Компания: {info['company']}")
        print(f"💼 Должность: {info['job']}")
        print(f"📣 Слоган: {info['catch_phrase']}\n")

@timer
def demo_credit_card(count=2):
    """Демонстрация генерации кредитных карт"""
    print_separator("Генерация данных кредитных карт (Fictional)")
    for i in range(count):
        card = generate_credit_card()
        print(f"💳 Провайдер: {card['provider']}")
        print(f"🔢 Номер: {card['number']}")
        print(f"📅 Срок: {card['expire']}")
        print(f"🔒 CVC: {card['security_code']}\n")
