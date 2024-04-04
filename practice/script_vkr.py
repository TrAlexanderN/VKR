import os

# Шаг 1: Запрос пути до репозитория для клонирования
repo_path = input("Введите путь до репозитория для клонирования: ")

# Шаг 2: Клонирование репозитория
os.system(f"git clone {repo_path}")

# Шаг 3: Переход в папку с клонированным репозиторием
repo_name = repo_path.split("/")[-1].replace(".git", "")
os.chdir(repo_name)

# Шаг 4: Запуск сканирования кода
os.system("/snap/bin/semgrep scan --config auto")

# Шаг 5: Сохранение результатов сканирования
os.system("/snap/bin/semgrep --config auto --output scan_results.txt --text")

# Шаг 6: Открытие файла с анализом
os.system("nano scan_results.txt")
