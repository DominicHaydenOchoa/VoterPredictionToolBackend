from django.urls import path
from .views import testing_data_list, training_data_list, testing_data_input_detail
from .views import testing_data_input_list, testing_data_results_list, account_verif, training_data_count
from .views import testing_data_count, testing_data_results_count, testing_data_results_all

urlpatterns = [
    path('login/', account_verif),
    path('testing_data/', testing_data_list),
    path('testing_data_input/', testing_data_input_list),
    path('training_data/', training_data_list),
    path('testing_data_results/', testing_data_results_list),
    path('training_data_count/', training_data_count),
    path('testing_data_count/', testing_data_count),
    path('testing_data_results_count/', testing_data_results_count),
    path('testing_data_results_all/', testing_data_results_all),


]