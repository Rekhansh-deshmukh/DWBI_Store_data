import pandas as pd

start_date ='2025-01-01' 
end_date ='2025-12-31'

# Generating series of dates using padas date range function
date_range = pd.date_range(start_date,end_date)
date_dimension = pd.DataFrame(date_range,columns=['Date'])

date_dimension['DateId'] = date_dimension['Date'].dt.strftime('%Y%m%d').astype(int)
date_dimension['DaysofWeek'] = date_dimension['Date'].dt.day_of_week 
date_dimension['Month'] = date_dimension['Date'].dt.month
date_dimension['Quarter'] = date_dimension['Date'].dt.quarter
date_dimension['Year'] = date_dimension['Date'].dt.year
date_dimension['Isweekend'] = date_dimension['Date'].isin([5,6])


cols = ['DateId'] + [cols for cols in date_dimension.columns if cols !='DateID']

print(cols)