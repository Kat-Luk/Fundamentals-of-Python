def read_contents( path ):
    try:
        file = open(path,"r")
        lines = []
        for line in file:
            return line
    except FileNotFoundError:
        return None
