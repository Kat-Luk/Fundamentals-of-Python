def analyze_courses(course_a, course_b):
    a = course_a.union(course_b)
    b = course_a.intersection(course_b)
    if b == set():
        c = True
    else:
        c = False
    d = course_a.difference(course_b)
    e = course_b.difference(course_a)
    thisdict = {
        "all" : a,
        "both" : b,
        "disjoint" : c,
        "only_a" : d,
        "only_b" : e
        }
    return thisdict

#course_math = { "Alice", "Bob", "Diana" }
#course_cs   = { "Charlie", "Eve", "Frank" }
#res         = analyze_courses( course_math, course_cs )
#print(res)
