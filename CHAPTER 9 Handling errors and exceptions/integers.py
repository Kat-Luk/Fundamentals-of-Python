def get_integers_from_stdin():
    lst = []
    while True:
        try:
            items = int(input("Enter an integer:"))
            lst.append(items)
        except KeyboardInterrupt:
            break
    return lst
