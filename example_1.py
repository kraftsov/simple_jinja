from jinja2 import Template

name = "Вася"
age = 25

info_about_man = Template("Зовут меня {{ name }}, мне {{ age }} лет.")

msg = info_about_man.render(name=name, age=age)

print(msg)
