def parameterized_config(template):
    all_vars = {k: v for d in [globals(), locals()] for (k, v) in d.items()}
    return template.format(**all_vars)