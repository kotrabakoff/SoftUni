page_cost = float(input())
cover_cost = float(input())
percentage_discount = int(input())
designer_cost = float(input())
percentage_paid_by_team = int(input())


price_per_book = (899 * page_cost + 2 * cover_cost) - ((899 * page_cost + 2 * cover_cost) * (percentage_discount / 100))

price_after_designer = price_per_book + designer_cost

money = price_after_designer - (price_after_designer * (percentage_paid_by_team / 100))

print(f"Avtonom should pay {money:.2f} BGN.")