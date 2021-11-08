cash = int(input())
stock_hist = list(map(int, input().split()))

def bnp():
    money = cash
    stock = 0
    for price in stock_hist:
        stock += money // price
        money = money % price

    return money+stock_hist[-1]*stock

def timing():
    money = cash
    stock = 0
    p_check = 0
    m_check = 0
    for i in range(1,14):
        if stock_hist[i] > stock_hist[i-1]:
            p_check += 1
            m_check = 0
        elif stock_hist[i] < stock_hist[i-1]:
            m_check += 1
            p_check = 0
        if m_check == 3:
            stock += money // stock_hist[i]
            money = money % stock_hist[i]
        if p_check == 3:
            money += stock*stock_hist[i]
            stock = 0
    return money+stock_hist[-1]*stock
if bnp() > timing():
    print("BNP")
elif bnp() < timing():
    print("TIMING")
else:
    print("SAMESAME")


