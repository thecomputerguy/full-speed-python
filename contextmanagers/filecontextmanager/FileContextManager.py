from contextlib import contextmanager

@contextmanager
def file_handle(path):
    try:
        f = open(path, 'w')
        yield f            
    except OSError:
        print("we had an error!")
    finally:
        f.close()

if __name__ == "__main__":
    with file_handle("./data.txt") as handler:
        handler.write('throwing some text in file')
        


