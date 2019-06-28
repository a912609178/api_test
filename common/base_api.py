import os,json
from xlrd import open_workbook
from common.file_path import DATA_PATH


def get_xls(xls_name,sheet_name):
    xls = []
    xlspath = os.path.join(DATA_PATH,'excel',xls_name)
    file = open_workbook(xlspath)
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_id':
            xls.append(sheet.row_values(i))
    return xls



if __name__ == '__main__':
    api_xls = get_xls('test.xlsx', 'api')
    print(str(api_xls[3][8]).split(','))





