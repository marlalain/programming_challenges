#!/usr/bin/env python3

# TODO Make it TUI

# imports
import os # TODO Change this
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as  web
from matplotlib import style
# vars
# defs
def get_csv(thing):
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2019,12,31)

    df = web.DataReader(thing, 'yahoo', start, end)
    df.to_csv('tsla.csv')
    print("Done")
def main():
    os.system("clear") # TODO Change this
    style.use('ggplot')
    #get_csv('TSLA')
    df = pd.read_csv('tsla.csv', index_col=0)
    #print(df.head())
# main
if __name__ == "__main__":
    main()
