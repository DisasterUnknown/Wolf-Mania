numberOfChapters = int(input("Enter the number of chapters: "))

for i in range(1, numberOfChapters + 1):
    with open(f'Chapter {i}.json', 'w') as file:
        pass