START_GREEN = "\033[32m"
START_RED = "\033[31m"
END_COLORS = "\033[0;0m"


def green(text):
    return START_GREEN + text + END_COLORS


def red(text):
    return START_RED + text + END_COLORS
