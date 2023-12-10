from jinja2 import Template

cities = [
    {'id': 1, 'city': "Москва"},
    {'id': 2, 'city': "Саратов"},
    {'id': 5, 'city': "Санкт-Петербург"},
    {'id': 7, 'city': "Новосибирск"},
    {'id': 8, 'city': "Екатеринбург"},
    {'id': 11, 'city': "Нижний Новгород"},
]

link = '''<select name="cities">
{% for city in cities -%}
{% if city.id >= 5 -%}
    <option value="{{ city.id }}">{{ city.city }}</option>
{% else -%}
    {{ city.city }}    
{% endif -%}
{% endfor -%}
</select>
'''

tm = Template(link)
msg = tm.render(cities=cities)

# msg = Template(link).render(cities=cities)

print(msg)
