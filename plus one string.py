def plus_one_string(num_str):
    num = int(num_str) + 1       
    return [int(d) for d in str(num)]  

num_str = input("Enter a number string: ")  
result = plus_one_string(num_str)
print("Output:", result)
