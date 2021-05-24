import requests
import json
import pandas as pd
from datetime import datetime
import time
import os

import configs


class Video:
    def __init__(self, urls, col_names, api_key):
        self.file_name = "export.csv"
        self.api_key = api_key
    
        self.urls = urls
        self.col_names = col_names
        self.dict = dict(zip(col_names, urls))
    
    def start_bot(self):
        if os.path.isfile(self.file_name):
            export_df = pd.read_csv(self.file_name, index_col = 0)
        else:
            export_df = pd.DataFrame(columns = self.col_names)
        
        while True:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            try:
                for col_name, url in self.dict.items():
                    # get desired Count from API
                    http = requests.Session()
                    response = http.get(url + '&key=' + self.api_key).text
                    response_json = json.loads(response)
                    export_df.loc[time_now, col_name] = int(response_json["items"][0]["liveStreamingDetails"]["concurrentViewers"])
                
                print(export_df)
                # export every hour
                if pd.DatetimeIndex(export_df.index).hour[-1] != pd.DatetimeIndex(export_df.index).hour[-2]:
                    export_df[col_names] = export_df[col_names].astype("Int64")
                    export_df.to_csv(self.file_name)
                
                time.sleep(59.8)
            except:
                # export when, an error occurs
                export_df[col_names] = export_df[col_names].astype("Int64")
                export_df.to_csv(self.file_name)
                break
            


if __name__ == "__main__":
    urls = ['https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=yxdOhAyVrak',
            'https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=9UGEwjFiR8Q']
    col_names = ["Count_original", 
                 "Count_LoFi"]

    Videos = Video(urls = urls,
                    col_names = col_names,
                    api_key = configs.key)
    Videos.start_bot()

