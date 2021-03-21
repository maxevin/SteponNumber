def createLadder(x, y):
    stair = {}
    loop = 0

    # take the highest stair loop
    if (x > y):
        loop = x
    else:
        loop = y

    for i in range(loop+1):
        if i == 0:
            # create upper stair
            stair[str(0),str(0)] = 0

            # create lower stair
            stair[str(2),str(0)] = 2
            continue
        
        if i % 2 == 1:
            # create upper stair
            stair[str(i),str(i)] = (i * 2) - 1

            # create lower stair
            stair[str(i+2),str(i)] = (i*2) + 1
        else:
            # create upper stair
            stair[str(i),str(i)] = i * 2

            # create lower stair
            stair[str(i+2),str(i)] = i + (i+2)

    return stair


def steponNumber(steps):
    # initial empty result
    result = []

    for i in range(len(steps)):
        # create ladder from steps param
        ladder = createLadder(steps[i][0], steps[i][1])

        # convert steps into index
        index = str(steps[i][0]), str(steps[i][1])

        # find index in ladder
        if index in ladder:
            result.append(ladder[index])
        else:
            result.append('No Number')
    
    return result

List_awal = [
    [4,2],
    [6,6],
    [3,4]
]

print(steponNumber(List_awal))