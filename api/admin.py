from django.contrib import admin
from .models import  testing_data_raw, training_data_raw, testing_data_input

# Register your models here.

admin.site.register(testing_data_raw)
admin.site.register(training_data_raw)
admin.site.register(testing_data_input)