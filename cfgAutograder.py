# CFG used as the base of the code
#
# <program> ::= <statement> | <statement> <program>
# <statement> ::= <assignment> | <if_statement> | <while_statement> | <for_statement> | <function_definition> | <expression_statement>
# <assignment> ::= <identifier> "=" <expression> "\n"
# <if_statement> ::= "if" <expression> ":" <block> ["elif" <expression> ":" <block>] ["else:" <block>]
# <while_statement> ::= "while" <expression> ":" <block>
# <for_statement> ::= "for" <identifier> "in"  <literal>":"<block>
# <function_definition> ::= "def" <identifier> "(" [<parameter_list>] ")" ":" <block>
# <block> ::= <statement> | <statement> <block>
# <expression_statement> ::= <expression> "\n"
# <expression> ::= <identifier> | <literal> | <expression> <operator> <expression>
# <parameter_list> ::= <identifier> | <identifier> "," <parameter_list>
# <identifier> ::= <letter> [<letter> | <digit>]*
# <literal> ::= <integer_literal> | <string_literal>
# <integer_literal> ::= <digit>+
# <string_literal> ::= '"' <character>* '"'
# <operator> ::= "+" | "-" | "*" | "/" | "==" | "!=" | "<" | ">"
# <letter> ::= "a" | "b" | "c" | ... | "z" | "A" | "B" | ... | "Z"
# <digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
# <character> ::= <letter> | <digit> | <punctuation> | " "
# <punctuation> ::= "," | "." | "!" | "?"


# stores syntax errors in this array
errors = []
# stores logical issues in this array
logical_issues = []
# stores the keywords in this array
control_structures = ('if', 'else', 'elif', 'for', 'while', 'def')


# checks the syntax of the code and adds the type of issue to the array
def check_syntax(code):
    # splits the code into a list of different lines
    lines = code.splitlines()
    # counts the number of parenthesis to check if there is a syntax error
    if code.count('(') != code.count(')'):
        errors.append("Syntax Error: Unmatched parentheses")
    # for loop to go through the index number and individual lines at the same time
    for index, line in enumerate(lines):
        # removes any whitespaces in the line
        stripped_line = line.strip()

        # checks if there is a syntax error due to not adding colon after the structures also returns the line number
        if stripped_line.startswith(control_structures) and not stripped_line.endswith(':'):
            errors.append("Syntax Error: Missing colon (:) after control structure in line: " + str(index + 1))

        # checks if there is an indentation after the control structures also returns the line number
        if stripped_line.startswith(control_structures) and not lines[index + 1].startswith('    '):
            errors.append("Syntax Error: Code should be indented after control structures in line: " + str(index + 1))

        # checks if there is an assignment operation going on in the if statement instead of comparison
        if 'if' in stripped_line and '=' in stripped_line and '==' not in stripped_line and '!=' not in stripped_line:
            parts = stripped_line.split('if')
            if len(parts) > 1 and '=' in parts[1]:
                errors.append("Syntax Error: Incorrect assignment in 'if' statement in line: " + str(index + 1))


# checks the logic of the code for common logic warning
def check_logic(code):
    # splits each line of code into a list
    lines = code.splitlines()
    # array list to store initialized variables
    initialized_variables = []
    # loop to iterate through the lines
    for line in lines:
        # removes the whitespace from the lines
        stripped_line = line.strip()
        # appends the variable before the assignment operation to the initialized variable list
        if '=' in stripped_line:
            # appends the variable names to the list
            variable = stripped_line.split('=')[0].strip()
            initialized_variables.append(variable)

    # counts if the def and return are equal to check if the functions have returns
    if code.count("def") != code.count("return"):
        logical_issues.append("Logical Issue: Possible error as the function does not return any value")

    # to iterate through the lines
    for line in lines:
        stripped_line = line.strip()

        # checks to tell there is a possibility of an infinite loop
        if stripped_line.startswith('while True:'):
            logical_issues.append("Logical Issue: Potential infinite loop found")

        # checks to see if the 'if' statement is executed properly
        if stripped_line.startswith('if') and 'print(' in stripped_line:
            logical_issues.append("Logical Issue: Check the condition in 'if' statement")

        # checks if the variable names are in the initialized variable list else it says the variable is not initialized
        if stripped_line.startswith('if'):
            # gets only the condition part of the if statement
            condition = stripped_line.split('if')[1].split(':')[0].strip()
            # splits the condition into tokens and replaces the operators with spaces
            tokens = condition.replace('==', ' ').replace('!=', ' ').replace('>', ' ').replace('<', ' ').split()

            # iterates through the tokens
            for token in tokens:
                # checks if token is an identifier and not initialized then appends the issue if it isn't initialized
                if token.isidentifier() and token not in initialized_variables:
                    logical_issues.append(f"Logical Issue: Uninitialized variable '{token}' used")


# function to print the analysis reports
def report():
    # prints the syntax errors if arrays is not empty
    if errors:
        print("Errors Found:")
        for error in errors:
            print(error)
    # else prints that there were no errors
    else:
        print("No syntax errors found")

    # prints the logical errors if arrays is not empty
    if logical_issues:
        print("Logical Issues Found:")
        for logical_issue in logical_issues:
            print(logical_issue)
    # else prints that there were no errors
    else:
        print("No logical issues were found")


# converts the code from a text file to a string
def code_conversion(filename):
    # opens the file as a variable f
    f = open(filename, "rt")
    s = ""
    # iterates through the lines and add them to the string
    for lines in f:
        s += lines
    # completed string is returned
    return s


# analyses the code to check for syntax and logical errors
def analyse_code(code):
    # checks for syntax and logic
    check_syntax(code)
    check_logic(code)
    # prints the analysis report with errors
    report()


# calls the function to analyse the code
# analyse_code(code_conversion())
