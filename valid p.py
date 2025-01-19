def is_valid_parentheses(expression):
    # Stack to keep track of opening brackets
    stack = []

    for char in expression:
        if char in "({[":  # If it's an opening bracket
            stack.append(char)
        elif char in ")}]":  # If it's a closing bracket
            if not stack:
                return False
            # Check if the last opening bracket matches the closing bracket
            last_open = stack.pop()
            if (char == ')' and last_open != '(') or \
               (char == '}' and last_open != '{') or \
               (char == ']' and last_open != '['):
                return False

    return not stack