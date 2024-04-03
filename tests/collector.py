
import re
import json
import time
from datetime import datetime
from requests import get

def get_value(key, text):
    return float(re.findall(f'''\n{key} (.*?)\n''', text)[0])

with open('tests/data.json', 'w', encoding = 'utf-8') as file:
    json.dump([], file, indent = 2)

with open('tests/data.json', 'r') as file:
    data = json.load(file)

while True:

    text = get('https://teste-prometheus-09dad054d275.herokuapp.com/metrics').text

    data.append(
        {
            'timestamp': int(datetime.now().timestamp()),
            'process_virtual_memory_mb_gauge': get_value('process_virtual_memory_bytes', text)/1000000,
            'process_resident_memory_mb_gauge': get_value('process_resident_memory_bytes', text)/1000000,
            'process_cpu_seconds_total_counter_min': round(get_value('process_cpu_seconds_total', text)/60, 1),
            'http_request_total_200': get_value('flask_http_request_total{method="GET",status="200"}', text)
        }
    )

    with open('tests/data.json', 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 2)

    time.sleep(5)

