expected_variable = "c"
actual_variable = "c"

print("Code 2 expects:", expected_variable)
print("Code 1 gives:", actual_variable)

if actual_variable != expected_variable:
    print("CONFLICT DETECTED!")
    exit(1)

print("NO CONFLICT")
