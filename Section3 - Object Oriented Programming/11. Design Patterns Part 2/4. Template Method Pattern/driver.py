from template import Template

# Test case handler
test_case = input()

if test_case == "basic_test":
    obj = Template("Test Name")
    obj.display_info()
elif test_case == "validation_test":
    obj = Template("Validation Test")
    print(f"Name: {obj.name}")