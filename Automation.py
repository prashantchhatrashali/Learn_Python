
'''
Reading and importing tables from website


import pandas as pd
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
len(simpsons)
#simpsons[1]
'''


'''
Using for loop downloading csv files

import pandas as pd
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

print(df_premier21)

#Updating names of perticular columns
df_premier21.rename(columns={'FTHG':'home_goal',
                             'FTAG':'away_goal'}, inplace=True)

df_premier21
'''

'''
Reading PDF and extracting data

use camelot-py library with dependency tk and ghostscript

'''

import camelot 

table=camelot.read_pdf("38.321_MAC_Specification_ts_138321v160100p.pdf", pages='148')
print(table)

table.export('mac.csv',f='csv', compress=True)
table[0].to_csv('mac.csv')
