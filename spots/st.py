
"""
Parses ST code (IEC 61131).

Alternatives:
 - http://www.dabeaz.com/ply/
 - http://pypi.python.org/pypi/grako/3.4.1
 - bues.ch/cms/hacking/awlsim.html
 - http://pydoc.net/Python/awlsim/0.22/awlsim.parser/
 - 

Info:
 - http://www.wseas.us/e-library/conferences/2010/Merida/CIMMACS/CIMMACS-24.pdf
 - 

Created on Fri Oct 17 16:44:37 2014

@author: Christian Wichmann
"""

# future imports for pypeg (see http://fdik.org/pyPEG/index.html)
from __future__ import unicode_literals, print_function

from pypeg2 import word
from pypeg2 import Enum
from pypeg2 import K
from pypeg2 import optional
from pypeg2 import maybe_some
from pypeg2 import List
from pypeg2 import attr
from pypeg2 import Keyword
from pypeg2 import parse


__all__ = ['parse_source', 'execute_source']


# list of all inputs with their current value (true|false)
current_input_image = {}
# list of all outputs with their current value (true|false)
current_output_image = {}
# current program that was parsed when function 'parse_source' was last called
current_program = []


class Output(str):
    grammar = word


class Input(str):
    grammar = word


class Negation(Keyword):
    grammar = Enum(K('not'))


class UnaryExpression(List):
    grammar = optional(Negation), attr("input", Input)


class AndExpression(List):
    grammar = UnaryExpression, maybe_some('and', UnaryExpression)

    def evaluate(self):
        global current_input_image
        list_of_inputs = []
        # find all elements of this expression that are Input
        for x in self:
            value = current_input_image[x.input]
            if 'not' in x:
                list_of_inputs.append(not value)
            else:
                list_of_inputs.append(value)
        return all(list_of_inputs)


class Expression(List):
    grammar = AndExpression, maybe_some('or', AndExpression)

    def evaluate(self):
        list_of_and_expressions = []
        # find all elements of this expression that are AndExpression
        for x in self:
            list_of_and_expressions.append(x)
        return any([a.evaluate() for a in list_of_and_expressions])


class Assignment(List):
    grammar = attr("output", Output), ':=', attr("expression", Expression), ';'


class Program(List):
    grammar = Assignment, maybe_some(Assignment)


def parse_source(source):
    """Parses given source code in ST (IEC 61131) and executes it. For all
    inputs the values from the given imput image are used. The function returns
    an output image with the value of all outputs that appear in the source.

    :param source: string containing the source to be executed
    :param input_image: input image with value of all inputs
    :returns: output image with all output values
    """
    global current_program
    current_program = parse(source, Program)


def execute_source(input_image):
    """Executes the stored source code given at he last call of function 
    'parse_source' with the values from the given imput image. The function
    returns an output image with the value of all outputs that appear in the
    source.

    If no program has been parsed before this function is called an exception
    is raised!

    :param input_image: input image with value of all inputs
    :returns: output image with all output values
    """
    # check whether a program has been already parsed
    global current_program
    if current_program == []:
        raise Exception('No program has been parsed!')
    # set given input image as current image
    global current_input_image
    current_input_image = input_image
    # create and fill output image
    new_output_image = {}
    for assignment in current_program:
        output = assignment.output
        value = assignment.expression.evaluate()
        print('{} -> {}'.format(output, value))
        new_output_image[output] = value
    current_output_image = new_output_image
    return current_output_image


def test_parsing():
    # setup and parse source
    sources = """O1 := I1;
                 O2 := I1 or I2;
                 O3 := not I2;
                 O4 := I1 and I2;
                 O5 := I1 and I2 or I3;"""
    parse_source(sources)
    # setup test cases
    test_cases = {0: {'I1': False, 'I2': False, 'I3': False},
                  1: {'I1': True, 'I2': False, 'I3': False},
                  2: {'I1': False, 'I2': True, 'I3': False},
                  3: {'I1': True, 'I2': True, 'I3': False},
                  4: {'I1': False, 'I2': False, 'I3': True},
                  5: {'I1': True, 'I2': False, 'I3': True},
                  6: {'I1': False, 'I2': True, 'I3': True},
                  7: {'I1': True, 'I2': True, 'I3': True}}
    test_values = {0: {'O1': False, 'O2': False, 'O3': True, 'O4': False, 'O5': False},
                   1: {'O1': True, 'O2': True, 'O3': True, 'O4': False, 'O5': False},
                   2: {'O1': False, 'O2': True, 'O3': False, 'O4': False, 'O5': False},
                   3: {'O1': True, 'O2': True, 'O3': False, 'O4': True, 'O5': True},
                   4: {'O1': False, 'O2': False, 'O3': True, 'O4': False, 'O5': True},
                   5: {'O1': True, 'O2': True, 'O3': True, 'O4': False, 'O5': True},
                   6: {'O1': False, 'O2': True, 'O3': False, 'O4': False, 'O5': True},
                   7: {'O1': True, 'O2': True, 'O3': False, 'O4': True, 'O5': True}}
    # check test cases
    for i in range(len(test_cases)):
        print('Checking: {}'.format(test_cases[i]))
        output = execute_source(test_cases[i])
        # check dicts for equality
        unmatched_item = set(output.items()) ^ set(test_values[i].items())
        if len(unmatched_item):
            raise Exception('Test result invalid!')


if __name__ == '__main__':
    test_parsing()
