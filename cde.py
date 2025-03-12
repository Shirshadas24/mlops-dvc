import pandas as pd
import os

data={
    'name':
    ['A','B','C','D'],
    'age':
    [10,20,30,40],
    'city':
    ['NY','LA','SF','DC']

}

df=pd.DataFrame(data)
#adding new row for v2
new_row_low={
    'name':'E',
    'age':50,
    'city':'CHI'
}
df.loc[len(df.index)]=new_row_low

#adding new row for v3
new_row_low2={
    'name':'F',
    'age':60,
    'city':'MIA'
}

df.loc[len(df.index)]=new_row_low2

#ensure data directory exists at root level
data_dir='data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

#define file path
file_path=os.path.join(data_dir,'data.csv')

#save data to csv
df.to_csv(file_path,index=False)

print('Data saved to:',file_path)