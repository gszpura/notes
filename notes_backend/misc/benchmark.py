import random
import string
import asyncio
from typing import Callable
from time import perf_counter
import asyncpg

from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.sql import select, func

from notes_backend.db.session import get_asyncpg_conn_string, async_session
from notes_backend.modules.note.models import Note


async def measure(func: Callable):
    cnt = 10
    total = 0
    for i in range(cnt):
        t1 = perf_counter()
        res = await func()
        t2 = perf_counter()
        total += t2 - t1
    return total, total / cnt


notes_table = Table(
    'notes',
    MetaData(),
    Column('id', Integer, primary_key=True),
    Column('note', String),
    Column('created_at', DateTime, default=func.now()),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now()),
)


def build_notes(cnt: int) -> str:
    notes: list[str] = []
    for i in range(cnt):
        note_str = ''.join(random.choices(string.ascii_letters, k=10))
        notes.append(f"('{note_str}')")
    return ','.join(notes)


async def fill_db(cnt: int):
    conn = await asyncpg.connect(get_asyncpg_conn_string())
    notes = build_notes(cnt)
    insert_batch = f'INSERT INTO notes(note) VALUES {notes};'
    try:
        async with conn.transaction():
            await conn.execute(insert_batch)
            total = await conn.fetch("SELECT COUNT(*) FROM notes;")
            print(total)
    finally:
        await conn.close()


async def clean_db():
    conn = await asyncpg.connect(get_asyncpg_conn_string())
    delete = f'DELETE FROM notes;'
    try:
        async with conn.transaction():
            await conn.execute(delete)
            total = await conn.fetch("SELECT COUNT(*) FROM notes;")
            print(total)
    finally:
        await conn.close()


async def run_sqlalchemy_model_new_session():

    async def get_notes():
        notes: list[Note] = []
        async with async_session() as session:
            async with session.begin():
                stmt = select(notes_table)
                result = await session.execute(stmt)
                for row in result:
                    notes.append(row)
        return notes

    total, per_call = await measure(get_notes)
    print("SQLAlchemy per call (new session every time):", per_call)
    return per_call


async def run_sqlalchemy_model_reuse_session():
    session = async_session()

    async def get_notes():
        notes: list[Note] = []
        async with session.begin():
            stmt = select(notes_table)
            result = await session.execute(stmt)
            for row in result:
                notes.append(row)
        return notes

    try:
        total, per_call = await measure(get_notes)
        print("SQLAlchemy per call (reuse session):", per_call)
    finally:
        await session.close()
    return per_call


async def run_asyncpg():
    conn = await asyncpg.connect(get_asyncpg_conn_string())

    async def get_notes():
        notes: list[Note] = []
        async with conn.transaction():
            result = await conn.fetch('SELECT * FROM notes')
            for row in result:
                notes.append(row)
        return notes

    try:
        total, per_call = await measure(get_notes)
        print("Asyncpg per call:", per_call)
    finally:
        await conn.close()
    return per_call


async def benchmark():
    await clean_db()
    await fill_db(50)
    await run_sqlalchemy_model_new_session()
    await run_sqlalchemy_model_reuse_session()
    await run_asyncpg()

    await clean_db()
    await fill_db(1000)
    await run_sqlalchemy_model_new_session()
    await run_sqlalchemy_model_reuse_session()
    await run_asyncpg()

    await clean_db()
    await fill_db(10000)
    await run_sqlalchemy_model_new_session()
    await run_sqlalchemy_model_reuse_session()
    await run_asyncpg()


asyncio.run(benchmark())
