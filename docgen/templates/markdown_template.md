{# templates/markdown_template.md #}
# Documentation

{% for item in items %}
## {{ item.name }}

{% if item.docstring %}
{{ item.docstring }}
{% endif %}

{% if item.params %}
### Parameters:
{% for param in item.params %}
- **{{ param.name }}**: {{ param.desc }}
{% endfor %}
{% endif %}

{% if item.returns %}
### Returns:
{{ item.returns }}
{% endif %}

{% endfor %}
