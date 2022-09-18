from websocket import create_connection
import json
import pprint

# Initialize the headers needed for the websocket connection
headers = json.dumps({
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
    "Cookie": "__utmz=178991673.1663184611.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=178991673.1137384341.1663184611.1663276690.1663411499.13; __utmc=178991673; _ga=GA1.2.1447543861.1663411512; _gid=GA1.2.1643500174.1663411512; __utmt=1; __utmb=178991673.35.9.1663412325744",
    "Host": "livetiming.getraceresults.com",
    "Origin": "https://livetiming.getraceresults.com",
    "Pragma": "no-cache",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    "Sec-WebSocket-Key": "86TiQCstGzMOMU5rmW13eA==",
    "Sec-WebSocket-Version": "13",
    "Upgrade": "websocket",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
})


# Then create a connection to the tunnel
ws = create_connection(
    'wss://livetiming.getraceresults.com/lt/connect?transport=webSockets&clientProtocol=1.5&_tk=81acecf7aef44248ba72ad080ad810fc&_gr=w&_tkdm=41980&connectionToken=7hVwQmQ83gkZ8ui8RipvLbRe4Y3P/uqRUJa8IilsERI6KhfwVb+n4zfltW0tO3ZMGDzqRn9PrNwxSV9S24/DLEb6E1vPfimhX4H+CcJteCnATf5IgAyRsgPbG4jlojF+&tid=6', headers=headers)

# Then send a message through the tunnel
ws.send('{"H":"publicmaphub","M":"getData","A":[],"I":1}')

# view the message return from the tunnel
while True:
    pprint.pprint(json.loads(ws.recv()))
