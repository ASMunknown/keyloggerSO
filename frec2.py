usage = {}

def count(key,usage):

    try:
        usage[key] = usage[key] + 1

    except Exception as e:
        usage[key] = 1
        

    print(usage[key])

with open('report.txt') as f:
    text = f.read()

    specialKeyFound = False
    tempSpecialKey = ''
    for i in range (0,len(text)):
        # print(text[i])

        if text[i] == '[':
            print('corchete we')
            specialKeyFound = True
            tempSpecialKey = text[i]
        elif specialKeyFound:
            if text[i] == ']':
                tempSpecialKey = tempSpecialKey + ']'
                count(tempSpecialKey)
                specialKeyFound = False
                tempSpecialKey = ''
            else:
                tempSpecialKey = tempSpecialKey + text[i]
        else:
            count(text[i])

print(usage)