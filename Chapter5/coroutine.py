import asyncio
import time
from random import randint

async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)
    print('Resume of the Transition:\nStart State calling ' + result)

async def state1(transition_value):
    output_value = 'State 1 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)
    return output_value + 'State 1 calling ' + result

async def state2(transition_value):
    output_value = 'State 2 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)
    return output_value + 'State 2 calling ' + result

async def state3(transition_value):
    output_value = 'State 3 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)
    return output_value + 'State 3 calling ' + result

async def end_state(transition_value):
    output_value = 'End State with transition value = %s\n' % transition_value
    print('...stop computation...')
    return output_value

if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
    loop.close()