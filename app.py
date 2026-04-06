import sys
from logic import demo_profile, demo_address, demo_company, demo_credit_card

def show_menu():
    """Отображение главного меню"""
    print("\n" + "=" * 50)
    print("🎭 FAKER ДЕМОНСТРАЦИОННЫЙ ПРОЕКТ")
    print("=" * 50)
    print("1. 👥 Генерация профилей")
    print("2. 🏠 Генерация адресов")
    print("3. 🏢 Генерация компаний и должностей")
    print("4. 💳 Генерация банковских карт")
    print("5. 🚀 Полная демонстрация всех генераторов")
    print("0. ❌ Выход")
    print("-" * 50)
    return input("Выберите пункт (0-5): ").strip()

def main():
    """Главная функция приложения"""
    while True:
        try:
            choice = show_menu()

            if choice == "1":
                demo_profile(2)
            elif choice == "2":
                demo_address(3)
            elif choice == "3":
                demo_company(2)
            elif choice == "4":
                demo_credit_card(2)
            elif choice == "5":
                demo_profile(1)
                demo_address(2)
                demo_company(1)
                demo_credit_card(1)
            elif choice == "0":
                print("\n👋 До свидания!")
                sys.exit(0)
            else:
                print("❌ Неверный выбор. Попробуйте снова.")

        except KeyboardInterrupt:
            print("\n\n👋 Прервано пользователем")
            sys.exit(0)
        except Exception as e:
            print(f"⚠️  Ошибка: {e}")

if __name__ == "__main__":
    main()
