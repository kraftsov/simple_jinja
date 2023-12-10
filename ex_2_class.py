from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Вася", 25)

templ = Template('Здравствуйте, меня зовут {{ p.name }}, мне {{ p.age }} лет.')

msg = templ.render(p=person)

print(msg)
