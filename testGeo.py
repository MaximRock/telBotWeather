from geopy.geocoders import Nominatim


geolokator = Nominatim(user_agent="user")
location = geolokator.geocode("archipovka, Russia")

# str_address = location.address

lst = list(map(str, location.address.split()))

# s = list(filter(lambda x: 'область,' in x, lst))
s = lst.index('область,')
# print(lst[0][:-1])

# str_1 = (lst[2], lst[s-1], lst[s], lst[-1])
# str_2 = (lst[0], lst[s-1], lst[s], lst[-1])

# if lst[0] == 'городской':
#     print(*str_1)
# else:
#     print(*str_2)

msg = ((lst[2][:-1], lst[s-1], lst[s][:-1], lst[-1]) if lst[0] == 'городской' else (lst[0][:-1], lst[s-1], lst[s][:-1], lst[-1]))
print(msg)



# print(location.latitude, location.longitude)

# ['Архиповка,', 'Сметанинское', 'сельское', 'поселение,', 'Смоленский', 'район,', 'Смоленская', 'область,', 'Центральный', 'федеральный', 'округ,', '214523,', 'Россия']

# Donetsk  archipovka

# городской округ Донецк, Ростовская область, Южный федеральный округ, Россия

# Архиповка, Сметанинское сельское поселение, Смоленский район, Смоленская область, Центральный федеральный округ, 214523, Россия

# Архиповка, Смоленский район, Смоленская область, Россия