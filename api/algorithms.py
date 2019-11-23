from api.utils import *

# Products extractor
def extract_receipt_product(filename):
    product_dict = {}
    for line in image_parser(filename).split("\n"):
        if any(c.isupper() for c in list(line)) and all([word.isupper() for word in list(filter(lambda x: not any(y.isdigit() for y in x), line.split()))]):
            product_name = []
            for (i, word) in enumerate(line.split()):
                if word.isupper(): product_name.append(word)
                elif i > 0: 
                    products_price = word
                    break
            product_name = " ".join(product_name)
            product_dict[product_name] = products_price
    return product_dict