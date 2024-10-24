import argparse
import logging
from cli.generate_identities import main as generate_identities_main
from cli.convert_files import main as convert_files_main
from cli.generate_identities import parse_args as generate_identities_parse_args
#from cli.convert_files import parse_args as convert_files_parse_args

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description="Utility for generating identities and converting files")
    subparsers = parser.add_subparsers(help='Sub-command help')

    # Sub-command for generating identities
    parser_generate = subparsers.add_parser('generate', help='Generate fake identities')
    parser_generate.set_defaults(func=lambda args: generate_identities_main(generate_identities_parse_args(vars(args))))

    # Sub-command for converting files
    parser_convert = subparsers.add_parser('convert', help='Convert files between different formats')
    parser_convert.set_defaults(func=convert_files_main)

    args = parser.parse_args()
    args.func()
    
if __name__ == "__main__":
    main()