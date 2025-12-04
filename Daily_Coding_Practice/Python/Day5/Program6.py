# Write function to log errors into a file

def log_error(msg):
    with open("Daily_Coding_Practice\Day5\errors.log", "a") as f:
        f.write(msg + "\n")

try:
    n = int("abc")
    print(n)
except ValueError:
    log_error("ValueError occurred")

