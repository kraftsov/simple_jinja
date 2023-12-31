from jinja2 import Template

name = "Вася"

link = '''В HTML-документе ссылки определяются так: 
<a href="#">Ссылка</a>'''

# конструкция {% raw %} ... {% endraw %}
templ = Template(
    "Пример экранирования имени {{ name }}. В этом случае не замещается синтаксис {% raw %} {{ name }} {% endraw %}!"
)
# конструкция | e производит возврат в HTML страницу кодировок типа &lt &#34 #&#34 и пр
templ_link = Template("Ссылка будет экранирована и будут выведены символы:\n{{link | e}}")


print(templ.render(name=name))
print()
print(templ_link.render(link=link))
print()