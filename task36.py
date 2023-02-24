def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        ans = []
        for j in range(1, num_columns + 1):
            ans.append(str(operation(i, j)))
        print("\t".join(ans))
 
 
print_operation_table(lambda x, y: x * y)