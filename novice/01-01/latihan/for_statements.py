words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
users = ['active', 'inactive']
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(user, len(user))
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    