users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
site_visitors = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}
total_visitors = len(users)
unique_visitors = len(set(users))
site_visitors["Общее количество"] = total_visitors
site_visitors["Уникальные посещения"] = unique_visitors

print(site_visitors)