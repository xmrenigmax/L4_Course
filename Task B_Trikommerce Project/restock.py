import random

def restock_inventory(available_items, inventory_records, current_day):
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
    This function handles the restocking of inventory. On day 0 and every 6 days thereafter, it restocks the inventory to a maximum of 2000 units and updates inventory_records with the details.
    This function takes records of previous days -as list -and updates the stocking record for a current day following the requirements.
    """
    if current_day == 0 or (current_day - 6) % 7 == 0:
        restocked_items = 2000 - available_items
        available_items = 2000
        sold_units = 0

    # Ensure available items do not exceed 2000 units
    available_items = min(available_items, 2000)
    
    return available_items
    