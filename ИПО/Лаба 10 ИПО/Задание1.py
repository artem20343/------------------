import os

folder_name = "Lab10_07"

# Проверяем, существует ли папка с таким именем
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Папка '{folder_name}' успешно создана в текущей директории.")
else:
    print(f"Папка '{folder_name}' уже существует в текущей директории.")
