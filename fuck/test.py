import requests
import schedule
import time
import datetime









def test():
    present = datetime.datetime.now()
    future = datetime.datetime(2023, 4, 1)
    difference = future - present
    days = difference.days
    header = {
        "Authorization": "MTQwNzc0ODEyNTAxOTM0MDgx.GDKLE5.LDqBpJJefyRG3GzSVXLJiWDbw9B6xwmWRETL0Q"
    }
    payload = {
        "content": f"Har du trent???"
    }
    requests.post(f"https://discord.com/api/v9/channels/490613672104689667/messages", data=payload, headers=header)
    

    
schedule.every(1).day.at("21:00").do(test)
while 1 : 
    schedule.run_pending()
    time.sleep(1)
    

