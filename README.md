# calculator
> A mathematical calculator

## General Information
- Perform 5 mathematical operators (add, subtract, multiply, divide, take the n-th root) and reset the memory of the calculator istance

## Technologies Used
- Python 3.7

## Features
- Instantiate a calculator object with a dedicated memory for a number
- Adding to the number in memory 
- Subtracting from the number in memory 
- Multiplying the number in memory 
- Dividing the number in memory 
- Taking the n-th root of the number in memory 
- Resetting the calculator memory to 0

## Installation
Run the following to grab the package:
```python
$ pip install -e git+https://github.com/Andriaus/tesla_factory#egg=tesla_factory
```

## Usage
```python
from calculator import calc

calculator = calc.Calculator()
calculator.add(5)
calculator.subtract(-4)
calculator.multiply(-3)
calculator.divide(-1)
calculator.take_root(3)
calculator.reset_memory()
```

## Project Status
No longer worked on, because other projects await

## Room for Improvement
Room for improvement:
- Implement more mathematical functions
- Besides support for real/float numbers add support for the complex numbers
- Add support for multi-dimensional vectors

## Acknowledgements
Turing College

## Contact
Created by [@andriaus](https://github.com/andriaus)

## License
[MIT license](https://opensource.org/licenses/MIT)
