# Youtube Livestream Viewer Counter

This Application is adressing the Youtube API for Information on Live Streams

`youtube_crawler.py` gets the live viewer count every minute and save the result in a Data Frame and exports this every Hour.

`analysis.py` contains simple analysis of the crawled data including a simple Plot.

`configs.py` contains the google API Key. Getting this is free with a Google Account. Just go to https://console.cloud.google.com/apis, create a project and generate a Key and put it in here.

`export.csv` contains an example export for two 24/7 videos from MDprospect.



## Usage

To use this tool yourself, you would only have to adjust the end of the strings in the list `urls` in line 53. Go to the Livestream you want to monitor on youtube and copy the part from the HTTP adress where it says `v=abcdefghijkl`. Then paste this into the end of the strings in `urls` and change the column names `col_names` to what you want to call them. 

After creating such a dataframe, you would have to adjust the analysis script `analysis.py` with the according column names.