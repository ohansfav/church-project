import time
import json
# from sitename import knownsite

def scan_from_file():
    with open("sites.json", "r") as f:
       site_list = json.load(f)
        
        
    for site in site_list:
        print(f"starting scan from: {site}")
        time.sleep(1)
        print(f"Finished: {site}\n")
        
        
# scan_from_file()