def process(filters=None, limit=1000, offset=0):
    
    def fibbonaci(filters, max_count):
        result = []

        """
            •[filter(number) for filter in filters] -> [b_1, b_2, b_3, ...] -> [True/False, True/False, True/False, ...]
                Where b_i is the result of i-th filter function applied to the number
                If all b_i is True, then the number is considered valid and will be added to the result list
            •If we have no filters, then all numbers will be considered as valid
        """

        if (False in [filter(0) for filter in filters] if filters else True):
            result.append(0)
            max_count -= 1

        if max_count > 0 and (False not in [filter(1) for filter in filters] if filters else True):
            result.append(1)
            max_count -= 1

        a, b = 0, 1
        while max_count > 0:
            number = a + b
            is_valid = False not in [filter(number) for filter in filters] if filters else True

            if is_valid:
                result.append(number)
                max_count -= 1
                
            a, b = b, a + b

        return result

    if limit < 0:
        assert limit > 0, 'Limit must be greater or equal than 0!'

    if limit == 0:
        return []
    
    if offset < 0:
        assert offset >= 0, 'Offset must be greater or equal to 0!'

    return fibbonaci(filters=filters, max_count=(limit + offset))[offset:]

def sum_digits(x):
    return sum(map(int, str(x)))

try:
    print(process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=2,
        offset=2
    ))
except Exception as e:
    print(e)