from api.utils import *

# Products extractor
def extract_receipt_product(filename):
    products_dict = []
    for line in image_parser(filename).split("\n"):
        if any(c.isupper() for c in list(line)) and all([word.isupper() for word in list(filter(lambda x: not any(y.isdigit() for y in x), line.split()))]):
            product = {}
            product_name = []
            for (i, word) in enumerate(line.split()):
                if i == 0 and word.isdigit(): quantity = int(word)
                elif word.isupper(): product_name.append(word)
                else: 
                    product_price = float("".join(list(map(lambda x: x if x != ',' else '.', list(word)))))
                    break
            product_name = " ".join(product_name)
            product["quantity"] = quantity
            product["product_name"] = product_name
            product["price"] = product_price
            products_dict.append(product)
    return products_dict