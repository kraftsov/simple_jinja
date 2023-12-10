from jinja2 import Template

html = '''
{% macro input(name, value='', type='text', size=20) -%} 
    <input_ тип="{{ type }}" имя="{{ name }}" значение="{{ value }}" размер="{{ size }}"> 
{%- endmacro %}

<p> Все что имеет значение: имя переменной и ее расположение в строке кода))
<p> {{ input('username', 'Вася') }}
<p> {{ input('email') }}
<p> {{ input('password', size=50) }}
'''

tm = Template(html)
msg = tm.render()

print(msg)
