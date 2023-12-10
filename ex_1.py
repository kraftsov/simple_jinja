from jinja2 import Template

# переменные:
name = "Вася"
age = 25

# словарь:
person = {
    "name": name,
    "age": age
}

# выдергиваем переменные напрямую:
info_about_man = Template("Зовут меня {{ name }}, мне {{ age }} лет.")

msg = info_about_man.render(name=name, age=age)


# выдергиваем переменные через словарь обращаясь по ключу:
info_from_dict = Template("Зовут меня {{ person.name }}, мне {{ person.age }} лет.")

msg2 = info_from_dict.render(person=person)

print(msg)
print()
print(msg2)
