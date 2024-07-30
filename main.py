from sorting_algorithms import counting_sort, radix_sort, bucket_sort
from database import create_connection, create_table, insert_result, fetch_results

def get_user_input():
    """Получает список чисел от пользователя и обрабатывает ввод."""
    while True:
        user_input = input("Введите список чисел, разделенных запятыми: ")
        try:
            # Преобразуем строку в список чисел
            numbers = [float(num) for num in user_input.split(",")]
            return numbers
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числа, разделенные запятыми.")

def main():
    print("Выберите алгоритм сортировки:")
    print("1. Сортировка подсчётом (Counting Sort) - только для целых чисел")
    print("2. Поразрядная сортировка (Radix Sort)")
    print("3. Сортировка ведрами (Bucket Sort)")
    choice = input("Введите номер выбранного алгоритма: ")

    # Получаем список чисел от пользователя
    data = get_user_input()

    # Создание соединения с базой данных
    conn = create_connection("sorting_results.db")
    create_table(conn)

    # Сортировка и сохранение результатов в зависимости от выбора пользователя
    if choice == '1':
        if all(isinstance(x, int) for x in data):
            sorted_data = counting_sort(data.copy())
            insert_result(conn, "Counting Sort", str(data), str(sorted_data))
        else:
            print("Сортировка подсчётом работает только с целыми числами. Пожалуйста, выберите другой алгоритм.")
            return
    elif choice == '2':
        sorted_data = radix_sort(data.copy())
        insert_result(conn, "Radix Sort", str(data), str(sorted_data))
    elif choice == '3':
        sorted_data = bucket_sort(data.copy())
        insert_result(conn, "Bucket Sort", str(data), str(sorted_data))
    else:
        print("Неверный выбор! Пожалуйста, выберите правильный номер.")
        return

    # Вывод результатов
    results = fetch_results(conn)
    for result in results:
        print(f"Algorithm: {result[1]}, Original: {result[2]}, Sorted: {result[3]}")

    # Закрытие соединения с базой данных
    conn.close()

if __name__ == "__main__":
    main()
