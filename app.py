import requests
import json

def main():
    url = "url"
    title = "title"
    textfile = "app.txt"
    sendmsg = ""
    with open(textfile, "r", encoding="utf-8") as f:
        reader = f.readlines()
        for row in reader:
            row = row.rstrip()
            sendmsg += row + "\n\n"

    msg = {
    "attachments": [
        {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
            {
                "type": "TextBlock",
                "text": title,
                "size": "Large",
                "weight": "Bolder",
                "color": "Accent"
            },
            {
                "type": "TextBlock",
                "text": "",
                "id": "acHeaderTagLine",
                "separator": True
            },
            {
                "type": "TextBlock",
                "text": sendmsg,
                "wrap": True,
            }
            ]
        }
        }
    ]
    }
    response = send_message(url, msg)

def send_message(url, msg):
    response = requests.post(
        url=url,
        data=json.dumps(msg),
        headers={"Content-Type": "application/json"}
    )
    return response

if __name__=='__main__':
    main()
