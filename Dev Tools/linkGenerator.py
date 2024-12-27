link1 = "https://media.reaperscans.com/file/4SRBHm/comics/9ab10139-d95c-4d3c-8b6d-fb1cc396990d/chapters/c2734f50-31a1-4aaa-aa7d-206bff8c302e/"
link2 = ".jpg"
num = int(input("Enter the number of chapters: "))

for i in range(1, num+1):
    if i < 10:
        print(f"\"{link1}0{i}{link2}\",")
    elif i > 9:
        print(f"\"{link1}{i}{link2}\",")
     