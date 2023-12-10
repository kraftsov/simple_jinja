from jinja2 import (
    Environment,
    FunctionLoader  # для работы с файловой системой
)

persons = [
    {"name": "Вася", "old": 25, "weight": 75},
    {"name": "Петя", "old": 30, "weight": 65},
    {"name": "Маша", "old": 28, "weight": 80},
]


def load_tpl(path):
    if path == "index":
        return '''Имя {{ u.name }}, возраст {{ u.old}}'''
    else:
        return '''Данные {{ u }}'''


file_loader = FunctionLoader(load_tpl)  # (аналог движка)
env = Environment(loader=file_loader)  # создаем окружение (загрузчик) (аналог сессии)

tm = env.get_template('index')  # создаем экземпляр класса Template
msg = tm.render(u=persons[0])  # подставляем данные

print(msg)
