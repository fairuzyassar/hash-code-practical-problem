def pizzaOrder(pizzatype, maxOrder):
    n = len(pizzatype)
    K = [[0 for i in range(maxOrder+1)] for j in range(n+1)]
    selectedIndex = []

    for x in range(n+1):
        for y in range(maxOrder+1):
            if x == 0 or y == 0:
                K[x][y] = 0
            elif y < pizzatype[x-1]:
                K[x][y] = K[x-1][y]
            elif y >= pizzatype[x-1]:
                K[x][y] = max(pizzatype[x-1]+K[x-1][y-pizzatype[x-1]], K[x-1][y])
        
    maxAvailable = K[x][maxOrder]
    print(maxAvailable)

    for i in range(n, 0, -1):
        if maxAvailable <= 0:
            break
        if maxAvailable == K[i-1][maxAvailable]:
            continue
        else:
            selectedIndex.insert(0, i-1)
            maxAvailable  -= pizzatype[i-1]

    print(*selectedIndex)

pizza = [2,5,6,8]
maxOrder = 17

pizzaOrder(pizza, maxOrder)