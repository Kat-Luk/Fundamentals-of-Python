# Create a function called localize_date( timepoint, fmt ) that takes 2 parameters:
# The first one (timepoint) is a datetime object, and the second one (fmt) is string representing how the date should the formatted.
# The second parameter can take the following values: "DMY", "YMD", "MDY".

# For example, a date formatted as "DMY" should look as such: 27.11.2001
# The separator should be a dot.

# The function takes the two parameters mentioned above. Then, formats the timepoint according to the format provided in fmt. Finally, returns the formatted date as a string to the main program.

import datetime
def localize_date(timepoint, fmt):
    match fmt:
        case "DMY":
            format = "%d.%m.%Y"
        case "YMD":
            format = "%Y.%m.%d"
        case "MDY":
            format = "%m.%d.%Y"
    return timepoint.strftime(format)