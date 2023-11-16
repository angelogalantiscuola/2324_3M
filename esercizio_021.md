# Exercise 21

You have three lists: `products`, `prices`, and `quantities`. The `products` list contains the names of different products, the `prices` list contains the corresponding prices of each product, and the `quantities` list contains the quantities of each product.

```python
products = ["laptop", "mouse", "keyboard"]
prices = [1000, 50, 70]
quantities = [5, 10, 8]
```

Your task is to write a Python program that performs the following operations:

1. Display the current inventory of products with their prices and quantities.
2. Ask the user for a product, a price, and a quantity. Add the product, its price, and its quantity to the products, prices, and quantities lists respectively. If the product already exists in the products list, update its price and quantity in the prices and quantities lists respectively.
3. Ask the user for a product to remove from the inventory. Remove the product, its price, and its quantity from the products, prices, and quantities lists respectively.
4. Calculate the total inventory by summing up the quantities of all products.
5. Calculate the total value of the stocks by multiplying the price of each product by its quantity and summing up the results.

Note: Make sure to handle the case where the user tries to remove a product that doesn't exist in the inventory.

