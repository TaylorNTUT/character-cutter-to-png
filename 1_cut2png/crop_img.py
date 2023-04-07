from PIL import Image
import numpy as np
import json
import os
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = None


PAGE_START = input("Please enter the number of pages you want to start processing(default:1): ")
if not PAGE_START.strip():
    PAGE_START = 1

PAGE_END = input("Please enter the number of pages you want to end processing(default:138): ")
if not PAGE_END.strip():
    PAGE_END = 138

PAGE_START = int(PAGE_START)
PAGE_END = int(PAGE_END)


im_dir = f'./{PAGE_START}_{PAGE_END}'

count = 0
count_123 = 0


def read_json(file):
    with open(file) as f:
        p = json.load(f)
        v = ['']*13759
        for i in range(13759):
            if (128 <= i & i < 256) or (0 <= i & i < 32): # 128 - 255: 'UNICODE' = '     '; 0 - 31: unable to print
                v[i] = '123'
            else:
                v[i] = 'U+' + p['CP950'][i]['UNICODE'][2:6] # ex: 0x1234 --> U+1234
        return v

v = read_json('./CP950.json')

print(len(v))


if not os.path.exists(im_dir): # 創png這個資料夾
    os.makedirs(im_dir)
    print(f"Created folders '{PAGE_START}_{PAGE_END}'. ")
else:
    print(f"Folders '{PAGE_START}_{PAGE_END}' have been created. ")

print(f"Processing page {PAGE_START}~{PAGE_END} files. ")

for i in tqdm(range(PAGE_START, PAGE_END + 1)): # 因為Python的range最後一個數字沒有包括，所以這邊需要 + 1
    im_input = f'../0_pdf2png/page_png/page_{i}.png'
    # 測試用：im_input = f'./pdf2png/test/page_{i}.png'

    im = Image.open(f'./{im_input}')
    img_size = im.size
    m = img_size[0]
    n = img_size[1]
    w = h = 14.75*m/210 # w = h = 14.75*m/210
    # print(m, n)


    if im_input == "new.png": # 原本的測試程式
        X = np.arange(10.5, 186.5, 19.54)
        Y = np.arange(24, 253, 25.43)
        print(X)
        print(Y)
    else:
        X = np.arange(7.61, 205, 20) # 7.61, 192.5, 20
        # print(X)
        Y = np.arange(21.36, 280, 25.993) # 21.36, 280, 25.993
        # print(Y)


    for j in range(10):
        for k in range(10):
            index = 100*(i-1) + k + 10*j + 1

            if index <= len(v):
                if v[index-1] == '123':
                    count_123 += 1
                    continue

                x = X[k]*m/210
                y = Y[j]*m/210
                re = im.crop((x, y, x+w, y+h))
                re = re.resize((300,300))
                re.save(f'./{PAGE_START}_{PAGE_END}/'+ v[index-1] + '.png') # 因為list是從0開始存，所以要減1
                # 測試用：re.save(f'./{PAGE_START}_{PAGE_END}/'+ str(j)+str(k) + '.png') # 因為list是從0開始存，所以要減1
                count += 1
            else:
                break

print(f"The crop of page {PAGE_START}~{PAGE_END} has been completed")
print(f"  A total of {count} png files were processed")
print(f"  A total of {count_123} png files were not processed")