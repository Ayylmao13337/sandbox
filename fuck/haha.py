import requests
import schedule
import time
import datetime



# Calculate days until training starts
present = datetime.datetime.now()
future = datetime.datetime(2023, 4, 1)
difference = future - present
days = difference.days
    
header = {
        "Authorization": "MTQwNzc0ODEyNTAxOTM0MDgx.GDKLE5.LDqBpJJefyRG3GzSVXLJiWDbw9B6xwmWRETL0Q"
    }
payload = {
        "content": f"Det er {days} dager igjen til trening starter https://tenor.com/view/training-work-hard-practice-gif-18181584"
    }

requests.post(f"https://discord.com/api/v9/channels/485915738776010784/messages", data=payload, headers=header)
    
    
