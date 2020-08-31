import argparse

def argument_parser():
    parser = argparse.ArgumentParser(
        "django_basic_crud_generator",
    )

    parser.add_argument(
        '--app_name',
        type=str,
        help="Name of the app containing the model",
        required=True
    )

    parser.add_argument(
        '--model_name',
        type=str,
        help="Name of model for make the crud",
        required=True
    )
    
    parser.add_argument(
        '--use_template_layout',
        action='store_true',
        #type=bool,
        help="Set this flag to render templates files using an layout",
        required=False
    )

    args = vars(parser.parse_args())
    
    return args
