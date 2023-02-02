import asyncio
import random

async def random_writer(string):
    global count_1
    count_1 = 0
    global count_2
    count_2 = 0
    for i in range(10):
        pseudo_string_1=random.choice([string,'other'])
        pseudo_string_2 = random.choice([string, 'other'])
        if pseudo_string_1 == 'MARUTI':
            count_1=count_1+1
        with open('File-1.txt', 'a') as f1:
            f1.write(pseudo_string_1+" ")
        await asyncio.sleep(1)
        if pseudo_string_2 == 'MARUTI':
            count_2 = count_2 + 1
        with open('File-2.txt', 'a') as f2:
            f2.write(pseudo_string_2+" ")

asyncio.run(random_writer('MARUTI'))

with open('counts.log', 'w') as file:
    file.write(f'''The total number of occurrences for the “MARUTI” keyword by file-1 :{count_1}
The total number of occurrences for the “MARUTI” keyword by file-2 :{count_2}
                ''')
