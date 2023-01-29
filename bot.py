#!/usr/bin/env python3

import fbchat
import re
from fbchat import Client
from fbchat.models import *
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

with open("credentials.txt") as file:
    email = file.readline().strip()
    password = file.readline().strip()

client = Client(email, password, max_tries=1)

print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)

#client.logout()
