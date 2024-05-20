def calculate_prices(symbol_same_sorting, each_unit_from_pair, quoted_prices):
    calculated_pricing = []
    # Zip takes multiple iterable objects and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
    for each_unit_from_pair, quoted_prices in zip(each_unit_from_pair, quoted_prices):
        calculated_pricing.append(float(each_unit_from_pair) * quoted_prices)

    total_pricing = sum(calculated_pricing)
    for symbol_same_sorting, calculated_pricing in zip(
        symbol_same_sorting, calculated_pricing
    ):
        print(f"{symbol_same_sorting} {calculated_pricing}")
    print(total_pricing)
