import sys
# Set sys.set_int_max_str_digits to 9999 to give more digits (default is 4300)
sys.set_int_max_str_digits(9999)
print("Calculator Shell - Type 'exit' to quit.")
# REPL
while True:
    user_input = input(">>>")
    if user_input.lower in ['exit', 'quit', 'bye']:
        break
    try:
        # eval() processes the string as a math expression
        result = eval(user_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

