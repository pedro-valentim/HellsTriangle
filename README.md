# HellsTriangle

This repo is for solving the problem below.

Given a triangle of numbers, find the maximum total from top to bottom

Example:

```text
      6
     3 5
    9 7 1
   4 6 8 4
```

In this triangle the maximum total is: 6 + 5 + 7 + 8 = 26
An element can only be summed with one of the two nearest elements in the next row.
For example: The element 3 in the 2nd row can only be summed with 9 and 7, but not with
1

Your code will receive an (multidimensional) array as input.
The triangle from above would be:
example = [[6],[3,5],[9,7,1],[4,6,8,4]]

## How to run

- First clone or download this repo:
```sh
git clone https://github.com/pedro-valentim/HellsTriangle
```

- Enter directory and execute the command below to see usage
```sh
python hellstriangle.py --help
```
```text
usage: hellstriangle.py [-h] triangle

Given a triangle of numbers, find the maximum total from top to bottom.

positional arguments:
  triangle    The triangle to find the max sum in a path. e.g.
              "[[6],[3,5],[9,7,1],[4,6,8,4]]" (with quotes)

optional arguments:
  -h, --help  show this help message and exit

```

## How to run tests

- Dependecies

	 - pytest (`pip install pytest`)

- Running tests
```sh
 pytest test.py
```
