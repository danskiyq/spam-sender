from telethon import TelegramClient
from time import time, sleep
import telethon.sync
import asyncio


class TimedSpam:
    """ Class sends message with given frequency in seconds"""
    def __init__(self, msg: str, ch_list: list, fq, send_immediately=False):
        self.message = msg
        self.channels_list = ch_list
        self.frequency = fq
        self.send_immediately = send_immediately

    async def send_spam(self):
        if not self.send_immediately:  # check if message needs to be sent immediately
            await asyncio.sleep(self.frequency)

        while True:
            start_time = time()
            for name in self.channels_list:
                await client.send_message(name, self.message)
            await asyncio.sleep(self.frequency - (time() - start_time))


if __name__ == '__main__':
    api_id = 16734569
    api_hash = '8c137eecf2abd641f472740daf3ab0fa'

    message = input('Message text:')
    frequency = int(input('Set frequency in seconds (Leave blank for 1 hour): '))
    send_immediately = (True if input('Do you want to send messages immediately? (Y/N):') in ('y', 'Y', 'Yes', 'yes', 'YES') else False)
    if not frequency:
        frequency = 3600

    client = TelegramClient('@zlatachkka', api_id, api_hash).start()
    client.get_dialogs()
    channels_list = [name.strip() for name in open('venv/channels_list', 'r')]

    timed_spam = TimedSpam(message, channels_list, fq=frequency)

    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([timed_spam.send_spam()])
    loop.run_until_complete(tasks)
