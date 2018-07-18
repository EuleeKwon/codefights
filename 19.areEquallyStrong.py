def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if max(yourLeft,yourRight) == max(friendsLeft,friendsRight):
        if yourLeft + yourRight == friendsLeft + friendsRight:
            return True
        else:
            return False
    else:
        return False
