import configparser

auth_config = configparser.ConfigParser()
auth_config.read(r"\\t999\Сетевой диск\pdn_\pdn\download_data\download_calls_data\auth.ini") 



user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
HEADERS = {'User-Agent': user_agent}

BASE_LINK = r'https://reports.vox-com.ru/rs/backend/'

AUTH_DATA = {"data[login]": auth_config['calls_reports']['login'], 
            "data[password]": auth_config['calls_reports']['password']}

ACCESS_DATA = {"to": "reports-show"}

MAKE_TABLE_DATA = {
	"data[id]": "769",
	"data[idReport]": "",
	"data[requestId]": "1659705677817",
	"data[variables][0][varName]": "begin",
	"data[variables][0][label]": "Начало+периода",
	"data[variables][0][id]": "9",
	"data[variables][0][value]": "",
	"data[variables][0][options]": "",
	"data[variables][0][required]": "1",
	"data[variables][0][conditions]": "",
	"data[variables][1][varName]": "end",
	"data[variables][1][label]": "Конец+периода",
	"data[variables][1][id]": "9",
	"data[variables][1][value]": "",
	"data[variables][1][options]": "",
	"data[variables][1][required]": "1",
	"data[variables][1][conditions]": "",
	"data[sortBy]": "",
	"data[projectId]": "corebo00000000000o0hv7qpcg8g8a7s",
	"data[columns][0][ID]": "31363",
	"data[columns][0][ENG_NAME]": "MO",
	"data[columns][0][RUS_NAME]": "МО",
	"data[columns][0][SORT_ORDER]": "1",
	"data[columns][0][EXCEL_TYPE]": "string",
	"data[columns][0][BROWSER_WIDTH]": "",
	"data[columns][0][show]": "1",
	"data[columns][1][ID]": "31364",
	"data[columns][1][ENG_NAME]": "MU",
	"data[columns][1][RUS_NAME]": "МУ",
	"data[columns][1][SORT_ORDER]": "10",
	"data[columns][1][EXCEL_TYPE]": "string",
	"data[columns][1][BROWSER_WIDTH]": "",
	"data[columns][1][show]": "1",
	"data[columns][2][ID]": "31365",
	"data[columns][2][ENG_NAME]": "MO_SOZD_PROG",
	"data[columns][2][RUS_NAME]": "МО+где+создали+программу+",
	"data[columns][2][SORT_ORDER]": "20",
	"data[columns][2][EXCEL_TYPE]": "string",
	"data[columns][2][BROWSER_WIDTH]": "",
	"data[columns][2][show]": "1",
	"data[columns][3][ID]": "31366",
	"data[columns][3][ENG_NAME]": "EMIASID",
	"data[columns][3][RUS_NAME]": "Emiasid+",
	"data[columns][3][SORT_ORDER]": "30",
	"data[columns][3][EXCEL_TYPE]": "string",
	"data[columns][3][BROWSER_WIDTH]": "",
	"data[columns][3][show]": "1",
	"data[columns][4][ID]": "31367",
	"data[columns][4][ENG_NAME]": "NAME",
	"data[columns][4][RUS_NAME]": "Имя",
	"data[columns][4][SORT_ORDER]": "40",
	"data[columns][4][EXCEL_TYPE]": "string",
	"data[columns][4][BROWSER_WIDTH]": "",
	"data[columns][4][show]": "1",
	"data[columns][5][ID]": "31368",
	"data[columns][5][ENG_NAME]": "PATRONYMIC",
	"data[columns][5][RUS_NAME]": "Отчетство",
	"data[columns][5][SORT_ORDER]": "50",
	"data[columns][5][EXCEL_TYPE]": "string",
	"data[columns][5][BROWSER_WIDTH]": "",
	"data[columns][5][show]": "1",
	"data[columns][6][ID]": "31369",
	"data[columns][6][ENG_NAME]": "PHONE",
	"data[columns][6][RUS_NAME]": "Контактный+телефон",
	"data[columns][6][SORT_ORDER]": "60",
	"data[columns][6][EXCEL_TYPE]": "string",
	"data[columns][6][BROWSER_WIDTH]": "",
	"data[columns][6][show]": "1",
	"data[columns][7][ID]": "31370",
	"data[columns][7][ENG_NAME]": "DOCTOR_FIO",
	"data[columns][7][RUS_NAME]": "ФИО+врача+",
	"data[columns][7][SORT_ORDER]": "70",
	"data[columns][7][EXCEL_TYPE]": "string",
	"data[columns][7][BROWSER_WIDTH]": "",
	"data[columns][7][show]": "1",
	"data[columns][8][ID]": "31371",
	"data[columns][8][ENG_NAME]": "DOCTOR_SPEC",
	"data[columns][8][RUS_NAME]": "Специальность+врача+",
	"data[columns][8][SORT_ORDER]": "80",
	"data[columns][8][EXCEL_TYPE]": "string",
	"data[columns][8][BROWSER_WIDTH]": "",
	"data[columns][8][show]": "1",
	"data[columns][9][ID]": "31372",
	"data[columns][9][ENG_NAME]": "PROG_DN",
	"data[columns][9][RUS_NAME]": "Программа+ДН+",
	"data[columns][9][SORT_ORDER]": "90",
	"data[columns][9][EXCEL_TYPE]": "string",
	"data[columns][9][BROWSER_WIDTH]": "",
	"data[columns][9][show]": "1",
	"data[columns][10][ID]": "31373",
	"data[columns][10][ENG_NAME]": "PROG_DATE",
	"data[columns][10][RUS_NAME]": "Дата+создания+мероприятия+(программы)",
	"data[columns][10][SORT_ORDER]": "100",
	"data[columns][10][EXCEL_TYPE]": "string",
	"data[columns][10][BROWSER_WIDTH]": "",
	"data[columns][10][show]": "1",
	"data[columns][11][ID]": "31374",
	"data[columns][11][ENG_NAME]": "KOD_MKB_10",
	"data[columns][11][RUS_NAME]": "Код+МКБ-10+",
	"data[columns][11][SORT_ORDER]": "110",
	"data[columns][11][EXCEL_TYPE]": "string",
	"data[columns][11][BROWSER_WIDTH]": "",
	"data[columns][11][show]": "1",
	"data[columns][12][ID]": "31375",
	"data[columns][12][ENG_NAME]": "DIAGNOZ_NAME",
	"data[columns][12][RUS_NAME]": "Наименование+диагноза",
	"data[columns][12][SORT_ORDER]": "120",
	"data[columns][12][EXCEL_TYPE]": "string",
	"data[columns][12][BROWSER_WIDTH]": "",
	"data[columns][12][show]": "1",
	"data[columns][13][ID]": "31385",
	"data[columns][13][ENG_NAME]": "PATIENT_GROUP",
	"data[columns][13][RUS_NAME]": "Группа+пациента",
	"data[columns][13][SORT_ORDER]": "125",
	"data[columns][13][EXCEL_TYPE]": "string",
	"data[columns][13][BROWSER_WIDTH]": "",
	"data[columns][13][show]": "1",
	"data[columns][14][ID]": "31376",
	"data[columns][14][ENG_NAME]": "OPERATOR_LOGIN",
	"data[columns][14][RUS_NAME]": "Логин+оператора",
	"data[columns][14][SORT_ORDER]": "130",
	"data[columns][14][EXCEL_TYPE]": "string",
	"data[columns][14][BROWSER_WIDTH]": "",
	"data[columns][14][show]": "1",
	"data[columns][15][ID]": "31377",
	"data[columns][15][ENG_NAME]": "CALL_START",
	"data[columns][15][RUS_NAME]": "Дата+и+время+звонка",
	"data[columns][15][SORT_ORDER]": "140",
	"data[columns][15][EXCEL_TYPE]": "string",
	"data[columns][15][BROWSER_WIDTH]": "",
	"data[columns][15][show]": "1",
	"data[columns][16][ID]": "31378",
	"data[columns][16][ENG_NAME]": "CALL_END",
	"data[columns][16][RUS_NAME]": "Дата+и+время+окончания+звонка",
	"data[columns][16][SORT_ORDER]": "150",
	"data[columns][16][EXCEL_TYPE]": "string",
	"data[columns][16][BROWSER_WIDTH]": "",
	"data[columns][16][show]": "1",
	"data[columns][17][ID]": "31379",
	"data[columns][17][ENG_NAME]": "F_RESULT",
	"data[columns][17][RUS_NAME]": "Результат+звонка+",
	"data[columns][17][SORT_ORDER]": "160",
	"data[columns][17][EXCEL_TYPE]": "string",
	"data[columns][17][BROWSER_WIDTH]": "",
	"data[columns][17][show]": "1",
	"data[columns][18][ID]": "31380",
	"data[columns][18][ENG_NAME]": "EXIST_CALL_ADD",
	"data[columns][18][RUS_NAME]": "Разговор+состоялся",
	"data[columns][18][SORT_ORDER]": "165",
	"data[columns][18][EXCEL_TYPE]": "string",
	"data[columns][18][BROWSER_WIDTH]": "",
	"data[columns][18][show]": "1",
	"data[columns][19][ID]": "31381",
	"data[columns][19][ENG_NAME]": "RECALL",
	"data[columns][19][RUS_NAME]": "Дата+и+время+переноса",
	"data[columns][19][SORT_ORDER]": "170",
	"data[columns][19][EXCEL_TYPE]": "string",
	"data[columns][19][BROWSER_WIDTH]": "",
	"data[columns][19][show]": "1",
	"data[columns][20][ID]": "31382",
	"data[columns][20][ENG_NAME]": "COMMS_INPUT",
	"data[columns][20][RUS_NAME]": "Комменатрий",
	"data[columns][20][SORT_ORDER]": "180",
	"data[columns][20][EXCEL_TYPE]": "string",
	"data[columns][20][BROWSER_WIDTH]": "",
	"data[columns][20][show]": "1",
	"data[columns][21][ID]": "31383",
	"data[columns][21][ENG_NAME]": "OLD_COMMENT",
	"data[columns][21][RUS_NAME]": "Предыдущий+комментарий",
	"data[columns][21][SORT_ORDER]": "190",
	"data[columns][21][EXCEL_TYPE]": "string",
	"data[columns][21][BROWSER_WIDTH]": "",
	"data[columns][21][show]": "1",
	"data[columns][22][ID]": "31384",
	"data[columns][22][ENG_NAME]": "CNT",
	"data[columns][22][RUS_NAME]": "Кол-во+попыток+дозвона",
	"data[columns][22][SORT_ORDER]": "200",
	"data[columns][22][EXCEL_TYPE]": "string",
	"data[columns][22][BROWSER_WIDTH]": "",
	"data[columns][22][show]": "1",
	"data[expiredDate]": "",
	"data[page]": "1",
	"data[perPage]": "100",
	"data[projectIds]": "",
	"data[showType]": "",
	"method": "show",
	"service": "reports/reports",
	"interface": "reports-show",
	"token": ""
}

# DOWNLOAD_TABLE_DATA = {"data[file]": "", 
#                        "data[idReport]": "",
#                        "method": "csv",
#                        "service": "files",
#                        "interface": "reports-show",
#                        "token": ""}

DOWNLOAD_TABLE_DATA = {"data[file]": "", 
                       "data[idReport]": "",
                       "method": "excel",
                       "service": "files",
                       "interface": "reports-show",
                       "token": ""}