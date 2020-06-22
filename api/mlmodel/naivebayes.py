import pandas as pd
import numpy as np
from ..models import testing_data_raw, training_data_raw, testing_data_input
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# read data from csv files
col_names_proc = ['Precinct', 'Congressional District', 'Age', 'Gender', 
    'Early Vote', 'Party']
col_names_test = ['Precinct', 'Congressional District', 'Age', 'Gender', 'Party']
training_data = pd.read_csv("C:/Users/Dominic/hevmREST/hevmREST/MLModel/processed_training_data.csv", names=col_names_proc)
testing_data = pd.read_csv("C:/Users/Dominic/hevmREST/hevmREST/MLModel/processed_testing_data.csv", names=col_names_test)

# format csv data into numpy arrays
x_train = np.array(training_data.drop("Early Vote", axis=1))
y_train = np.array(training_data['Early Vote'])
x_test = np.array(testing_data)

# instantiate a Gaussian Naive Bayes Model
gnb = GaussianNB()

y_gnb = gnb.partial_fit(x_train, y_train, np.unique(y_train))

results = gnb.predict_proba(x_test)[: , [1]]
df_results = pd.DataFrame(data=results)
print(results)
testing_data['Early Vote Probability'] = df_results
