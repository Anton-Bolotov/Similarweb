from country import const_countries
import sys
import re
import time
import requests


def count_of_links(file_in):
    count_links = 0
    with open(file_in, 'r', encoding='utf-8') as file:
        for _ in file:
            count_links += 1
    return count_links


def list_domain(file_in):
    some_list = []
    with open(file_in, 'r', encoding='utf-8') as file:
        ff = [i.strip() for i in file]
        for urls in ff:
            if '//' in urls:
                a = urls.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
                some_list.append(a)
            else:
                b = urls.replace('www.', '')
                some_list.append(b)
    return some_list


def rounding(number_to_round):
    if len(str(number_to_round)) >= 7:
        h = str(number_to_round)[:3] + '.' + str(number_to_round)[3:]
        j = round(float(h))
        g = str(j) + '0' * (len(str(number_to_round)) - 3)
        return g
    elif 5 <= len(str(number_to_round)) <= 6:
        h = str(number_to_round)[:2] + '.' + str(number_to_round)[2:]
        j = round(float(h))
        g = str(j) + '0' * (len(str(number_to_round)) - 2)
        return g
    elif 1 <= len(str(number_to_round)) <= 4:
        h = str(number_to_round)[:1] + '.' + str(number_to_round)[1:]
        j = round(float(h))
        g = str(j) + '0' * (len(str(number_to_round)) - 1)
        return g


def all_month(lenght, domain, result_all_month):
    if lenght == 12:
        with open(file='all_month.txt', mode='a', encoding='utf-8') as all_data_file1:
            all_data_file1.write(str(domain) + '\t'
                                 + str(rounding(number_to_round=result_all_month[1])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[3])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[5])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[7])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[9])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[11])) + '\n')
    elif lenght == 10:
        with open(file='all_month.txt', mode='a', encoding='utf-8') as all_data_file1:
            all_data_file1.write(str(domain) + '\t'
                                 + '-' + '\t'
                                 + str(rounding(number_to_round=result_all_month[1])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[3])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[5])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[7])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[9])) + '\n')
    elif lenght == 8:
        with open(file='all_month.txt', mode='a', encoding='utf-8') as all_data_file1:
            all_data_file1.write(str(domain) + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + str(rounding(number_to_round=result_all_month[1])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[3])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[5])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[7])) + '\n')
    elif lenght == 6:
        with open(file='all_month.txt', mode='a', encoding='utf-8') as all_data_file1:
            all_data_file1.write(str(domain) + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + str(rounding(number_to_round=result_all_month[1])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[3])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[5])) + '\n')
    elif lenght == 4:
        with open(file='all_month.txt', mode='a', encoding='utf-8') as all_data_file1:
            all_data_file1.write(str(domain) + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + str(rounding(number_to_round=result_all_month[1])) + '\t'
                                 + str(rounding(number_to_round=result_all_month[3])) + '\n')
    elif lenght == 2:
        with open(file='all_month.txt', mode='a', encoding='utf-8') as all_data_file1:
            all_data_file1.write(str(domain) + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + '-' + '\t'
                                 + str(rounding(number_to_round=result_all_month[1])) + '\n')
    else:
        print('Печалька')


def taken(domain, text):
    regular = f'"EstimatedMonthlyVisits":(.+\W),"GlobalRank":'
    regular_top5 = r'"TopCountryShares":(.+\W)],'
    match = re.search(regular, text)
    match_top5 = re.search(regular_top5, text)
    if match:
        subtotal = match.group(1).replace("{", "").replace("}", "").replace('"', '').replace(',', ' ').replace(':', ' ')
        result = subtotal.split(' ')[-1]
        result_all_month = subtotal.split(' ')
        result_intermediate = match_top5.group(1).replace('{"Value":', '').replace('],', ' ').replace('},', ' ')
        result_top5 = result_intermediate.replace('[', '').replace('}', '').replace(',"Country":', ' ')

        country1 = result_top5.split(' ')[1]
        country2 = result_top5.split(' ')[3]
        country3 = result_top5.split(' ')[5]
        country4 = result_top5.split(' ')[7]
        country5 = result_top5.split(' ')[9]

        percent1 = float(result_top5.split(' ')[0])
        percent2 = float(result_top5.split(' ')[2])
        percent3 = float(result_top5.split(' ')[4])
        percent4 = float(result_top5.split(' ')[6])
        percent5 = float(result_top5.split(' ')[8])

        amount_of_interest1 = round(int(result) * percent1)
        amount_of_interest2 = round(int(result) * percent2)
        amount_of_interest3 = round(int(result) * percent3)
        amount_of_interest4 = round(int(result) * percent4)
        amount_of_interest5 = round(int(result) * percent5)

        lenght_all = len(result_all_month)
        all_month(lenght=lenght_all, domain=domain, result_all_month=result_all_month)

        beautiful_number = rounding(result)
        with open('output.txt', 'a', encoding='utf-8') as file:
            file.write(
                str(domain) + '\t' + 'TotalTraffic' + '\t' + str(beautiful_number) + '\t' + 'FastFilter' + '\n' +
                str(domain) + '\t' + str(const_countries[country1]) + '\t' + str(
                    rounding(number_to_round=amount_of_interest1)) + '\n' +
                str(domain) + '\t' + str(const_countries[country2]) + '\t' + str(
                    rounding(number_to_round=amount_of_interest2)) + '\n' +
                str(domain) + '\t' + str(const_countries[country3]) + '\t' + str(
                    rounding(number_to_round=amount_of_interest3)) + '\n' +
                str(domain) + '\t' + str(const_countries[country4]) + '\t' + str(
                    rounding(number_to_round=amount_of_interest4)) + '\n' +
                str(domain) + '\t' + str(const_countries[country5]) + '\t' + str(
                    rounding(number_to_round=amount_of_interest5)) + '\n')


def filtration(file_in):
    start_time = time.time()
    print('*** После прохождения 20 ссылок необходимо выждать минуту, для обхода блокировки ***'
          '\n*** Процесс автоматический, ничего делать не нужно! ***\n')
    print('Начинаем парсинг данных...')
    with open(file='all_month.txt', mode='w', encoding='utf-8') as all_data_file:
        all_data_file.write('* Название месяца уточняйте на www.similarweb.com'
                            + '\n' + 'Домен' + '\t' + 'Месяц *' + '\t' +
                            'Месяц *' + '\t' + 'Месяц *' + '\t' +
                            'Месяц *' + '\t' + 'Месяц *' + '\t' + 'Месяц *' + '\n')
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write('Домен' + '\t' + 'Разбивка по странам' + '\t' + 'Посещаемость' + '\t' + 'FastFilter' + '\n')
    reg = r'"SiteName":(.+\W)'
    domain = list_domain(file_in)
    len_of_domain = int(len(domain))
    count = 0
    count_links = count_of_links(file_in)
    with open('bad_links.txt', 'w', encoding='utf-8') as ff:
        ff.write('Эти ссылки нужно проверить вручную:' + '\n')
    while True:
        count += 1
        r = requests.get(f'https://data.similarweb.com/api/v1/data?domain={domain[count - 1]}')
        if r.status_code != 429:
            sys.stdout.write('\r' + 'Пройдено ссылок: ' + str(count) + ' из ' + str(count_links) +
                             ' домен - ' + str(domain[count - 1]))
            sys.stdout.flush()
        if r.status_code == 429:
            time.sleep(61)
            count -= 1
        elif r.status_code == 404:
            with open('bad_links.txt', 'a', encoding='utf-8') as file:
                file.write('https://www.similarweb.com/website/' + str(domain[count - 1]) + '\n')
        elif r.status_code == 400:
            print(f'                                      - Это не домен или ссылка! Проверь в файле, '
                  f'строка № {count}!')
        elif r.status_code == 200:
            search1 = re.search(reg, r.text)
            if search1:
                match = search1.group(1).replace('"', '').split(',')[0]
                if domain[count - 1] == match:
                    need_domain = domain[count - 1]
                    need_r_text = r.text
                    try:
                        taken(domain=need_domain, text=need_r_text)
                    except IndexError:
                        with open('bad_links.txt', 'a', encoding='utf-8') as file:
                            file.write('https://www.similarweb.com/website/' + str(domain[count - 1]) + '\n')
                else:
                    with open('bad_links.txt', 'a', encoding='utf-8') as file:
                        file.write('https://www.similarweb.com/website/' + str(domain[count - 1]) + '\n')
        if count == len_of_domain:
            finish_time = time.time()
            parse_time = round(finish_time - start_time)
            print(f'\n\n{"":-^65}\n'
                  f'{" Готово! ":-^65}\n'
                  f'{" Положительный результат смотри в файле - output.txt ":-^65}\n'
                  f'{" Необработанные ссылки смотри в файле - bad_links.txt ":-^65}\n'
                  f'{" Посещаемость за все месяца смотри в файле - all_month.txt ":-^65}\n'
                  f'{" Парсинг занял - " + str(parse_time) + " секунд ":-^65}\n'
                  f'{"":-^65}')
            # print(f'{" Для выхода из программы нажмите - Enter ":-^65}\n{"":-^65}\n')
            # input()
            break


filtration('input.txt')
