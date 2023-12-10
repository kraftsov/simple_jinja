# вложенные макросы

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
    <li>{{u.name}} {{caller(u)}}
{% endfor -%}
</ul>
{% endmacro %}

{% call(_) list_users(users_list) %}
<ul>
<li>возраст: {{_.old}}
<li>вес: {{_.weight}}
</ul>
{% endcall %}
'''

tm = Template(html)
msg = tm.render(users_list=persons)

print(msg)
