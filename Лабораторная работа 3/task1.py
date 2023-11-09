# TODO Напишите функцию для поиска индекса товара

def search(list_of_products, product):
    for  index_ , value_ in enumerate(list_of_products):
        if value_ == product:
            return index_
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

