""" Django Basic CRUD Generator """
import os
import codecs
import string
import re
import pathlib
from .argumentParser import argument_parser


def camel_case_to_underscore(name):
    """
    This function camel_case_to_underscores a Camel Case word to a underscore word
    """
    temp = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', temp).lower()

def is_file(file_name):
    """ Simple shortcut to check if file exist  """
    return os.path.isfile(file_name)


def read_file(file_path):
    """ Red the file and return its content """
    return "".join(
        codecs.open(
            file_path,
            encoding='UTF-8'
        ).readlines()
    )


def prepend_to_file(file_path, content):
    """ Add content to begin of the file  """
    file = open(file_path, 'r+', encoding='utf-8')
    lines = file.readlines()
    file.seek(0)
    file.write(content)
    for line in lines:  # write old content after new
        file.write(line)
    file.close


def append_to_file(file_path, content):
    """ Add Content to the end of file """
    file = open(file_path, 'a+', encoding='utf-8')
    #lines = file.readlines()
    file.write(content)
    # for line in lines:  # write old content after new
    #    file.write(line)
    file.close


def is_folder(folder_name):
    """ Simple shortcut to check if folder exist  """
    return os.path.isdir(folder_name)


def create_folder_if_not(folder):
    """ Check if folder exists and create one if not """
    if is_folder(folder):
        print("%s exists" % folder)
    else:
        print("%s created" % folder)
        os.mkdir(folder)


def open_or_create_file(file):
    """ Check if file exists and return it,
    create a new one if not and return the new created one """
    if is_file(file):
        print("%s exists" % file)
        return codecs.open(file, 'a+')
    else:
        print("%s created" % file)
        return codecs.open(file, 'w+')


def execute_from_command_line():

    args = argument_parser()

    app_name = args['app_name']
    model_name = args['model_name']
    model_name_underscore = camel_case_to_underscore(model_name)


    components = [
        "views",
        "templates",
        "tests",
    ]

    crud_items = [
        "list",
        "create",
        "detail",
        "update",
        "delete"
    ]

    # Create app folder with given app_name if there is no one
    create_folder_if_not(app_name)

    for component in components:
        # Create component folder inside app folder 
        create_folder_if_not(os.path.join(app_name, component))
        # Create model folder inside component folder
        create_folder_if_not(os.path.join(
            app_name, component, model_name_underscore))

        # Create __init__.py files in views and tests directories
        if component != "templates":
            # Create __init__.py file inside component folder 
            open_or_create_file(os.path.join(
                app_name, component, "__init__.py"))
            # Create __init__.py file inside model folder of current component
            open_or_create_file(os.path.join(
                app_name, component, model_name_underscore, "__init__.py"))

        for crud_item in crud_items:
            real_path = pathlib.Path(__file__).parent.absolute()
            template_file_path = os.path.join(real_path,"templates",component,(crud_item+".tmpl"))
            template_file_content = read_file(template_file_path)
            template_rendered = string.Template(template_file_content).safe_substitute(
                app_name=app_name,
                model_name=model_name,
                model_name_u_lower=model_name_underscore,
                model_name_lower=model_name.lower()
            )
            # Views and Tests files have py suffix
            crud_item_file_name = ("{}_{}.py".format(
                model_name_underscore, crud_item))
            # If component is template files must end with html suffix
            if component == "templates":
                crud_item_file_name = ("{}_{}.html".format(
                    model_name_underscore, crud_item))
            if component == "tests":
                crud_item_file_name = ("{}_{}_test.py".format(
                    model_name_underscore, crud_item))
            crud_item_file_path = os.path.join(
                app_name, component, model_name_underscore, crud_item_file_name)
            file = open_or_create_file(crud_item_file_path)
            file.write(template_rendered)
            file.close()

            # Import Created classes to init.py files
            if component != "templates":
                model_init_file_path = os.path.join(
                    app_name, component, model_name_underscore, "__init__.py")
                prepend_content = ("from ." +
                                   model_name_underscore + "_"+crud_item +
                                   " import " +
                                   model_name+crud_item.capitalize()+component[:-1].capitalize()+"\n")
                prepend_to_file(model_init_file_path, prepend_content)

                component_init_file_path = os.path.join(
                    app_name, component, "__init__.py")
                prepend_content = ("from ." +
                                   model_name_underscore +
                                   " import " +
                                   model_name+crud_item.capitalize()+component[:-1].capitalize()+"\n")
                prepend_to_file(component_init_file_path, prepend_content)

            # Generate urls.py content
            if component == "views":
                urls_file_path = os.path.join(app_name, "urls.py")
                open_or_create_file(urls_file_path)
                prepend_view_import_content = (
                    "from " + app_name + "." + component +
                    " import " + model_name + crud_item.capitalize() + "View\n"
                )
                append_view_path_content = ("path('" + model_name_underscore + "/" + crud_item + "', " +
                                            model_name + crud_item.capitalize() + "View.as_view(), name='" +
                                            model_name_underscore + "_" + crud_item + "')\n"
                                            )
                print(prepend_view_import_content + " ADD TO "+urls_file_path)
                prepend_to_file(urls_file_path, prepend_view_import_content)
                print(append_view_path_content + " ADD TO "+urls_file_path)
                append_to_file(urls_file_path, append_view_path_content)

def __main__():
    execute_from_command_line()