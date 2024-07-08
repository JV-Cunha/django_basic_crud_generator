from django.views.generic.edit import ListView
from django.urls import reverse_lazy

from ExampleApp.models import ExampleModel

class ExampleModelListView(ListView):
    model = ExampleModel
    template_name = "example_model/example_model_list.html"
    
     //
    