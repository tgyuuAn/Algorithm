present_count, money, original_sale_count = map(int,input().split())
present_prices = sorted(list(map(int,input().split())))

window = []
total_price = 0
sale_count = original_sale_count

for price in present_prices:
    if original_sale_count > 0:
        if sale_count > 0 and money >= (total_price + price//2):
            window.append(price//2)
            total_price += price//2
            sale_count -= 1

        elif money >= (total_price + window[-original_sale_count] + price//2):
            window.append(price//2)
            total_price += price//2
            total_price += window[-original_sale_count-1]
            window[-original_sale_count-1] *= 2

        else: break

    else:
        if money >= total_price + price:
            window.append(price)
            total_price += price

        else: break

    print(window)

print(len(window))