import os
from PyPDF2 import PdfReader, PdfWriter

def abc_operation(file_path, output_pdf_path, bool_value):

    try:
        pdf_reader = PdfReader(file_path)
        pdf_writer = PdfWriter()

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        with open(output_pdf_path, "wb") as f:
            pdf_writer.write(f)
    except Exception as e:
        bool_value = False
        print(f"Error Error Error ---- occurred while processing {file_path}: {e}")


bool_value = True

# 设置文件夹路径
folder_path = 'P:/Book/RAW'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 特定的文件扩展名进行过滤
        if file.endswith('.pdf'):
            file_path = os.path.join(root, file)

            # 设置输出文件路径
            output_pdf_path = os.path.join("P:/Book/CLN", file)
            print(f"start ---- {file_path}...")
            abc_operation(file_path, output_pdf_path, bool_value)

if bool_value:
    print("All done!")
else:
    print("Error occurred!")
