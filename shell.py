import flynt

while True:
    text = input("flynt > ")
    result, error = flynt.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        print(result)
