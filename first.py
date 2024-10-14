import asyncio as asc


async def first() -> None:
    await asc.sleep(2)
    print("oczekiwanie zakonczone")


async def second() -> None:
    await asc.sleep(1)
    print("hello")
    await asc.sleep(1)
    print("world")


async def thirdf() -> None:
    await asc.sleep(3)
    print("pierwszy komunikat")


async def thirds() -> None:
    await asc.sleep(1)
    print("drugi komunikat")


async def third() -> None:
    await (thirdf())
    await (thirds())


async def fourth() -> None:
    for temp in range(1, 6):
        await asc.sleep(1)
        print(temp)


async def fib(n) -> None:
    n0 = 0
    n1 = 1
    temp = 0
    while temp < n:
        print(n1)
        nth = n1 + n0
        n0 = n1
        n1 = nth
        temp += 1
        await asc.sleep(1)


async def fetch(delay) -> str:
    await asc.sleep(delay)
    return "zwrocono"


async def fmain() -> None:
    await asc.gather(fetch(3), fetch(5), fetch(1))


async def krojenie() -> None:
    await asc.sleep(2)


async def gotowanie() -> None:
    await asc.sleep(5)


async def smazenie() -> None:
    await asc.sleep(3)


async def kucharz1() -> None:
    await gotowanie()
    await gotowanie()
    await smazenie()
    print("gotowe")


async def kucharz2() -> None:
    await smazenie()
    await gotowanie()
    await smazenie()
    print("gotowe")


async def kucharz3() -> None:
    await smazenie()
    await gotowanie()
    await gotowanie()
    print("gotowe")


async def kuchnia() -> None:
    await asc.gather(kucharz1(),kucharz2(),kucharz3())


async def wczytanie() -> None:
    await asc.sleep(2)
    print("wczytano")

async def analiza() -> None:
    await asc.sleep(4)
    print("Analiza zakonczona")

async def zapis() -> None:
    await asc.sleep(1)
    print("zapisano")

async def plik() -> None:
    await wczytanie()
    await analiza()
    await zapis()


async def przetwarzanie() -> None:
    for x in range(1,6):
        await plik()
        print("zakonczono przetwarzanie pliku nr",x)



async def maszynaA()->None:
    await asc.sleep(2)
    print("koniec A")

async def maszynaB()->None:
    await asc.sleep(3)
    print("koniec B")

async def maszynaC()->None:
    await asc.sleep(5)
    print("koniec C")

async def machnineloop()->None:
    time = asc.get_event_loop().time()
    while True:
        end_time = asc.get_event_loop().time() - time
        await asc.gather(maszynaA(),maszynaB(),maszynaC())
        if end_time > 15:
            break



if __name__ == "__main__":
     asc.run(first())
     asc.run(second())
     asc.run(third())
     asc.run(fourth())
     asc.run(fib(10))
     asc.run(fmain())
     asc.run(kuchnia())
     asc.run(przetwarzanie())
     asc.run(machnineloop())

