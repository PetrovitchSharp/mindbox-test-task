import argparse

from functions import get_members_count, get_members_count_from_zero


def make_parser() -> argparse.ArgumentParser:
    '''
    Make cli arguments parser

    Returns:
        CLI args parser
    '''

    parser = argparse.ArgumentParser(
        description='Get count of group\'s members'
    )

    parser.add_argument(
        '-n_customers',
        type=int,
        default=1,
        help='Number of customers'
    )

    parser.add_argument(
        '-n_first_id',
        type=int,
        default=0,
        help='First ID of sequence'
    )

    parser.add_argument(
        '-mode',
        type=str,
        default='from_zero',
        help='Operating mode (possible values: from_zero, from_id)'
    )

    return parser


def sort_dict_by_keys(dct: dict) -> dict:
    '''
    Sort dictionary by keys increasing

    Args:
        dct: Dictionaty to sort

    Returns:
        Dictionary sorted by keys
    '''
    sorted_keys = sorted(dct)

    return {key: dct[key] for key in sorted_keys}


def print_dict(dct: dict) -> None:
    '''
    Print dictionary as table

    Args:
        dct: Dictionary to print
    '''
    print('Group\t||\tCount')
    print('--------||-----------')

    sorted_dct = sort_dict_by_keys(dct)

    for key in sorted_dct.keys():
        print(f'{key}\t||\t{dct[key]}')


def main() -> None:
    # CLI arguments parsing
    parser = make_parser()
    args = parser.parse_args()

    mode = args.mode
    n_customers = args.n_customers
    n_first_id = args.n_first_id

    # Running script in chosen mode
    match mode:
        case 'from_zero':
            print_dict(get_members_count_from_zero(n_customers))

        case 'from_id':
            print_dict(get_members_count(n_customers, n_first_id))

        case _:
            print('No such mode')


if __name__ == '__main__':
    main()
