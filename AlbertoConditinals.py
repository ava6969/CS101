
def main():
    print('Welcome to my store')

    money = 100
    cookies_quantity = 5
    cookies_price = 3
    ice_cream_quantity = 2
    ice_cream_price = 2
    juice_quantity = 3
    juice_price = 1

    # if cookies_quantity > 0 and money > cookies_price:
    #     print('cookies bought')
    # if ice_cream_quantity > 0 and money >= ice_cream_price:
    #     print('ice-cream bought')
    # if juice_quantity > 0 and money > juice_price:
    #     print('juice bought')
    # else:
    #     print('out of stock')

    # '0) cookies(' + str(cookies_price) + '$): ' + str(cookies_quantity) + ' left\n'
    # '1) ice_cream(' + str(ice_cream_price) + '$): ' + str(ice_cream_quantity) + ' left\n'
    # 'default) juice(' + str(juice_price) + '$): ' + str(juice_quantity) + ' left\n' + '>> ')

    # loop
    while money > 0 and (juice_quantity > 0 or ice_cream_quantity > 0 or cookies_quantity > 0):
        item = input('what do you want to buy?\n'
                     '0) cookies({}$): {} left\n'
                     '1) ice_cream({}$): {} left\n'
                     '(default) juice({}$): {} left\n'
                     '>> '.format(cookies_price, cookies_quantity,
                                  ice_cream_price, ice_cream_quantity,
                                  juice_price, juice_quantity))

        if int(item) == 0 and money >= cookies_price:
            quant = cookies_quantity - 1
            if quant >= 0:
                cookies_quantity -= 1  # min
                money -= cookies_price  # money = money - cookies_price
                print('cookies bought, amount left:', money)
        elif int(item) == 1 and money >= ice_cream_price:
            quant = ice_cream_quantity - 1
            if quant >= 0:
                money -= ice_cream_price  # money = money - juice_price
                ice_cream_quantity -= 1
                print('ice_cream bought, amount left:', money)
        else:
            if money >= juice_price:
                quant = juice_quantity - 1
                if quant >= 0:
                    money -= juice_price  # money = money - juice_price
                    juice_quantity -= 1
                    print('juice bought, amount left:', money)




main()