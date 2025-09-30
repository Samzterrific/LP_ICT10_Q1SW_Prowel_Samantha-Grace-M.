from  pyscript import display
# Ordering System Using Python

# String Data Type
shop_name = "ATINY'S DESTINY"
owner_name = "Sam Prowel"

# Integer Data type
year_since = 2018

# Float data type
tax_rate = 0.08

# Boolean data type
has_delivery = True
buy_here = True

# List data type
product_names = ["THE WORLD EP.FIN", "GOLDEN HOUR: PART.3", "WORLD EP.2: OUTLAW", "SPIN OFF: FROM THE WITNESS", "TREASURE EPILOGUE: Action to Answer", "ANITEEZ SET", "MIGHTEEZ SET", "LIGHTINY"]

# Tuple data types
business_hours = ("11:00 AM", "8:00 PM")

# Dictionary data types
products = {
    "THE WORLD EP.FIN": 699,
    "GOLDEN HOUR: PART.3": 799,
    "WORLD EP.2: OUTLAW": 599,
    "SPIN OFF: FROM THE WITNESS": 699,
    "TREASURE EPILOGUE: Action to Answer": 599,
    "ANITEEZ SET": 899,
    "MIGHTEEZ SET": 899,
    "LIGHTINY": 2000
}

# Set Data Types
commonly_bought = {"THE WORLD EP.FIN", "LIGHTINY", "GOLDEN HOUR: PART.3"}

# Displaying shop info
display (shop_name, target="name1")
display (f"Owner: {owner_name}", target="owner")
display (f"Since {year_since}", target="since")
display (f"Product Pricelist", target="heading1",)

# Display product items
display (product_names[0], target="prod1")
display (f"₱{products['THE WORLD EP.FIN']:.2f}", target="price1")

display (product_names[1], target="prod2")
display (f"₱{products['GOLDEN HOUR: PART.3']:.2f}", target="price2")

display (product_names[2], target="prod3")
display (f"₱{products['WORLD EP.2: OUTLAW']:.2f}", target="price3")

display (product_names[3], target="prod4")
display (f"₱{products['SPIN OFF: FROM THE WITNESS']:.2f}", target="price4")

display (product_names[4], target="prod5")
display (f"₱{products['TREASURE EPILOGUE: Action to Answer']:.2f}", target="price5")

display (product_names[5], target="prod6")
display (f"₱{products['ANITEEZ SET']:.2f}", target="price6")

display (product_names[6], target="prod7")
display (f"₱{products['MIGHTEEZ SET']:.2f}", target="price7")

display (product_names[7], target="prod8")
display (f"₱{products['LIGHTINY']:.2f}", target="price8")

# Display additional info
display (f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

# Display order type
display(f"F2F Orders Available", target="orderType")