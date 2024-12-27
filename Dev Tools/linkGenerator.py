link1 = "https://media.reaperscans.com/file/4SRBHm/comics/9ab10139-d95c-4d3c-8b6d-fb1cc396990d/chapters/a6b2f1c2-f22f-4b8e-b392-e11fa16e0aaf/"
link2 = ".jpg"
num = int(input("Enter the number of chapters: "))

for i in range(1, num+1):
    if i < 10:
        print(f"\"{link1}0{i}{link2}\",")
    elif i > 9:
        print(f"\"{link1}{i}{link2}\",")
     