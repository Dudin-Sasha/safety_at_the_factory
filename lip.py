import cv2
from numpy import mean as mn
from matplotlib import pyplot as plt

lf = (0, 0, 210)
hf = (100, 150, 255)

# -----------------------------------|---------------------------------------|-----------------------------------------#
# Сохраняем отфильтрованную фотографию
# for i in range(1, 6):
#     photo = cv2.imread("kas" + str(i) + ".jpg")  # фото
#
#     only_object = cv2.inRange(photo, lf, hf)  # Отфильтрованное фото
#
#     plt.imshow(cv2.cvtColor(only_object, cv2.COLOR_BGR2RGB))
#     plt.savefig('only kas ' + str(i) + ".jpg", facecolor='black')  # Сохраняем
    # plt.show()
# ---------------------------------------------------------------------------------------------------------------------#

# Функция вычисления хэша

def CalcImageHash(FileName):
    image = cv2.imread(FileName)# Прочитаем картинку
    image = cv2.resize(image, (8, 8), interpolation=cv2.INTER_NEAREST)
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_NEAREST)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count

def choose():
    filt = cv2.inRange(cv2.imread(input("напишите название файла с расширениeм: ")), lf, hf)
    plt.imshow(cv2.cvtColor(filt, cv2.COLOR_BGR2RGB))
    plt.savefig('nado.jpg', facecolor="black")  # Сохраняем
    hashing = CalcImageHash("nado.jpg")
    return hashing

hash1 = choose()
# hash2 = CalcImageHash("only kas 1.jpg")

list = []
for o in range(1,6):
    list.append(CalcImageHash("only kas " + str(o) +'.jpg'))


def dof(hash1,list):
    spisok = []
    for i in list:
        spisok.append(CompareHash(hash1, i))
    spisok = mn.mean(spisok)
    print(spisok)
    return spisok


if str(1) in hash1:
    if dof(hash1, list) <= 5.0:
        print("каска надета")
    else:
        print("каска не надета")
else:
    print("каска не надета")

