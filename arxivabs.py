import re
# Extract Subjects
def extract_and_format(input_str):
    return (', '.join(re.findall(r'\((.*?)\)', input_str)) + ', ')
print(extract_and_format(input("Enter Subjects: ")))