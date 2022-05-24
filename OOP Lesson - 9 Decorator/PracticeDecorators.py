import openpyxl

def decor_save_excel(funct):
    def wrapper(lst):
        wb = openpyxl.Workbook()
        sheet = wb.active

        data = (
            ('Количество элементов', 'Среднее значение', 'Сумма элементов'),
            (len(lst), sum(lst)/len(lst), sum(lst))
        )
        for row in data:
            sheet.append(row)

        wb.save('calcList.xlsx')
    return wrapper

@decor_save_excel
def my_list_fun(lst):
    return lst

def main():
    my_list_fun([34,54,3,54,65,7,11])

if __name__ == '__main__':
    main()