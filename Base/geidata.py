import yaml, os


class GetData:
    def get_yml_data(self, y):
        with open("./Data" + os.sep + y, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
