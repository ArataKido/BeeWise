






# class DatabaseManager(AbstractPlugin):
#     class Config:
#         ENGINE: Pool = None
#         PSQL_DATABASE: str = None
#         PSQL_USER: str = 'postgres'
#         PSQL_PASSWORD: str = 'postgresPass'
#         PSQL_HOST: str = 'database'
#         CONNECTION: Connection = None

#     @classmethod
#     async def start(
#         cls,
#         database: str,
#         user: str = None,
#         password: str = None,
#         host: str = None,
#         url: str = None
#     ) -> None:
#         """
#             Firstly, try loads from envirement, then from function arguments,
#             then from plugun defaults.

#             see plugins.AbsctractPlugin.loads_secrets for more
#         """
#         database, user, password, host = cls.loads_secrets(
#             DATABASE_NAME=database,
#             DATABASE_USER=user,
#             DATABASE_PASSWORD=password,
#             DATABASE_HOST=host,
#             DATABASE_URL=url,
#         )
#         cls.Config.ENGINE = await create_engine(
#             url=url
#         )
#         logging.info(f'DatabaseManager create postgres pool on:{cls.Config.POOL}')
