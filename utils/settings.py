import os
import json


def get_token() -> str:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        return settings['api_token']


def set_token(token: str):
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        settings['api_token'] = token
    with open('settings.json', 'w') as f:
        json.dump(settings, f)