from faker import Faker

# Инициализируем Faker с русской локалью
fake = Faker('ru_RU')

def generate_profile():
    """Генерация профиля пользователя"""
    return fake.profile()

def generate_address():
    """Генерация случайного адреса"""
    return fake.address()

def generate_company_info():
    """Генерация данных компании"""
    return {
        "company": fake.company(),
        "job": fake.job(),
        "catch_phrase": fake.catch_phrase()
    }

def generate_credit_card():
    """Генерация данных кредитной карты"""
    return {
        "provider": fake.credit_card_provider(),
        "number": fake.credit_card_number(),
        "expire": fake.credit_card_expire(),
        "security_code": fake.credit_card_security_code()
    }
