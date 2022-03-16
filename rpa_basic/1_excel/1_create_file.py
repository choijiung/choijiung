from openpyxl import Workbook
wb = Workbook() #새 워크북 생성
ws = wb.active # 현재 활성화된 sheet 가져옴
ws.title="auto_Sheet" # sheet 의 이름은 변경
wb.save("excel_files/sample.xlsx") # sample 이름으로 저장 (excel_projects은 경로)
wb.close()