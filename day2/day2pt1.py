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
    for x in range(loopNum-1):
        if "red" in splits[2*x +1]:
            red = int(splits[2*x])
        if "green" in splits[2*x +1]:
            green = int(splits[2*x])
        if "blue" in splits[2*x +1]:
            blue = int(splits[2*x])
        if red > 12 or green > 13 or blue > 14:
            sum+= int(gamenum)
            break
            

        # print("First = " +splits[2*x])
        # print("Second = " +splits[2*x +1])
    
    
    # if red < 13 or green < 14 or blue < 15:
    #     sum+= int(gamenum)
print(total-sum)