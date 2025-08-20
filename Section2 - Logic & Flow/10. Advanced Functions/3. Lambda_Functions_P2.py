'''
Lambda Functions Part2:

Lambda functions can also include conditional logic using the if-else expression syntax.

Create a basic lambda function with an if-else condition:
    # Format: lambda parameters: value_if_true if condition else value_if_false
    is_adult = lambda age: "Adult" if age >= 18 else "Minor"

Test the lambda function with different values:
    print(is_adult(20))  # Output: "Adult"
    print(is_adult(15))  # Output: "Minor"

You can use more complex conditions as well:

    grade_status = lambda score: "Amazing!" if score == 100 else "Pass" if score >= 60 else "Fail"
    print(grade_status(75))  # Output: "Pass"

'''
