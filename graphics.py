from datetime import datetime, timedelta
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


API_BASE = "https://api.stackexchange.com/2.2/questions?pagesize=1&filter=total&order=desc&sort=activity"


# Display graph.
def generate_graph(df: object):
    df.plot(kind='line', title="Numbers of questions over time", grid=True)
    plt.xticks(rotation=-50, ha='left')
    plt.subplots_adjust(bottom=0.24, left=0.1)
    plt.show()


# Get the data from stackexchange API.
def fetch_data(params: dict):
    df = pd.DataFrame(columns=params['tags'])

    # for each step between the two dates.
    while params['from'] < params['to']:
        row = []
        stepped = params['from'] + params['step']
        ifrom = int(datetime.timestamp(params['from']))
        ito = int(datetime.timestamp(stepped))

        # For each tag, get the total number of question for the slice of time.
        for tag in params['tags']:
            query = f"{API_BASE}&site={params['site']}&fromdate={ifrom}&todate={ito}&tagged={tag}"
            # print(query)
            r = requests.get(query)
            jr = r.json()
            if not 'total' in jr:
                print("error while fetching.")
                print(f"query: {query}")
                print(jr)
                exit(1)
            row.append(r.json()['total'])

        # Removing the date/time part if unnecessary.
        index = (str(params['from'].date()) if params['from'].hour == 0 else str(params['from'].time())).replace('-', ' ')
        df.loc[index] = row
        params['from'] = stepped

    return df


# Call this function directly if using this script as part of another one (not as a standalone tool).
# Parameters:
# from      datetime.datetime
# to        datetime.datetime
# step      dateutils.relativedelta
# tags      array<str>
# site      str
def graphics(params: dict):
    data = fetch_data(params)

    print(data)
    generate_graph(data)
