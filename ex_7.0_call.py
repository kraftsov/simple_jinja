# вложенные макросы (первая часть)

from jinja2 import Template

persons = [
    {"name": "Вася", "age": 25, "old": 25, "weight": 75},
    {"name": "Петя", "age": 30, "old": 30, "weight": 65},
    {"name": "Маша", "age": 28, "old": 28, "weight": 80},
]

html = '''
{% macro list_users(list_of_user) %}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}
{% endfor -%}
</ul>
{% endmacro %}

{{list_users(users_list)}}

'''

tm = Template(html)
msg = tm.render(users_list=persons)

print(msg)
