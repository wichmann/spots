
"""
Parses ST code (IEC 61131). This module uses the pyPEG parser for parsing and
executing ST code (http://fdik.org/pyPEG/).

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

import logging
import re

from pypeg2 import attr
from pypeg2 import optional
from pypeg2 import maybe_some
from pypeg2 import Enum
from pypeg2 import List
from pypeg2 import Keyword
from pypeg2 import K
from pypeg2 import parse


__all__ = ['parse_source', 'execute_source']


logger = logging.getLogger('spots.st')


# list of all inputs with their current value (true|false)
current_input_image = {}
# list of all outputs with their current value (true|false)
current_output_image = {}
# current program that was parsed when function 'parse_source' was last called
current_program = []


class Output(Keyword):
    regex = re.compile(r"O{1}[0-9]+")


class Input(Keyword):
    regex = re.compile(r"I{1}[0-9]+")


class Negation(Keyword):
    grammar = Enum(K('not'))


class ConstantTrue(Keyword):
    grammar = Enum(K('true'))


class ConstantFalse(Keyword):
    grammar = Enum(K('false'))


class UnaryExpression(List):
    grammar = optional(Negation), [ConstantTrue, ConstantFalse, Input]


class AndExpression(List):
    grammar = UnaryExpression, maybe_some('and', UnaryExpression)

    def evaluate(self):
        global current_input_image
        list_of_inputs = []
        # find all elements of this expression that are Input or Constants
        for x in self:
            for y in x:
                if type(y) is ConstantTrue:
                    value = True
                elif type(y) is ConstantFalse:
                    value = False
                elif type(y) is Input:
                    value = current_input_image[y]
            if Negation('not') in x:
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


class BlockComment(str):
    grammar = '(*', str, '*)'
    #grammar = re.compile(r"(?m)\(\*.*?\*\)")


class Program(List):
    grammar = maybe_some(Assignment)
    #grammar = some([optional(BlockComment), optional(Assignment)])


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
        if type(assignment) == Assignment:
            output = assignment.output
            value = assignment.expression.evaluate()
            logger.debug('{} -> {}'.format(output, value))
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
    logger.info('===== Testing simple logical terms =====')
    for i in range(len(test_cases)):
        logger.info('Checking: {}'.format(test_cases[i]))
        output = execute_source(test_cases[i])
        # check dicts for equality
        unmatched_item = set(output.items()) ^ set(test_values[i].items())
        if len(unmatched_item):
            raise Exception('Test result invalid!')


def test_parsing_2():
    # setup and parse source
    sources = """O1 := true;
                 O2 := false;
                 O3 := not true;
                 O4 := not false;
                 O5 := true and false;
                 O6 := true and true;
                 O7 := true or false;
                 O8 := false or not false;
                 O9 := true or true;"""
    parse_source(sources)
    # setup test cases    
    test_values = {'O1': True,
                   'O2': False,
                   'O3': False,
                   'O4': True,
                   'O5': False,
                   'O6': True,
                   'O7': True,
                   'O8': True,
                   'O9': True}
    logger.info('===== Testing negation and boolean constants =====')
    output = execute_source(dict())
    # check dicts for equality
    unmatched_item = set(output.items()) ^ set(test_values.items())
    if len(unmatched_item):
        raise Exception('Test result invalid!')


def test_syntax():
    logger.info('===== Testing simple syntaxtical terms =====')
    logger.info('To be implemented!!! - Have to catch Exceptions when Syntax is invalid!')


if __name__ == '__main__':
    test_parsing()
    test_parsing_2()
    test_syntax()

