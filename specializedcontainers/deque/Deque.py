from collections import deque
import string
#creates a deque and fills it with lowercase characters
d = deque(string.ascii_lowercase)
for element in d:
    print(element)

print()
print()
print()
print()
print()
print()

#creates a deque and fills it with the last n lines from the given file
def read_n_lines(filename, n):
    """
    Returns the last n lines from the file
    """
    try:
        with open(filename) as f:
            #creates a deque and give a file handler. Also, define the upper bound limit for the deque
            deq = deque(f, n)
            return deq
    except OSError:
        print("Error opening file {}".format(filename))
        raise

lines = read_n_lines(filename = "../defaultdict/DefaultDict.py", n = 50)
print(lines)
print()