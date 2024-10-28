import random

def daily_sales(available_items, inventory_records, current_day):
    """
    Function Input:
    ---------------
    available_items: (integer) Available Tshirts from the previous day.
    inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
    current_day: (integer) Day number which you want to add as the current day. 

    Function Output:
    ----------------
    available_items: (integer) This function returns this integer which updates the available items at the current day.

    The function will also update the inventory_records (For restocking) for a given current day. It will also return "available_items".
    This function manages the daily sales of inventory. On non-restocking days, it generates a random number of sold units (up to 200) and updates inventory_records with the number of units sold and remaining inventory.
    """
    # manages the daily sales of inventory
    ##generates a random number of sold_unit to 200 and updates inventory records with the number of unit sold and remaining inventory
    if current_day == 0 or (current_day - 6) % 7 == 0:
        sold_units = 0
        restocked_items = 2000 - available_items
        available_items = 2000
    else:
        restocked_items = 0
        sold_units = random.randint(0, 200)
        available_items -= sold_units

    # updates inventory records with the details of daily sales
    inventory_records.append((current_day, sold_units, restocked_items, available_items))

    return available_items
