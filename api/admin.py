from django.contrib import admin
from .models import  testing_data, training_data, testing_data_input, testing_data, testing_data_result

# Register your models here.

admin.site.register(testing_data)
admin.site.register(training_data)
admin.site.register(testing_data_input)
admin.site.register(testing_data_result)