
import openpyxl

wb=openpyxl.load_workbook("D:\\software testing class\\demo part\\Framework\\data\\login_data.xlsx")
sh1=wb['Sheet1']
row=sh1.min_row

print(row)
print(type(row))
