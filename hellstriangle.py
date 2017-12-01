import argparse

DESCRIPTION = 'Given a triangle of numbers, find the maximum total from top to bottom.'
TRIANGLE_ARG_HELP = '''The triangle to find the max sum in a path.
    e.g. "[[6],[3,5],[9,7,1],[4,6,8,4]]" (with quotes)'''


class TriangleException(Exception):
    pass


class StoreAsBidimensionalArray(argparse._StoreAction):
    def __call__(self, parser, namespace, value, option_string=None):
        try:
            rows = value.replace(' ', '')[2:-2].split('],[')
            bidimensional_array = [list(map(int, row.split(','))) for row in rows]
        except ValueError:
            raise TriangleException(
                'Could not parse triangle. Run python hellstriangle.py -h for help string.')

        return super().__call__(parser, namespace, bidimensional_array, option_string)


class Triangle(object):

    def __init__(self, triangle):
        self.triangle = self.validate(triangle)
        self._max_sum = None

    def validate(self, triangle):
        # if triangle is an empty list than it's valid
        if len(triangle) == 0:
            return triangle

        # list the length of each row
        lengths = [len(row) for row in triangle]

        # check if it starts with only one number
        if lengths[0] != 1:
            raise TriangleException('Triangle top does not have only one number.')

        # check if the length of each row is sequential
        if not all(_num + 1 == _num_next for _num, _num_next in zip(lengths, lengths[1:])):
            raise TriangleException('Triangle does not have a valid structure.')

        return triangle

    @property
    def max_sum(self):
        if len(self.triangle) != 0:
            self._find_max_sum()

        return self._max_sum or 0

    def _find_max_sum(self, current_summing=0, row_index=0, col_index=0):

        # sums previous summing with current number
        # or first number with zero (default current_summing)
        current_summing += self.triangle[row_index][col_index]

        # gets if summing with number in last row
        is_last = len(self.triangle) == row_index + 1

        if is_last is True and (self._max_sum is None or current_summing > self._max_sum):
            # if it is the last row and the sum at this point is greater
            # than current max: sets as current max sum
            self._max_sum = current_summing
        elif is_last is False:
            # if it is NOT the last row then call it for left and right leafs
            self._find_max_sum(current_summing, row_index + 1, col_index)
            self._find_max_sum(current_summing, row_index + 1, col_index + 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        'triangle',
        action=StoreAsBidimensionalArray,
        type=str,
        help=TRIANGLE_ARG_HELP)

    try:
        args = parser.parse_args()
        max_total = Triangle(args.triangle).max_sum
        print('In this triangle the maximum total is: {} = {}'.format('', max_total))
    except TriangleException as e:
        print(e)
