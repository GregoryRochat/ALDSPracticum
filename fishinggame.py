fishlist1 = [1, 3, 13, 2, 3, 2]
fishlist2 = [3, 5, 1, 2]
scorelist = []


def solvefishinggame_v2(fishlist, p1=0):
    print(fishlist, "!", p1)
    global scorelist
    if len(fishlist) <= 2:
        print("[", max(fishlist) + p1, "]")
        scorelist.append(max(fishlist) + p1)
    else:
        solvefishinggame_v2(fishlist[2:], fishlist[0] + p1)
        solvefishinggame_v2(fishlist[1:-1], fishlist[0] + p1)
        solvefishinggame_v2(fishlist[:-2], fishlist[-1] + p1)
        solvefishinggame_v2(fishlist[1:-1], fishlist[-1] +p1)

    if not p1:
        maxscore = max(scorelist)
        for n in scorelist:
            if (sum(fishlist) - n) < n and n < maxscore:
                maxscore = n
        return maxscore


def solvefishinggame_v3(fishlist, p1=0):
    print(fishlist, "wtf", p1)
    global scorelist
    if len(fishlist) <= 2:
        for n in fishlist:
            scorelist.append(p1 + n)
    else:
        solvefishinggame_v2(fishlist[2:], fishlist[0] + p1)
        solvefishinggame_v2(fishlist[1:-1], fishlist[0] + p1)
        solvefishinggame_v2(fishlist[:-2], fishlist[-1] + p1)
        solvefishinggame_v2(fishlist[1:-1], fishlist[-1] +p1)

    if not p1:
        maxscore = max(scorelist)
        for n in scorelist:
            if (sum(fishlist) - n) < n < maxscore:
                maxscore = n
        return maxscore


print(solvefishinggame_v3(fishlist1))
print(scorelist, "\n")
scorelist = []
print(solvefishinggame_v3(fishlist2))
print(scorelist, "\n")


