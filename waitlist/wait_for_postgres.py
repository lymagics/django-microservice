import time

import psycopg2
from environs import Env

env = Env()
env.read_env()


def wait_for_postgres_to_come_up():
    deadline = time.time() + 120
    while time.time() < deadline:
        try:
            return psycopg2.connect(env.str('DJANGO_DATABASE_URL'))
        except psycopg2.OperationalError:
            time.sleep(0.5)
    raise Exception('Postgres never came up')


if __name__ == '__main__':
    wait_for_postgres_to_come_up()
    