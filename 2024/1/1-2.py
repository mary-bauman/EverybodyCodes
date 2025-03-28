with open("1-2-in.txt", "r") as f:
    s = f.readline()
    potions = 0
    for i in range(0,len(s),2):
        one = s[i]
        two = s[i+1]
        if one == "x":
            match two:
                case "B": potions += 1
                case "C": potions += 3
                case "D": potions += 5
        elif two == "x":
            match one:
                case "B": potions += 1
                case "C": potions += 3
                case "D": potions += 5
        elif one == "A":
            match two:
                case "A": potions += 1 + 1
                case "B": potions += 1 + 2
                case "C": potions += 1 + 4
                case "D": potions += 1 + 6
        elif one == "B":
            match two:
                case "A": potions += 2 + 1
                case "B": potions += 2 + 2 
                case "C": potions += 6
                case "D": potions += 2 + 6
        elif one == "C":
            match two:
                case "A": potions += 5
                case "B": potions += 4 + 2
                case "C": potions += 4 + 4
                case "D": potions += 4 + 6
        elif one == "D":
            match two:
                case "A": potions += 6 + 1
                case "B": potions += 6 + 2
                case "C": potions += 6 + 3
                case "D": potions += 6 + 6

        
    print(potions)     
