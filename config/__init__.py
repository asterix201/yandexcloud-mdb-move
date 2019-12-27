import json

cfg = {}

with open("config.json") as fd:
    cfg = json.load(fd)
