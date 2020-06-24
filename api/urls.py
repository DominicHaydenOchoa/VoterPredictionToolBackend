from django.urls import path
from .views import testing_data_list, training_data_list, testing_data_input_detail, testing_data_input_list, testing_data_results_list, account_verif

urlpatterns = [
    path('login/', account_verif),
    path('testing_data/', testing_data_list),
    path('testing_data_input/', testing_data_input_list),
    path('testing_data_input/<int:user_id>/', testing_data_input_detail),
    path('training_data/', training_data_list),
    path('testing_data_results/<int:session_id>/', testing_data_results_list)


]