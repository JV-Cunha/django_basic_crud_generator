from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ExampleApp.models import ExampleModel

class ExampleModelCreateView(CreateView):
    model = ExampleModel
    template_name = "example_model/example_model_create.html"
    
     fields = '__all__'
    
     success_url = reverse_lazy('example_model_list')
    