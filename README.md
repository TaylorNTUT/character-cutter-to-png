# character-cutter-to-png

## 0_pdf2png(如果已經有每一頁的.png檔案，這邊可以跳過)

放入想要切割的 pdf檔案 到 0_pdf2png 這個資料夾內


### 執行pdf2png.py：
a. 請輸入pdf的檔案名稱(放在同一個資料夾裡面/包含.pdf)：(測試的話可以用29_31.pdf來跑一次，之後改成自己的檔案)
b. 請輸入要切割的pdf對應到的起始頁(在138頁中的第幾頁開始)：(這邊改成138對應的頁數，如果切29到31，就寫29)
c. 請輸入要切割的pdf對應到的結束頁(在138頁中的第幾頁結束)：(如果切29到31，這邊寫31)
d. 請輸入output的資料夾(Ex: page_png)：page_png


注意：
如果是切29到31頁，資料夾裡面應該要有page_29.png, page_30.png, page_31.png這三個檔案，檔案的數字要對，因為會影響到下一個程式
如果是切1到138頁，資料夾裡面會有138個檔案(從page_1.png到page_138.png)


執行完後，page_png裡面會有每一頁的pdf檔案


## 1_cut2png

### 執行crop_img.py：
a. Please enter the number of pages you want to start processing(default:1): (輸入起始頁，如果是29到31，輸入29)
b. Please enter the number of pages you want to end processing(default:138): (輸入結束頁，如果是29到31，輸入31)
之後就會創一個29_31的資料夾，裡面會有300個png檔案


注意：w, X, Y的參數可能會依照png檔案的像素不同而需要修改，可以用test.png來抓對應的位置


註：
直接用Notability輸出PNG的話，這樣畫質不好

所以用Notability輸出：
1. 整個pdf檔案
2. 再把每一頁pdf檔案轉成PNG，並存成138個PNG檔案



