from contextlib import ExitStack

filenames = ['data.txt', 'dump.txt', 'contacts.txt']
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename)) for filename in filenames]
    print(file_objects)