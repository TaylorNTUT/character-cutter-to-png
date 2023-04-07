from pdf2image import convert_from_path
from PIL import Image
import os
from tqdm import tqdm


def pdf_to_png(pdf_path, output_folder, start, end, dpi=600):
    # 使用 pdf2image 將 PDF 轉換為 PIL.Image.Image 對象列表
    print("讀取pdf檔案中，請稍候…")
    images = convert_from_path(pdf_path, dpi)
    start = int(start)
    end = int(start)

    # 確保輸出文件夾存在
    if not os.path.exists(output_folder):
        print(f"創立{output_folder}資料夾")
        os.makedirs(output_folder)

    # 遍歷圖像並將它們保存為 PNG
    for i, image in tqdm(enumerate(images), total=len(images), desc="Converting PDF to PNG"):
        output_path = os.path.join(output_folder, f'page_{start}.png')
        image.save(output_path, 'PNG')
        start += 1

# 使用範例
pdf_path = input('請輸入pdf的檔案名稱(放在同一個資料夾裡面/包含.pdf)：')  # 輸入 PDF 文件的路徑
page_start = input("請輸入要切割的pdf對應到的起始頁(在138頁中的第幾頁開始)：")
page_end = input("請輸入要切割的pdf對應到的結束頁(在138頁中的第幾頁結束)：")
output_folder = input('請輸入output的資料夾(Ex: page_png)：')  # 輸出 PNG 文件的文件夾
dpi = 600  # 設定輸出圖像的 DPI，增加 DPI 可提高圖像品質

pdf_to_png(pdf_path, output_folder, page_start, page_end, dpi)