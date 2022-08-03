import asyncio


async def do_some_work(work_id: int):
    print(f'Start working id: {work_id}')
    await asyncio.sleep(1)
    print(f'End working id: {work_id}')


async def run_many_tasks():
    tasks = {
        asyncio.create_task(
            do_some_work(work_id)
        )
        for work_id in range(1, 100)
    }
    coroutine = asyncio.wait(tasks)
    await coroutine


def main():
    asyncio.run(run_many_tasks())


if __name__ == '__main__':
    main()
