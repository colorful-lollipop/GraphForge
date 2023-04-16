type_map: dict[str, str] = {
    'int': 'int',
    'str': 'string',
    'string': 'string',
    'float': 'float',
    'double': 'double',
    'decimal': 'double',
    'bool': 'bool',
}


def get_type(name: str) -> str:
    name = name.lower()
    if name not in type_map:
        raise Exception(f'illegal type {name}')
    return type_map[name]
