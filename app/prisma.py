from prisma import Prisma
from functools import wraps


def with_prisma(func):
    @wraps(func)
    async def wrapper(*args,**kwargs):
        prisma=Prisma()
        try:
            await prisma.connect()
            return await func(*args,prisma=prisma,**kwargs)
        finally:
            await prisma.disconnect()
    return wrapper