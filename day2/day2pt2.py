file = open("day2.txt")
sum = 0
total = 0
for line in file:
    game = line.split(':')
    gamenum =  game[0].split(' ')[1]
    total = total + int(gamenum)
    line =line.replace(';', ',')
    splits = line.split(' ')


    red = 0
    green =0
    blue =0

    
    loopNum = int(len(splits)/2)
    for x in range(loopNum):
        if "red" in splits[2*x +1] and red < int(splits[2*x]):
            red = int(splits[2*x])
        if "green" in splits[2*x +1] and green < int(splits[2*x]):
            green = int(splits[2*x])
        if "blue" in splits[2*x +1] and blue < int(splits[2*x]):
            blue = int(splits[2*x])
    
    print(str(red) +" " + str(green)+" " + str(blue))
    sum = sum + red*blue*green
print(sum)