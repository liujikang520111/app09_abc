import yaml

data = {
    "name": "小皮",
    "age": 20
}

with open("./hehe", "w", encoding="utf-8") as f:
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)

    print(data)
    # print(type(data.get("value12")))
    # print(type(data.get("value13")))
