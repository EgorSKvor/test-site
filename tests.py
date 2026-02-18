# with open('/Users/aaa/Desktop/sheet/StepanErshov.github.io/file.txt', 'a', encoding='utf-8') as f:
#     f.write('\nПривет Денис, как дела?')


# with open('/Users/aaa/Desktop/sheet/StepanErshov.github.io/file.txt', 'r', encoding='utf-8') as f:
    # cont = f.read().splitlines()
    # print(cont)


# film = input()
# income = int(input())
# loss = int(input())

# if loss - income  < 0:
#     print(False)
# else:
#     clear_income = loss - income
#     print(f'{film}, {clear_income}')

# flag = True
# counter = 0
# while flag:
#     string = input()
#     if string == 'СТОП':
#         break
#     parsed_str = string.split(',')
#     film = parsed_str[0]
#     inc_usa = int(parsed_str[1])
#     inc_world = int(parsed_str[2])
#     if inc_usa > 50 and inc_world > 200:
#         counter += 1
# print(counter)

# companies = input()
# companies_parsed = companies.split(',')
# share = input()
# share_parsed = share.split(',')
# amount = float(input())
# res_list = []

# for i in range(len(companies_parsed)):
#     if float(share_parsed[i]) > amount:
#         res_list.append(companies_parsed[i])

# res_list.sort()
# print(', '.join(res_list))

# films_kir = input()
# films_kir_parsed = films_kir.split(', ')

# films_kol = input()
# films_kol_parsed = films_kol.split(', ')

# film_longer_2 = input()
# film_longer_2_parsed = film_longer_2.split(', ')

# longest_str = films_kir_parsed
# not_longest_str = films_kol_parsed
# if len(films_kol_parsed) > longest_str:
#     longest_str = films_kol_parsed
#     not_longest_str = films_kir_parsed

# res_list = []
# for i in range(len(longest_str)):
#     if longest_str[i] in not_longest_str and longest_str[i] not in film_longer_2_parsed:
#         res_list.append(longest_str[i])

# res_list.sort()
# print(', '.join(res_list))


# films_kir = set(input().split(', '))
# films_kol = set(input().split(', '))
# films_long = set(input().split(', '))

# res_list = list((films_kir & films_kol) - films_long)

# res_list.sort()
# print(', '.join(res_list))

# films = {'Lionsgate': {'Рэмбо': [54, 72]}}

# amount = int(input())
# count = 0

# for studio in films:
#     for film in films[studio]:
#         usa = int(films[studio][film][0])
#         worldwide = int(films[studio][film][1])
#         worlwide_without_us = worldwide - usa
        
#         if worlwide_without_us >= amount:
#             count += 1

# print(count)


# data = input()
# channels = []

# for item in data.split(', '):
#     name, ratings = item.split(' - ')
#     rating_2020 = float(ratings.split('; ')[-1])
#     channels.append((name, rating_2020))


# channels.sort(key=lambda x: x[1], reverse=True)
# print(', '.join([f"{name} - {rating}" for name, rating in channels]))

# min_duration = int(input())

# with open('films.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         line = line.strip()
#         if not line:
#             continue
            
#         parts = line.split(';')
#         name = parts[0]
#         duration = int(parts[1])
#         genres = parts[3]
        
#         if duration > min_duration and 'Crime' in genres:
#             print(name)


# min_duration = int(input())
# films_list = []

# with open('films.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         line = line.strip()
#         if not line:
#             continue
            
#         parts = line.split(';')
#         name = parts[0]
#         duration = parts[1]
#         genres = parts[3]
#         views_str = parts[4]
#         duration = int(duration.split()[0])
        
#         if duration > min_duration and 'Crime' in genres:
#             views = int(views_str.replace(',', ''))
#             films_list.append((name, views))

# films_list.sort(key=lambda x: x[1], reverse=True)
# top_films = films_list[:3]

# for film in top_films:
#     print(film[0])



# n = int(input())
# ratings = {}

# for _ in range(n):
#     _, channels_str = input().split(': ')
#     channels = channels_str.split(', ')
    
#     for i, channel in enumerate(channels):
#         ratings[channel] = ratings.get(channel, 0) + (3 - i)

# best_channel = max(ratings, key=ratings.get)
# print(best_channel)
