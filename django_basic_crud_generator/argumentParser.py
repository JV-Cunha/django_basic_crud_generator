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

    parser.add_argument(
        '--override_templates',
        type=str,
        #type=bool,
        help="Set this flag to render templates files using an layout",
        required=False,
        default=None
    )

    args = vars(parser.parse_args())
    
    print("")
    print("Django Basic Crud Generator\n")
    print("app_name:\t\t"+str(args['app_name']))
    print("model_name:\t\t"+str(args['model_name']))
    print("use_template_layout:\t"+str(args['use_template_layout']))
    print("override_templates:\t"+str(args['override_templates']))
    print("")

    return args
