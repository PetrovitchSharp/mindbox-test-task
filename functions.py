def get_members_count(n_customers: int, n_first_id: int) -> dict:
    '''
    Get the number of members of each group

    Args:
        n_customers: Number of customers
        n_first_id: First ID

    Returns:
        Dictionaty {Group number (sum of digits of ID) : Count of members}

    Raises:
        ValueError: If number of customers less than 1 OR first ID is negative
    '''
    def get_sum_fo_digits(num: int) -> int:
        '''
        Get sum of decimal number's digits

        Args:
            num: Decimal non-negative number

        Returns:
            Sum of number's digits

        Raises:
            ValueError: If parameter less than 0
        '''
        if num < 0:
            raise ValueError('Number has to be non-negative integer')

        sum_ = 0

        # At each iteration we get last digit,
        # add it to the sum and divide number by 10
        # to get next digit as long as we have digits
        while num > 0:
            sum_ += num % 10
            num //= 10

        return sum_

    if n_customers < 1:
        raise ValueError('Number of customers must be non-negative integer')

    if n_first_id < 0:
        raise ValueError('ID must be non-negative integer')

    groups_counter = {}

    # For each ID we get it's digit's sum
    for num in range(n_first_id, n_first_id + n_customers):

        sum_of_digits = get_sum_fo_digits(num)

        if groups_counter.get(sum_of_digits, 0) > 0:
            # If we have such sum of digits in dictionary,
            # we increase it's value
            groups_counter[sum_of_digits] += 1
        else:
            # If we don't have such sum of digits in dictionary,
            # we set it equal to 1
            groups_counter[sum_of_digits] = 1

    return groups_counter


def get_members_count_from_zero(n_customers: int) -> dict:
    '''
    Get the number of members of each group (starts from 0)

    Args:
        n_customers: Number of customers

    Returns:
        Dictionaty {Group number (sum of digits of ID) : Count of members}

    Raises:
        ValueError: If number of customers less than 1
    '''
    if n_customers < 1:
        raise ValueError('Number of customers must be non-negative integer')

    # This task can be reduced to the previous
    # setting of the first ID equal to 0
    return get_members_count(n_customers, 0)
