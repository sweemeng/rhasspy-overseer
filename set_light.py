import pprint


def set_light(payload):
    pprint.pprint(payload)
    msg = {}
    output = {}
    for item in payload["slots"]:
        msg[item["entity"]] = item["rawValue"]
    print(msg)
    if msg["name"] == "room light":
        topic = "switch/roomlight"
    else:
        topic = ""
    return topic, msg["state"]
