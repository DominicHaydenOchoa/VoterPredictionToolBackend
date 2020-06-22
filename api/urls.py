from django.urls import path
from .views import testing_data_raw_list, training_data_raw_list, testing_data_raw_detail, testing_data_input_detail, testing_data_input_list

urlpatterns = [
    path('testing_data_raw/', testing_data_raw_list),
    path('testing_data_input/', testing_data_input_list),
    path('testing_data_input/<int:user_id>/', testing_data_input_detail),
    path('detail/testing_data_raw/<int:pk>/', testing_data_raw_detail),
    path('training_data_raw/', training_data_raw_list),


]