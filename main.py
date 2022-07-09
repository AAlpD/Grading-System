while True:
    try:
        not_ = int(input("Not: "))
    except:
        not_ = 101

    notlist = [[100, 90], [89, 85], [84, 80],
               [79, 75], [74, 70], [69, 65],
               [64, 60],  [59, 50], [49, 0]]
    harflist = ["AA", "BA", "BB",
                "CB", "CC", "DC",
                "DD", "FD", "FF"]
    for i in range(10):
        if i == 9:
            print("DZ")
            break
        if notlist[i][0] >= not_ >= notlist[i][1]:
            print(harflist[i])
            break
        
