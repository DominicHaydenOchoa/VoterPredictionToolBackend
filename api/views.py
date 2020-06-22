import pandas as pd
import numpy as np
import itertools
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import testing_data_raw, training_data_raw, testing_data_input
from .serializers import testing_data_raw_serializer, training_data_raw_serializer, testing_data_input_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

col_names_proc = ['Precinct', 'Congressional District', 'Age', 'Gender', 
    'Early Vote', 'Party']
col_names_input = ['ID', 'Precinct', 'Congressional District', 'Age', 'Gender', 
    'Early Vote', 'Party']
col_names_test = ['Precinct', 'Congressional District', 'Age', 'Gender', 'Party']

# machine learning model
def naive_bayes(data):
    # convert data into pandas dataframe
    training_data = process_training_data()
    testing_data = process_testing_data(data)
    

    # convert dataframes into numpy arrays
    x_train = np.array(training_data.drop("Early Vote", axis=1))
    y_train = np.array(training_data['Early Vote']).astype('int')
    x_test = np.array(testing_data.drop(['Early Vote', 'ID'], axis=1))

    print(np.shape(x_train))
    print(np.shape(y_train))
    print(np.shape(x_test))


    # instantiate a Gaussian Naive Bayes Model
    gnb = GaussianNB()

    y_gnb = gnb.partial_fit(x_train, y_train, np.unique(y_train))

    results = gnb.predict_proba(x_test)[: , [1]]
    result_string = '%s.%s%%' % (str(results)[4:6], str(results)[6:8])

    print(result_string)

    return result_string
    # df_results = pd.DataFrame(data=results)
    # print(results)
    # testing_data['Early Vote Probability'] = df_results


# process raw data into usable data for model training
def process_training_data():
    df_result = pd.DataFrame(columns=col_names_proc)
    ev_dict = {"Y": 1, "N": 0}
    age_dict = {"18-34": 1, "35-44": 2, "45-54": 3, "55-64": 4, "65-74": 5, "75-84": 6, "Over 85": 7}
    gender_dict = {"M": 1, "F": 2, "U": 3}
    party_dict = {"DEM": 1, "REP": 2, "LBT": 3, "GRN": 4, "OTH": 5}
    temp_ind = 1
    data = training_data_raw.objects.all().values_list()
    df = pd.DataFrame(data=data, columns=col_names_input)

    # convert values into int datatypes 
    for index, row in df.iterrows():
        pct = int(row['Precinct'])
        cd = int(row['Congressional District'])
        age = age_dict[row['Age']]
        gender = gender_dict[row['Gender']]
        ev = ev_dict[row['Early Vote']]
        party = party_dict[row['Party']]
        df_result.loc[temp_ind] = [pct, cd, age, gender, ev, party]
        temp_ind = temp_ind + 1
    
    return df_result

def process_testing_data(data):
    df_result = pd.DataFrame(columns=col_names_input)
    ev_dict = {"Y": 1, "N": 0}
    age_dict = {"18-34": 1, "35-44": 2, "45-54": 3, "55-64": 4, "65-74": 5, "75-84": 6, "Over 85": 7}
    gender_dict = {"M": 1, "F": 2, "U": 3}
    party_dict = {"DEM": 1, "REP": 2, "LBT": 3, "GRN": 4, "OTH": 5}
    temp_ind = 1
    # data = testing_data_input.objects.get(user_id=user_id)
    
    # extract data
    id = int(data['user_id'])
    pct = int(data['precinct'])
    cd = int(data['CD'])
    age = age_dict[data['age']]
    gender = gender_dict[data['gender']]
    ev = None
    party = party_dict[data['party']]

    df_result.loc[temp_ind] = [id, pct, cd, age, gender, ev, party]
    temp_ind = temp_ind + 1
    print(df_result)
    return df_result
        

@api_view(['GET', 'POST'])
def testing_data_raw_list(request):

    if request.method == 'GET':
        data = testing_data_raw.objects.all()
        serializer = testing_data_raw_serializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = testing_data_raw_serializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def testing_data_input_list(request):
    print(request.data)
    if request.method == 'GET':
        data = testing_data_input.objects.all()
        serializer = testing_data_input_serializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['early_vote'] = naive_bayes(request.data)
        serializer = testing_data_input_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def testing_data_input_detail(request, user_id):

    try:
        data = testing_data_input.objects.get(user_id=user_id)
    except: 
        testing_data_input.DoesNotExist(status=404)

    if request.method == 'GET':
        serializer = testing_data_input_serializer(data) 
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = training_data_input_serializer(data=data)

        if serializer.is_valid():
            naive_bayes(user_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def training_data_raw_list(request):

    if request.method == 'GET':
        data = training_data_raw.objects.all()
        serializer = training_data_raw_serializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = testing_data_raw_serializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def testing_data_raw_detail(request, pk):
    try:
        data = testing_data_raw.objects.get(pk=pk)
    except: 
        testing_data_raw.DoesNotExist(status=404)

    if request.method == 'GET':
        serializer = testing_data_raw_serializer(data) 
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = training_data_raw_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)