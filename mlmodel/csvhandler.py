import pandas as pd

# process raw data into usable data for model training
def process_training_data(df):

    ev_dict = {"Y": 1, "N": 0}
    age_dict = {"18-34": 1, "35-44": 2, "45-54": 3, "55-64": 4, "65-74": 5, "75-84": 6, "Over 85": 7}
    gender_dict = {"M": 1, "F": 2, "U": 3}
    party_dict = {"DEM": 1, "REP": 2, "LBT": 3, "GRN": 4, "OTH": 5}
    temp_data = pd.DataFrame(data=data.sample(n=3000), columns=col_names)
    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in temp_data.iterrows():
        pct = int(row['Precinct'])
        cd = int(row['Congressional District'])
        age = age_dict[row['Age']]
        gender = gender_dict[row['Gender']]
        ev = ev_dict[row['Early Vote']]
        party = party_dict[row['Party']]

        # append dataframe with correct amount of individual voters
        for x in range(1, row['Amount']):
            df.loc[temp_ind] = [pct, cd, age, gender, ev, party]
            temp_ind = temp_ind + 1
            df = df.sort_index()
    
    # output dataframe to csv
    df.to_csv("C:/Users/Dominic/hevmREST/hevmREST/MLModel/processed_training_data.csv")

def generate_testing_data(df):
    
    temp_data = pd.DataFrame(data=data.sample(n=150), columns=col_names)
    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in temp_data.iterrows():
        pct = row['Precinct']
        cd = row['Congressional District']
        age = row['Age']
        gender = row['Gender']
        party = row['Party']

        # append dataframe with correct amount of individual voters
        for x in range(1, row['Amount']):
            df.loc[temp_ind] = [pct, cd, age, gender, party]
            temp_ind = temp_ind + 1
            df = df.sort_index()
    
    # output dataframe to csv
    df.to_csv("C:/Users/Dominic/hevmREST/hevmREST/MLModel/testing_data.csv")

def prcoess_testing_data(df):
    
    age_dict = {"18-34": 1, "35-44": 2, "45-54": 3, "55-64": 4, "65-74": 5, "75-84": 6, "Over 85": 7}
    gender_dict = {"M": 1, "F": 2, "U": 3}
    party_dict = {"DEM": 1, "REP": 2, "LBT": 3, "GRN": 4, "OTH": 5}
    temp_data = pd.DataFrame(data=data.sample(n=3000))
    temp_ind = 1
    
    # convert values into int datatypes 
    for index, row in temp_data.iterrows():
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
            df = df.sort_index()
    
    # output dataframe to csv
    df.to_csv("C:/Users/Dominic/hevmREST/hevmREST/MLModel/processed_testing_data.csv")


col_names = ['Id', 'Precinct', 'Congressional District', 'Age', 'Gender', 'Early Vote', 
    'Party', 'Amount']

col_names_proc = ['Precinct', 'Congressional District', 'Age', 'Gender', 'Early Vote', 
    'Party']

col_names_test = ['Precinct', 'Congressional District', 'Age', 'Gender',
    'Party']

# load unprocessed csv data
data = pd.read_csv("C:/Users/Dominic/hevmREST/hevmREST/MLModel/Hispanic_Registration.csv",
    skiprows=1, names=col_names, header=None)

# initialize data structure for processed data
empty_train_data = pd.DataFrame(columns=col_names_proc)
empty_test_data = pd.DataFrame(columns=col_names_test)




process_training_data(empty_train_data)
# generate_testing_data(empty_test_data)
# prcoess_testing_data(empty_test_data)