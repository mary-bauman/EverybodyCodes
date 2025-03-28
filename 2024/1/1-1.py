with open("1-1-in.txt", "r") as t:
    s = t.readline()
    potions = 0
    for c in s:
        match c:
            case "B": potions += 1
            case "C": potions += 3
    print(potions)     
