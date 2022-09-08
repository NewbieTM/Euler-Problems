# one - 3       two - 3        three - 5    four - 4        five - 4    six - 3        seven - 5    eight - 5  nine - 4 ten - 3 eleven -6   twelve - 6

value = 0
lexicon = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10 : 3,
    11 : 6,
    12 : 6,
    13 : 8,
    15 : 7,
    18 : 8,
    20 : 6,
    30: 6,
    40 : 5,
    50 : 5,
    80 : 6,
    100: 10
}

for x in range(1,1001):
    line = list(str(x))
    if x <= 13:
        value += lexicon[x]
    elif x <= 100:
        if x in lexicon:
            value+= lexicon[x]
        elif x <= 20:
            value += lexicon[int(line[1])] + 4
        else:
            line2 = line[0] + '0'
            if int(line2) in lexicon:
                value += lexicon[int(line2)] + lexicon[int(line[1])]
            else:
                value += lexicon[int(line[0])] + 2
                if int(line[1]) != 0:
                    value += lexicon[int(line[1])]
    elif x < 1000:
        if int(line[2]) != 0 and int(line[1]) != 0:
            line2 = line[1] + line[2]
            if not int(line2) in lexicon and int(line2) > 20:
                line3 = line[1] + '0'
                if not int(line3) in lexicon:
                    value += lexicon[int(line[0])] + 10 + lexicon[int(line[1])] + 2 + lexicon[int(line[2])]
                else:
                    value += lexicon[int(line[0])] + 10 + lexicon[int(line3)]  + lexicon[int(line[2])]
            elif not int(line2) in lexicon and int(line2) < 20:
                value += lexicon[int(line[0])] + 10 + lexicon[int(line[2])] + 4
            else:
                value += lexicon[int(line[0])] + 10 + lexicon[int(line2)]
        elif int(line[2]) == 0:
            line2 = line[1] + '0'
            if int(line2) in lexicon:
                value += lexicon[int(line2)] + 10 + lexicon[int(line[0])]
            else:
                if int(line[1]) == 0:
                    value+= 7 + lexicon[int(line[0])]
                else:
                    value += lexicon[int(line[1])] + 12
                    value += lexicon[int(line[0])]
                    if int(line[2]) != 0:
                        value += lexicon[int(line[2])]
        else:
            value += lexicon[int(line[0])] + 10 + lexicon[int(line[2])]
    else:
        value+=11

print(value)