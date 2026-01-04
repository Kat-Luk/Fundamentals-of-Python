def triangle_area(b,h):
    if b <= 0 or h <= 0:
        raise ValueError
    else:
        area = (float(b)*float(h))/2
        return area

    
