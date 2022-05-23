
import requests
import json
import random
import time
from datetime import datetime

def getlist():

    # You can add more than one bot if you have multiple discord accounts.
    bots_setting = [
        {
            "name": "bot1",
            "authorizations": [
                    "token1","token 2"
                ],  # Please remember to put in your discord message authorization code
                    # separate by comma if you have more than one token.
            "channel_lists": [
                {
                    "name": "Alpha Shark",  # Nickname for the channel
                    "settings": {
                        "channel_id": "949490494944198727",     # Channel's discord ID
                        "lottery_keyword": "",      # Lottery keyword to detect:  "React with 🎉 to enter!"
                        "emojis_to_click": ["%F0%9F%90%BC"]     # emoji to click
                    }
                },{
                    "name": "channel2",  # Nickname for the channel
                    "settings": {
                        "channel_id": "949490494944198730",     # Channel's discord ID
                        "lottery_keyword": "",      # Lottery keyword to detect:  "React with 🎉 to enter!"
                        "emojis_to_click": ["%F0%9F%90%BC"]     # emoji to click
                    }
                }
# can add more channel here




            ]
        }
    ]

    limit=20
    
    for bot in bots_setting:
        for auth in bot["authorizations"]:
            header = {
                "Authorization": auth,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
            }
            for channel in bot["channel_lists"]:
                url = "https://discord.com/api/v9/channels/{}/messages?limit={}".format(channel["settings"]["channel_id"], limit)
                try:
                    res = requests.get(url=url, headers=header)
                    messages_json = json.loads(res.text)
                    for message in messages_json:
                        try:
                            if channel["settings"]["lottery_keyword"] in json.dumps(message):
                                is_lottery_post = True
                            else:
                                is_lottery_post = False

                            if is_lottery_post:
                                print("-------------Lottery captured!--------------")
                                print("Date:", datetime.now())
                                print("Channel:", channel["name"])
                                print("Message ID:", message["id"])
                                print("Content:", message["content"])
                                print("embeds:", message["embeds"])
                                for emoji in channel["settings"]["emojis_to_click"]:
                                    url = "https://discord.com/api/v9/channels/{}/messages/{}/reactions/{}/%40me".format(
                                        channel["settings"]["channel_id"], message["id"], emoji)
                                    requests.put(url=url, headers=header)
                                    time.sleep(1)

                        except:
                            print("Failed to expand messages.")
                            pass
                except:
                    print("Failed to get discord message.")
                    pass

if __name__ == '__main__':
    while True:
        try:
            getlist()
            sleeptime = random.randrange(30, 50)
            time.sleep(sleeptime)
        except:
            pass
        continue