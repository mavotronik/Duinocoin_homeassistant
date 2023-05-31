username = data.get('username')
password = data.get('password')
amount = data.get('amount')

import requests

resp = requests.get(f"https://server.duinocoin.com/stake/{username}?password={password}&amount={amount}")
logger.warning(resp.text)
