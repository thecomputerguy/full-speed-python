from contextlib import redirect_stdout
from io import StringIO

stream = StringIO()
write_to_stream = redirect_stdout(stream)

with write_to_stream:
    print('writing to the stream')
    with write_to_stream:
        print('writing again to the stream')

print(stream.getvalue())
print()