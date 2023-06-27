import pandas as pd 
import numpy as np 
import glob
import boto3 

def convert_csv_to_df(csv_directory_path):
    dfs = {}
    print('Now converting csv files to dataframes...')
    print('-' * 150)
    for csv_file in glob.glob(csv_directory_path + '/*.csv'):
        print(f'Working on converting {csv_file} to dataframe...')
        df = pd.read_csv(csv_file)
        print('Now Getting filename...')
        filename = csv_file.split('/')[-1].replace('.csv', '')
        print('Renaming dataframe...')
        exec(f"dfs['df_{filename}'] = df")
    print('-' * 150)
    print('Done converting csv files')
    return dfs

dfs = convert_csv_to_df('data-analytics-files')

dfs.keys()
sorted_keys = sorted(dfs.keys())
dfs_sorted = {key: dfs[key] for key in sorted_keys}
dfs_sorted.keys()
print(dfs_sorted.keys())
print('-' * 150)

# function that will be used to find columns have a few or all NULL and NAN values. This function will couunt and display the values in the terminal and drop all
def count_and_clean_nulls_values(df):
    number_of_rows = df.shape[0]
    print(f'This dataframe contains {number_of_rows} rows')
    print('-' * 150)
    null_count = pd.isna(df).sum()
    print(null_count)
    print('-' * 150)
    nan_columns = df.columns[df.isna().all()]
    print(nan_columns)
    print('Now dropping all NULL columns in dataframe')
    df.drop(columns=nan_columns, axis=1, inplace=True)
    print(df.columns[df.isna().all()])
    print('-' * 150)
    return df

# Running the count_and_clean_nulls_values function and returning the clean dataframes into a list.
df_list = []
for df_name, data_frame in dfs_sorted.items():
    print(f'Working on {df_name}')
    print('-' * 150)
    df = count_and_clean_nulls_values(data_frame)
    df_list.append(df)

# This section counts the number of rows in each dataframe and the number of nulls in each column. This section of code will also count the total number of  nulls in total then replace them withthe value 0.
clean_df_list = []
for df in df_list:
    number_of_rows = df.shape[0]
    print(f'This dataframe contains {number_of_rows} rows')
    null_values_count= df.isnull().sum()
    if null_values_count.any():
        print(f'This dataframe contains NULL values')
        all_null_values = df.isnull().sum().sum()
        print(f'This dataframe contains a total  of {all_null_values} values')
    else:
        print('This dataframe does NOT contains NULL values')
    print(f'Replacing NULL values in the dataframe with 0s')
    print('-' * 150)
    df.fillna(0 ,inplace = True)
    clean_df_list.append(df)

for df in clean_df_list:
    print('Checking columns in data_frame')
    columns = df.columns.to_list()
    print(columns)
    total_num_of_columns = len(columns)
    print(f'There are {total_num_of_columns} total columns in this data_frame')
    print('-' * 150)
    
print(f'Now concatenating the different dataframes')
df = pd.concat(clean_df_list).reset_index(drop=True)
number_of_rows = df.shape[0]
print(f'This dataframe contains {number_of_rows} rows')
for column in df.columns:
    null_values_count = df[column].isnull().sum()
    print(f'{column}: has {null_values_count} null values')
    df.fillna(0, inplace=True)
    print ('Replacing NULL values in the combined dataframe with 0s')

print('Saving the combined dataframe...')
df.to_csv('combined_dataframe.csv', index=False)
number_of_rows = df.shape[0]
print(f'This dataframe contains {number_of_rows} rows')


