import argparse

def argument_parser():
    parser = argparse.ArgumentParser(
        "DjangoBasicCrudGenerator",
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

    args = vars(parser.parse_args())
    
    return args
