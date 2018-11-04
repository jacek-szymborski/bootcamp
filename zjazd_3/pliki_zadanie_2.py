user_last_login = {}
user_total_time = {}

with open("dane/logs.txt") as f:
    user_time = {}
    for line in f:
        stripped = line.rstrip()
        login, action, time = stripped.split(';')
        time = int(time)
        if action == "LOGIN":
            user_last_login[login] = time
        if action == "LOGOUT":
            user_total_time[login] = user_total_time.get(login, 0) + time-user_last_login[login]

print("Czas przebywania w systemie:")
for login in user_total_time:
    print(f" - {login}: {user_total_time[login]}")
