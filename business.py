weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_sales = weekly_sales.copy()  

try:
  copied_sales = (weekly_sales)  
except ImportError:
  print("Error: 'copy' module not found. Please install the 'copy' module.")
  exit()

copied_sales["Week 2"]["Electronics"] = 18000

print("Original Sales Data:")
print(weekly_sales)

print("\nCopied Sales Data (modified):")
print(copied_sales)