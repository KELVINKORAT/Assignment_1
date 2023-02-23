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

# string_generator creates the random string
    async def __string_generator(self):
        k = random.randint(10, 20)
        rand_string = ''.join(random.choices(string.ascii_letters, k=k))
        mylist = [rand_string, self.string_to_count]
        return random.choice(mylist)

# writer writes the generated string in the file
    async def __writer(self, fname, mode, string):
        async with aiofiles.open(fname, mode) as f:
            await f.write(string + " ")

# string_counter counts the occurrences of string in the given file
    async def __string_counter(self, fname):
        async with aiofiles.open(fname, 'r') as f:
            # read content of file to string
            data = await f.read()
            # get number of occurrences of the substring in the string
            return data.count(self.string_to_count)

# write_to_file writes random strings to both the files and then creates the counts.log file
    async def write_to_file(self):
        while True:
            pseudo_string_1 = await self.__string_generator()
            pseudo_string_2 = await self.__string_generator()
            await self.__writer('File-1.txt', 'a', pseudo_string_1)
            await asyncio.sleep(1)
            await self.__writer('File-2.txt', 'a', pseudo_string_2)
            await self.__writer('counts.log', 'w',
                f'''The total number of occurrences for the “MARUTI” keyword by file-1 :{await self.__string_counter('File-1.txt')}
                \rThe total number of occurrences for the “MARUTI” keyword by file-2 :{await self.__string_counter('File-2.txt')}
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
