import logging
import argparse
import sys
import os


def main():
    #####################################################################
    #            Code for parsing command line arguments                #
    #####################################################################

    # https://docs.python.org/3.7/howto/argparse.html
    # https://docs.python.org/3/library/argparse.html

    # create the arguent parser
    parser = argparse.ArgumentParser(
        description='A description of the cli program')

    # mutually exclusive means that only one option can be supplied. supplying both will result in an error
    group = parser.add_mutually_exclusive_group()

    # "store_true" means that if the argument is provided, the value of the argument is true
    group.add_argument('-v', '--verbose', action='store_true',
                       help='Give more output')
    group.add_argument('-q', '--quiet', action='store_true',
                       help='Give no output')

    # a mandatory argument. we also specified that only integers can be supplied
    parser.add_argument(
        'square', help='This is the help for echo, a mandatory argument of type int', type=int)

    # an argument that accepts multiple value seperated by a comma. the "-" means it is optional
    parser.add_argument(
        '--multiple', help='This optional option accepts multiple options', nargs='*')

    # code for subparsers
    # dest='subparser_name' is used to identify the subparser name
    subparsers = parser.add_subparsers(
        title='List of sub commands', description='A description of all the available sub commmands', help='All the commands', dest='subparser_name')

    # code for subparser command a
    parser_a = subparsers.add_parser('a', help='a help')
    parser_a.add_argument('bar', type=int, help='bar help')
    # a function to call when subparser invoked
    parser_a.set_defaults(func=a_parser)

    # create the parser for the "b" command
    parser_b = subparsers.add_parser('b', help='b help')
    parser_b.add_argument('--baz', help='baz help')
    # a function to call when subparser invoked
    parser_b.set_defaults(func=b_parser)

    # writing the arguments to a variable to be accesed
    args = parser.parse_args()

    # if verbose flag not passed on as an argument, this will disable all logging levels
    if not args.verbose:
        logging.disable(logging.CRITICAL)  # This will disable all logging

    # if quiet flag is enabled, stdout (console output) is written to devnull where data is discarded
    if args.quiet:
        sys.stdout = open(os.devnull, 'a')

    #########################################
    #        Application code below         #
    #########################################

    # prints all the arguments as Namespace object https://docs.python.org/3/library/argparse.html#the-namespace-object
    print("args -->", args)

    # print all the arguments as a dictionary
    print('vars(args) -->', vars(args))

    # identifying if a subparser is invoked. if invoked, call appripriate function
    if 'func' in vars(args):
        print('calling the appropriate function for parser')
        args.func(args)
    else:
        print("no subparser called")

    print('this is the start of the program. This should appear even if verbosity is disabled, unless the quiet option is enabled')

    # below are logging levels with "debug" being the lowest and "critical" being the highest
    logging.debug(
        'The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.')
    logging.info('Used to record information on general events in your program or confirm that things are working at their point in the program.')
    logging.warning(
        'Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.')
    logging.error(
        'Used to record an error that caused the program to fail to do something')
    logging.critical(
        'The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.')


if __name__ == "__main__":
    main()
