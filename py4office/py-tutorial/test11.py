import pandas as pd
import numpy as np
import json

# data = pd.read_csv('py4office/py-pandas/data/property-data.csv')
# # print(data)

# data2 = pd.read_json('py4office/py-pandas/data/nested_list.json')
# print(data2)

obj = """
{
    "name": "Wes",
    "place_lived": [
        "US",
        "Spain",
        "China"
    ],
    "pet": null,
    "siblings": [
        {
            "name": "john",
            "age": 30,
            "pets": [
                "Zeus",
                "Zuko"
            ]
        },
        {
            "name": "ali",
            "age": 27,
            "pets": [
                "Cisco",
                "Taozi"
            ]
        }
    ]
}
"""
data = json.loads(obj)
print(data)

siblings = data["siblings"]
sb = pd.DataFrame(siblings, columns=['name', 'age'])
print(sb)

#pd.read_json()是要转换成dataframe or series,所以需要same size的array
#可以把dataframe or series转换成to_json()
