def add_item(cart, item, quantity):
  """Adds an item to the shopping cart."""
  found = False
  for i in range(len(cart)):
    if cart[i][0] == item:
      cart[i][1] += quantity
      found = True
      break
  if not found:
    cart.append([item, quantity])
  print("Item added:", item, "Quantity:", quantity)
  print("Cart:", cart)

def remove_item(cart, item):
  """Removes an item from the shopping cart."""
  for i in range(len(cart)):
    if cart[i][0] == item:
      del cart[i]
      print("Item removed:", item)
      print("Cart:", cart)
      return
  print("Item not found in cart:", item)
  print("Cart:", cart)

def update_quantity(cart, item, quantity):
  """Updates the quantity of an item in the shopping cart."""
  for i in range(len(cart)):
    if cart[i][0] == item:
      cart[i][1] = quantity
      print("Quantity updated:", item, "Quantity:", quantity)
      print("Cart:", cart)
      return
  print("Item not found in cart:", item)
  print("Cart:", cart)

# Initialize an empty shopping cart
cart = []

# Add items to the cart
add_item(cart, "Apple", 2)
add_item(cart, "Banana", 3)
add_item(cart, "Apple", 1)  # Add more of an existing item

# Remove an item from the cart
remove_item(cart, "Banana")

# Update the quantity of an item
update_quantity(cart, "Apple", 4)