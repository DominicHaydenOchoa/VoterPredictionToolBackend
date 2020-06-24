import pandas as pd
import numpy

# generate raw training data for user breakdown
def generate_training_data(df, df_empty):
    
    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in df.iterrows():
        
        pct = row['Precinct']
        cd = row['Congressional District']
        age = row['Age']
        gender = row['Gender']
        early_vote = row["Early Vote"]
        party = row['Party']

        # append dataframe with correct amount of individual voters
        for x in range(1, row['Amount']):
            df_empty.loc[temp_ind] = [pct, cd, age, gender, early_vote, party]
            temp_ind = temp_ind + 1
            df_empty = df_empty.sort_index()
    
    # output dataframe to csv
    df_empty.to_csv("C:/Users/Dominic/Documents/Capstone/HEVM/backend/mlmodel/training_data.csv")

# process raw data into usable data for model training
def process_training_data(df, df_empty):

    ev_dict = {"Y": 1, "N": 0}
    age_dict = {"18-34": 1, "35-44": 2, "45-54": 3, "55-64": 4, "65-74": 5, "75-84": 6, "Over 85": 7}
    gender_dict = {"M": 1, "F": 2, "U": 3}
    party_dict = {"DEM": 1, "REP": 2, "LBT": 3, "GRN": 4, "OTH": 5}
    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in df.iterrows():
        pct = int(row['Precinct'])
        cd = int(row['Congressional District'])
        age = age_dict[row['Age']]
        gender = gender_dict[row['Gender']]
        ev = ev_dict[row['Early Vote']]
        party = party_dict[row['Party']]

        # append dataframe with correct amount of individual voters
        for x in range(1, row['Amount']):
            df_empty.loc[temp_ind] = [pct, cd, age, gender, ev, party]
            temp_ind = temp_ind + 1
            df_empty = df_empty.sort_index()
    
    # output dataframe to csv
    df_empty.to_csv("C:/Users/Dominic/Documents/Capstone/HEVM/backend/mlmodel/processed_training_data.csv")

def generate_testing_data(df, df_empty):

    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in df.iterrows():
        pct = row['Precinct']
        cd = row['Congressional District']
        age = row['Age']
        gender = row['Gender']
        ev = row['Early Vote']
        party = row['Party']

        # append dataframe with correct amount of individual voters
        df_empty.loc[temp_ind] = [pct, cd, age, gender, ev, party]
        temp_ind = temp_ind + 1
        df_empty = df_empty.sort_index()
    
    # output dataframe to csv
    df_empty.to_csv("C:/Users/Dominic/Documents/Capstone/HEVM/backend/api/csv/testing_data.csv")


def process_testing_data(df, df_empty):
    
    age_dict = {"18-34": 1, "35-44": 2, "45-54": 3, "55-64": 4, "65-74": 5, "75-84": 6, "Over 85": 7, "nan": 0}
    gender_dict = {"M": 1, "F": 2, "U": 3}
    party_dict = {"DEM": 1, "REP": 2, "LBT": 3, "GRN": 4, "OTH": 5}
    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in df.iterrows():
        
        pct = int(row['Precinct'])
        cd = int(row['Congressional District'])
        print(row['Age'])
        age = age_dict[row['Age']]
        gender = gender_dict[row['Gender']]
        party = party_dict[row['Party']]

        # append dataframe with correct amount of individual voters
        for x in range(1, row['Amount']):
            df.loc[temp_ind] = [pct, cd, age, gender, party]
            temp_ind = temp_ind + 1
            df_empty = df_empty.sort_index()
    
    # output dataframe to csv
    df_empty.to_csv("C:/Users/Dominic/Documents/Capstone/HEVM/backend/MLModel/processed_testing_data.csv")


col_names = ['Id', 'Precinct', 'Congressional District', 'Age', 'Gender', 'Early Vote', 
    'Party', 'Amount']

col_names_proc = ['Precinct', 'Congressional District', 'Age', 'Gender', 'Early Vote', 
    'Party']

col_names_test = ['Precinct', 'Congressional District', 'Age', 'Gender',
    'Party']

# load unprocessed csv data
data = pd.read_csv("C:/Users/Dominic/Documents/Capstone/HEVM/backend/api/csv/hispanic_registration.csv",
    skiprows=1, names=col_names, header=None)

# initialize data structure for processed data
empty_train_data = pd.DataFrame(columns=col_names_proc)
result_data = pd.DataFrame(columns=col_names_proc)

df_train = pd.DataFrame(data=data.sample(n=1200))
df_test = pd.DataFrame(data=data.sample(n=150))



# generate_training_data(df_train, empty_train_data)
# process_training_data(df_train, empty_train_data)
generate_testing_data(df_test, result_data)
# prcoess_testing_data(df_test, empty_test_data)