import requests
import base64
from pdn.download_data.download_calls_data import post_requests_config as config
import datetime
import pandas as pd
import os
import re

def download(start_date: datetime.datetime = datetime.datetime.now().date(), 
            end_date: datetime.datetime = datetime.datetime.now().date() + datetime.timedelta(days=1), 
            path: str ='', name: str = 'calls_data_' + datetime.datetime.now().strftime(r'%Y%m%d') + '.xlsx',
            drop_income: bool = True, drop_test_calls: bool = True, save_file: bool = True ):
    '''
    Скачивание calls_data с использованием post запросов.
    start_date - дата начала периода скачивания. Если не указана - Сегодня 00:00
    end_date - дата конца периода скачивание. Если не указана - Завтра 00:00
    path - путь для скачивания
    name - имя файла БЕЗ РАСШИРЕНИЯ
    drop_income - убрать входящие звонки
    drop_test_calls - убрать тестовые звонки
    save_file - сохранить файл. Если False - xlsx файл удалится. Но DataFrame всегда возвращается.
    '''
    # TEST_CALLS_EMIASID = pd.read_csv(r'\\t999\Сетевой диск\pdn_\pdn\download_data\download_calls_data\test_calls_emiasid.csv')

    # name_xlsx = name + '.xlsx'
    # name_csv = name + '.csv'

    start = start_date.strftime('%d.%m.%Y %H:%M')
    end = end_date.strftime('%d.%m.%Y %H:%M')

    print('------------------\n\tdates\n', start, '\n', end)
    
    session = requests.Session()
    
    auth = session.post(os.path.join(config.BASE_LINK, 'auth.php'),
                        data=config.AUTH_DATA,
                        headers=config.HEADERS
                    )
    try:
        print('------------------\n\tauth\n', auth.json()['alert'])
    except:
        print('------------------\n\tauth\ndone!\ntoken: ', auth.json()['token'])
    
    access = session.post(os.path.join(config.BASE_LINK, 'access.php'),
                data=config.ACCESS_DATA,
                headers=config.HEADERS
                )

    try:
        print('------------------\n\taccess\n', access.json()['alert'])
    except:
        print('------------------\n\taccess\ndone!')
    
    make_table_data = config.MAKE_TABLE_DATA
    make_table_data['token'] = auth.json()['token']
    make_table_data['data[variables][0][value]'] = start
    make_table_data['data[variables][1][value]'] = end

    make_table = session.post(os.path.join(config.BASE_LINK, 'handler.php'),
                            data = make_table_data,
                            headers=config.HEADERS
                            )
    try:
        print(f'------------------\n\tmake_table\n', make_table.json()['alert'])
    except:
        print(f'------------------\n\tmake_table\ndone!\nreportName: ', make_table.json()["reportFile"])
        try: 
            print(f'idReport: ', make_table.json()["idReport"])
        except:
            print('------------------\n\tEmpty!')
            return None
    

    download_table_data = config.DOWNLOAD_TABLE_DATA
    download_table_data['data[file]'] = make_table.json()['reportFile']
    download_table_data['data[idReport]'] = make_table.json()['idReport']
    download_table_data['token'] = auth.json()['token']

    download_table = session.post(os.path.join(config.BASE_LINK, 'handler.php'),
                                data=download_table_data, 
                                headers=config.HEADERS
                                )
    try:
        print(f'------------------\n\tdownload_table\n', download_table.json()['alert'])
    except:
        print(f'------------------\n\tdownload_table\ndone!')

    content = base64.b64decode(download_table.content)

    with open(os.path.join(path, name), 'wb') as f:
        f.write(content)
    
    # Закрытие сессии
    session.close()

    data = pd.read_excel(os.path.join(path, name))
    cols = data.columns
    data.columns = [col.replace('+', ' ').strip() for col in cols]
    # data['Emiasid'] = data['Emiasid'].astype(str) \
    #     .apply(lambda x: x.replace('.0', ''))
    # data['Контактный телефон'] = data['Контактный телефон'] \
    #     .astype(str).apply(lambda x: x.replace('.0', ''))
    # data['Дата и время звонка'] = data['Дата и время звонка'] \
    #     .apply(lambda x: pd.to_datetime(x, dayfirst=True))
    # data['Дата и время окончания звонка'] = data['Дата и время окончания звонка']\
    #     .apply(lambda x: pd.to_datetime(x, dayfirst=True))
    # data['Дата и время переноса'] = data['Дата и время переноса'] \
    #     .apply(lambda x: pd.to_datetime(
    #         str(x).replace('.', '').replace(':', '').replace(' ', '').replace('400', '40'), 
    #         format=r"%d%m%Y%H%M", 
    #         dayfirst=True))
    # data['Дата создания мероприятия (программы)'] = \
    #     data['Дата создания мероприятия (программы)'] \
    #     .apply(lambda x: pd.to_datetime(x, dayfirst=True))

    if drop_income:
        data = data[data['Группа пациента'] != 'Входящий звонок']
    
    if drop_test_calls:
        data = data[[re.search(r'\b11111', str(id)) == None for id in data['Emiasid']]]

    os.remove(os.path.join(path, name))

    data = data.drop_duplicates()

    if save_file:
        data.to_excel(os.path.join(path, name), index=False)
        print('------------------\n\tfile is ready\nfile_name: ', name)
    else:
        print('------------------\nno file! only return')

    return data



if __name__ == '__main__':
    download()