import sys

import flynt

file = sys.argv[1]

with open(file, "r") as file:
    content = [
        line
        for line in file.read().splitlines()
        if line and not line.startswith((" ", "\t"))
    ]


for statement in content:
    print("flynt >", statement)
    result, error = flynt.run("<stdin>", statement)

    if error:
        print(error.as_string())
    elif result:
        print(result)
