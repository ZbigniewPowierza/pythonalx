statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(slownik, status):
    ile = 0
    for i in slownik:
        if slownik[i] == status:
            ile = ile + 1
    return ile
print(online_count(statuses, "online"))
print(online_count(statuses, "offline"))