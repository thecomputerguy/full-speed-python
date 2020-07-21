from contextlib import redirect_stdout

with open('text.txt', 'w') as f:
    with redirect_stdout(f):
        help(redirect_stdout)
        
print('data to file has been written')