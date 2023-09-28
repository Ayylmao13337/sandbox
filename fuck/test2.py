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
        "content": f"HAHAHAHA DET FUNGERER, 'Jeg aner egentlig ikke om det kommer til å fungere så dette er en melding jeg har skrevet før'"
    }
    requests.post(f"https://discord.com/api/v9/channels/490613672104689667/messages", data=payload, headers=header)
    
schedule.every(1).day.at("08:10").do(test)
while 1 : 
    schedule.run_pending()
    time.sleep(1)