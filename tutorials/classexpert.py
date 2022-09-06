import requests
import json

column_index_int = 0
column_index = {}

x = requests.get('https://classpert.com/search.json?p=1&q=python')
out = x.text

jout = json.loads(out)

for course in jout['data']:
    for k, v in course:
        # new_row =
        if k in column_index:
            pass
        else:
            column_index

print(jout)
