# class DatabaseManager(AbstractPlugin):
#     class Config:

#     @classmethod
#     async def start(
#         cls,
#         database: str,
#     ) -> None:
#         """
#             Firstly, try loads from envirement, then from function arguments,
#             then from plugun defaults.

#             see plugins.AbsctractPlugin.loads_secrets for more
#         """
#         cls.Config.ENGINE = await create_engine(
