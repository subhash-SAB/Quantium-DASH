import pandas as pd 

file1=pd.read_csv('S:/QUANTIUM RESORCES/daily_sales_data_0.csv')
file2=pd.read_csv('S:/QUANTIUM RESORCES/daily_sales_data_1.csv')
file3=pd.read_csv('S:/QUANTIUM RESORCES/daily_sales_data_2.csv')


df=pd.concat([file1, file2, file3], ignore_index=True)
df=df[df['product']=='pink morsel']

#verification
#print(df)

df['price']=df['price'].astype(str).str.replace('$', '', regex=False).astype(float)
df['sales']=df['quantity']*df['price']
df['sales']='$'+df['sales'].astype(str)

#verification
#print(df['sales'])

final=df[['sales', 'date', 'region' ]]
final.to_csv('S:/QUANTIUM/final_ouput.csv',index=False)
