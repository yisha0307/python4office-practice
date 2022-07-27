import numpy as np
import pandas as pd
import pandas_datareader as pdr

all_data = {sticker: pdr.get_data_stooq(sticker) for sticker in ['AAPL', 'IBM', 'GOOG']}
# print(all_data)

price = {sticker: data['Close'] for sticker, data in all_data.items()}
price = pd.DataFrame(price)
print(price.head())

volume = {sticker: data['Volume'] for sticker, data in all_data.items()}
volume = pd.DataFrame(volume)
print(volume.head())

cor = price.corrwith(volume)
print(cor)
print(price.corr())