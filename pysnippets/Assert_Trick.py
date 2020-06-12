#creative ways to use the assert method

def apply_discount(product, discount):
    price = int(product['price']*(1.0-discount))
    assert 0 <= price <= product['price'] # this statement ensures discount price is always less than product price and higher than 0
    return price

shoes = {'name': 'Fancy Shoes', 'price': 1000 }

#print(apply_discount(shoes,1.25)) #this should fail

print(apply_discount(shoes,0.16)) #this should fail
