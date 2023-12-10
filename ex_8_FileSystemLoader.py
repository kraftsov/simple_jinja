from jinja2 import (
    Environment,
    FileSystemLoader,  # для работы с файловой системой OC
)

persons = [
    {"name": "Вася", "old": 25, "weight": 75},
    {"name": "Петя", "old": 30, "weight": 65},
    {"name": "Маша", "old": 28, "weight": 80},
]

file_loader = FileSystemLoader('templates')  # указываем на папку с шаблонами (аналог движка)
env = Environment(loader=file_loader)  # создаем окружение (загрузчик) (аналог сессии)

tm = env.get_template('main.html')  # создаем экземпляр класса Template
msg = tm.render(users=persons)  # подставляем данные

print(msg)

