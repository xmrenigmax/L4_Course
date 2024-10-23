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
    # Check if it's a restocking day (every 7 days)
    if not (current_day == 0 or (current_day - 6) % 7 == 0):
        restocked_items = 0
        sold_units = random.randint(0, 200)
        available_items -= sold_units
    
    return available_items