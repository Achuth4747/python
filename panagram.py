def panagram(m):
    l="qwertyuiopasdfghjklzxcvbnm"
    m=m.lower()
    for i in l:
        if i not in m:
            return False
        else:
            return True






print(panagram("hai how are you"))