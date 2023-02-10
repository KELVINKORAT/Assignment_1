import asyncio
import string
import random
import aiofiles
import sys
import signal


# RandomWriter class provides the functionality of Files monitoring
class RandomWriter:
    def __init__(self, string_to_count):
        self.string_to_count = string_to_count
        self.__count_in_file_1 = 0
        self.__count_in_file_2 = 0

# string_generator creates the random string
    async def __string_generator(self):
        k = random.randint(10, 20)
        rand_string = ''.join(random.choices(string.ascii_letters, k=k))
        mylist = [rand_string, self.string_to_count]
        return random.choice(mylist)

# write_to_file writes random strings to both the files and then creates the counts.log file
    async def write_to_file(self):
        while True:
            pseudo_string_1 = await self.__string_generator()
            pseudo_string_2 = await self.__string_generator()
            if pseudo_string_1 == self.string_to_count:
                self.__count_in_file_1 = self.__count_in_file_1 + 1
            async with aiofiles.open('File-1.txt', 'a') as f1:
                await f1.write(pseudo_string_1+" ")
            await asyncio.sleep(1)
            if pseudo_string_2 == self.string_to_count:
                self.__count_in_file_2 = self.__count_in_file_2 + 1
            async with aiofiles.open('File-2.txt', 'a') as f2:
                await f2.write(pseudo_string_2+" ")
            async with aiofiles.open('counts.log', 'w') as file:
                await file.write(
                    f'''The total number of occurrences for the “MARUTI” keyword by file-1 :{self.__count_in_file_1}
                    \rThe total number of occurrences for the “MARUTI” keyword by file-2 :{self.__count_in_file_2}
                ''')


# signal_handler catches the Interrupt signals and exit the program successfully without any trace
def signal_handler(signal, frame):
    sys.exit(0)


async def main():
    signal.signal(signal.SIGINT, signal_handler)
    writer = RandomWriter('MARUTI')
    await writer.write_to_file()

try:
    asyncio.run(main())
except Exception as e:
    print(f"Error in main function: {e}")
