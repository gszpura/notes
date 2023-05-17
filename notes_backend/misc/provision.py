import os
import asyncio
import itertools

import asyncpg
from notes_backend.core.config import settings

# from notes_backend.db.session import get_asyncpg_conn_string, async_session
# from notes_backend.modules.note.models import Note


async def create_pool():
    pool = await asyncpg.create_pool(
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
        database=settings.DATABASE_NAME,
        host=settings.DATABASE_HOST
    )
    async with pool.acquire() as conn:
        await conn.execute("SELECT 1")
    return pool


def get_sql_files():
    #cwd = pathlib.Path().resolve()
    files = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith(".sql"):
                files.append(os.path.join(dirpath, filename))
    return files


def get_queries(filename: str):
    # TOOD: extract queries
    queries: list[str] = ['lala']
    print(f"Checking {filename}")
    return queries


async def run_queries(queries: list[str]):
    pool = await create_pool()

    async with pool.acquire() as conn:
        resp = await conn.execute(queries[0])
        print(resp)
        await conn.commit()


async def main():
    files = get_sql_files()
    q = [get_queries(f) for f in files]
    qs = list(itertools.chain(*q))
    print(qs)
    await run_queries(["SELECT * FROM notes;"])


if __name__ == "__main__":
    asyncio.run(main())
