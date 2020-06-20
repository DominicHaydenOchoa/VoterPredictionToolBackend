from django.urls import path
from .views import testing_data_raw_list, training_data_raw_list

urlpatterns = [
    path('testing_data_raw/', testing_data_raw_list),
    path('training_data_raw/', training_data_raw_list)

]