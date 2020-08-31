# Django Basic Crud Generator

[![PyPI](https://img.shields.io/pypi/v/Django-Basic-CRUD-Generator.svg)](https://pypi.org/project/Django-Basic-CRUD-Generator/)

* Django Basic CRUD Generator is a simple python script to generate views, templates and tests files for a given Django Model.
* The Script will generate the following files, using as base these [templates files](https://github.com/J-hanks/django_basic_crud_generator/tree/master/django_basic_crud_generator/templates)

```bash
├── APP_NAME
│   ├── templates
│   │   ├── MODEL_NAME
│   │   │   ├── MODEL_NAME_list.html
│   │   │   ├── MODEL_NAME_create.html
│   │   │   ├── MODEL_NAME_detail.html
│   │   │   ├── MODEL_NAME_update.html
│   │   │   ├── MODEL_NAME_delete.html
│   ├── tests
│   │   ├── MODEL_NAME
│   │   │   ├── __init__.py
│   │   │   ├── MODEL_NAME_list_test.py
│   │   │   ├── MODEL_NAME_create_test.py
│   │   │   ├── MODEL_NAME_detail_test.py
│   │   │   ├── MODEL_NAME_update_test.py
│   │   │   ├── MODEL_NAME_delete_test.py
│   ├── views
│   │   ├── MODEL_NAME
│   │   │   ├── __init__.py
│   │   │   ├── MODEL_NAME_list.py
│   │   │   ├── MODEL_NAME_create.py
│   │   │   ├── MODEL_NAME_detail.py
│   │   │   ├── MODEL_NAME_update.py
│   │   │   ├── MODEL_NAME_delete.py
│   │── urls.py
```

## Installation:
Download the repository 
```bash
git clone https://github.com/J-hanks/django_basic_crud_generator.git
```
Install using pip
```bash
pip install django_basic_crud_generator
```
## Usage:
You can call the script anywhere set app_name and model_name options are Required
```bash
python -m django_basic_crud_generator --app_name MY_APP --model_name MY_MODEL
```
You can also import in your python scripts to generate files programatically.
```python
import django_basic_crud_generator
django_basic_crud_generator.generate_files(
    app_name="MyApp",
    model_name="MyModel",
    use_template_layout=True,
    override_templates="MyTemplatesFolder/"
)
```
Options:
- `--app_name`: Your Django application name
- `--model_name`: Your Django model name you want crud generated
- `--use_template_layout`: Set this flag to system render templates files using this [layout file](https://github.com/J-hanks/django_basic_crud_generator/tree/master/django_basic_crud_generator/templates/layout/base.tmpl)
- `--override_templates`: Set the override templates folder. **Ex:**  *--override_templates MY_TEMPLATES_FOLDER*

## Manually fix urls file:
- The urls.py file will need mannualy inspection
- Make sure you included you app urls in your project level urls.py file.
- If you only use project level, copy the contents of generated app urls.py to your project level urls.py file

## Examples
You can see examples of generated files [here](https://github.com/J-hanks/django_basic_crud_generator/tree/master/ExampleApp/)

