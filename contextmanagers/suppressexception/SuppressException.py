from contextlib import suppress

#with suppress exception
with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

print("suppressed exception")
print()
print()

print('Running without suppress and it should raise exception FileNotFoundException')
print()
print()
#without suppressing exception
with open('fauxfile.txt') as f:
    for line in f:
        print(line)