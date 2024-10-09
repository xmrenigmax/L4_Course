import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 
This function takes records of previous days -as list -and updates the sales for a current day following the requirements
This function manages the daily sales of inventory. On non-restocking days, it generates a random number of sold units (up to 200) and updates inventory_recordswith the number of units sold and remaining inventory.The final code output must be able to do the following:i.Generate report: This feature should automatically generate an Excel sheet with records of daily stock levels.As an example, a sample on a generated Excel sheet report for a couple of days is given in the example table below for your guidance. Please be aware that your code should be able to automatically generate a simulated sheet as required for the full required tracking period (i.e., from 0 to 49 days).ii.Check report: You do not need to write any code for this feature. You need to use this feature in section (d).iii.Exit:DaySold UnitsRestocked UnitsAvailable Units00200020001105018952144017513470170441660153854301495617501320706802000Table 2: Example copied from an excel sheet report generated showing 2 stocking periods. The 1ststocking period is at day 0 and the 2ndstocking period is at day 7.

    '''
    # Check if it's a restocking day (every 7 days)
    if current_day % 7 == 0:
        restocked_items = 200
        sold_units = 0
    else:
        restocked_items = 0
        sold_units = random.randint(0, 200)

    # Update available items
    available_items = available_items + restocked_items - sold_units

    # Append the current day's record to inventory_records
    inventory_records.append((current_day, sold_units, restocked_items, available_items))
    return available_items