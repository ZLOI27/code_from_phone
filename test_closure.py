def wrapper(arg):
    x = arg
    print('init closure x=', x)
    def add(x_plus=1):
        nonlocal x 
        x += x_plus
        print('x=', x)

    def set_x(new_x):
        nonlocal x
        x = new_x
        print('new_x=', x)

    def get_atr():
        return [add, set_x, x]
    return get_atr


