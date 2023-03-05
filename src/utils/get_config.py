import json


def _get_config(config_file: str) -> dict:
    try:
        with open(config_file) as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"Failed to red config.json: {e}")
