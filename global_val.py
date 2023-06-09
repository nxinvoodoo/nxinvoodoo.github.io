global_value = 10
def change_global_value(new_value):
    global global_value
    print('befor',global_value)
    global_value = new_value
    print('after',global_value)
