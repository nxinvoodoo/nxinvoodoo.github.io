from global_val import global_value, change_global_value
print('befor fun',global_value)  # Outputs: 10
change_global_value(20)
print('after fun',global_value)  # Outputs: 20
