"""Print out all the melons in our inventory.
Edit both files to track flesh color, rind color, and average weight of melons. 
lOutput should look something like:

"""


from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    # print(f"{name}s {have_or_have_not} seeds and are ${price:.2f}")

    print(f"""
        {name.upper()}
          seedless: {seedless}
          price: {price}
          flesh_color: None
          weight: None
          rind_color: None
          """)



for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
