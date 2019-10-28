import os

core = os.cpu_count()
login = os.getlogin()
path = os.get_exec_path()
envkey = 'PYTHON_HOME'
env = os.getenv(envkey)

print("Your computer has", core, "cores")
print("You are logged in as", login)
print("You computer path is the following:", path)
print("env", env)
