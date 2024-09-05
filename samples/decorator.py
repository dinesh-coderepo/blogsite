def decoroator(f):
    def wrapper():
        print('inside 1')
        f()
        print('inside 2')
    return wrapper

@decoroator
def smile():
    print('Smile')

smile()