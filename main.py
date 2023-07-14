import json

with open('input.json', 'r') as file:
    data = json.load(file)

def process_data(data):
    if isinstance(data, dict):
        if 'type' in data and data['type'] == 'object':
            data['additionalProperties'] = False
        if 'type' in data and data['type'] == 'string':
            data['maxLength'] = 255
        if 'type' in data and data['type'] == 'array':
            data['maxItems'] = 100
        if 'type' in data and (data['type'] == 'number' or data['type'] == 'integer'):
            data['minimum'] = -2147483648
            data['maximum'] = 2147483647
        for key, value in data.items():
            if isinstance(value, dict):
                if 'type' in value and value['type'] == 'object':
                    value['additionalProperties'] = False
                if 'type' in data and data['type'] == 'string':
                    data['maxLength'] = 255
                if 'type' in data and data['type'] == 'array':
                    data['maxItems'] = 100
                if 'type' in data and (data['type'] == 'number' or data['type'] == 'integer'):
                    data['minimum'] = -2147483648
                    data['maximum'] = 2147483647
                process_data(value)
            elif isinstance(value, list):
                for item in value:
                    process_data(item)
    elif isinstance(data, list):
        for item in data:
            if 'type' in item and item['type'] == 'object':
                item['additionalProperties'] = False
            if 'type' in data and data['type'] == 'string':
                data['maxLength'] = 255
            if 'type' in data and data['type'] == 'array':
                data['maxItems'] = 100
            if 'type' in data and (data['type'] == 'number' or data['type'] == 'integer'):
                data['minimum'] = -2147483648
                data['maximum'] = 2147483647
            process_data(item)
    else:
        return

process_data(data)

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)