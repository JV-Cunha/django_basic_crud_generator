from django.views.generic import ListView

from ExampleApp.models import ExampleModel

class ExampleModelListView(ListView):
    model = ExampleModel
    template_name = "example_model/example_model_list.html"
