"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).
    """
    if len(all_phones) == 0:
        return []

    return all_phones.split(",")


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).
    """
    phones = list_of_phones(all_phones)
    brands = []
    
    if len(all_phones) == 0:
        return []
    
    for i in phones:
        i = i.split(" ")
        
        if i[0] in brands:
            continue
        
        brands.append(i[0])
    
    return brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).
    """
    phones = list_of_phones(all_phones)
    brands = phone_brands(all_phones)
    models = []
    
    if len(all_phones) == 0:
        return []
    
    for i in phones:
        i = i.split(" ")

        for e in brands:
            if i[0] == e:
                i.pop(0)
        
        i = " ".join(i)
        if i in models:
            continue
        
        models.append(i)

    return models


def search_by_brand(all_phones: str, brand: str) -> list:
    """
    Search for phones by brand.

    The search is case-insensitive.
    """
    phones = list_of_phones(all_phones)
    results = []
    
    for i in phones:
        i = i.split(" ")
        for x in i:
            
            if brand.lower().count(x.lower()) > 0:
                results.append(" ".join(i))
                break
            
    return results


def search_by_model(all_phones: str, model: str) -> list:
    """
    Search for phones by model.

    The search is case-insensitive.
    """
    phones = list_of_phones(all_phones)
    models = [x.lower() for x in phone_models(all_phones)]
    brands = [x.lower() for x in phone_brands(all_phones)]
    results = []
    
    if len(model.split(" ")) > 1:
        return []
    if model.lower() in brands:
        return []
    
    for i in phones:
        i = i.split(" ")
        for x in i:
            if model.lower().count(x.lower()) > 0:
                results.append(" ".join(i))
                break
            
    return results


if __name__ == '__main__':
    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  
    # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11")) 
    # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  
    # ['Google']
    print(phone_brands(""))  
    # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))  
    # ['14', 'Pixel', 'Magic5']
    print(phone_models("IPhone 14 A,Google Pixel B,Honor Magic5,IPhone 14"))  
    # ['14 A', 'Pixel B', 'Magic5', '14']
    print(phone_models("LG Optimus Black"))
    # ['Optimus Black']
    print(search_by_brand("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "iphone"))  
    # ['IPhone X', 'IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "pro"))  
    # ['IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "1"))  
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "IPhone"))  
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "12 Pro"))  
    # []
    print(search_by_model("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "pro"))
    # ['IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model(['Google Pixel 2021', 'Google Pixel 2022', 'Random a b c d e f g h i j k l m n o p q r s t u v w x y z'], ))