# Django Basic Crud Generator
* Django Basic CRUD Generator is a simple python script to generate views, templates and tests files for a given Django Model.
* The Script will generate the following files, using as base the templates inside django_basic_crud_generator/templates

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
You must set app_name and model_name options
```bash
python -m django_basic_crud_generator --app_name YOUR_APP --model_name YOUR_MODEL
```
Options:
- `--app_name`: Your Django application name
- `--model_name`: Your Django model name you want crud generated

## Manually fix urls file:
- The urls.py file will need mannualy inspection

