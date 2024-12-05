# List to check
data = [1, "hello", 42, "world", 3.14]

# Lambda function to check type
check_type = lambda x: "Integer" \
    if isinstance(x, int) \
      else "String" \
        if isinstance(x, str)\
             else "Other"

# Apply the lambda function to each element in the list
results = [check_type(item) for item in data]

# Output the results
print(results)

