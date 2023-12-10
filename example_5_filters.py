from jinja2 import Template

cars = [
    {'id': 1, 'brand': "BMW", 'model': "X5", "price": 100000},
    {'id': 2, 'brand': "Audi", 'model': "A6", "price": 80000},
    {'id': 3, 'brand': "Toyota", 'model': "Camry", "price": 60000},
    {'id': 4, 'brand': "Lada", 'model': "Niva", "price": 40000},
]

calc = "Общая стоимость автомобилей в продаже {{ garage | sum(attribute='price') }} долларов"
total_sum_tmpl = Template(calc)
msg = total_sum_tmpl.render(garage=cars)

max_cost = "Самый дорогой автомобиль в продаже - {{ (garage | max(attribute='price')).model }}"
max_cost_tmpl = Template(max_cost)
msg2 = max_cost_tmpl.render(garage=cars)

print(msg)
print(msg2)

###

person = [
    {"name": "Вася", "old": 25, "weight": 75},
    {"name": "Петя", "old": 30, "weight": 65},
    {"name": "Маша", "old": 28, "weight": 80},
]

person_tmpl = '''
{%- for p in crowd -%}
{% filter upper -%}
    {{ p.name }}
{% endfilter -%}
{%-  endfor -%}
'''

tm = Template(person_tmpl)
msg_1 = tm.render(crowd=person)

print(msg_1)