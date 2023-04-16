from nebula3.Config import Config
from nebula3.gclient.net import ConnectionPool, Session

from config import GraphDB

class Client:
    def __init__(self) -> None:
        self.connection_pool = None

    def start(self) -> None:
        if self.running():
            return
        config = Config()
        config.max_connection_pool_size = 10
        self.connection_pool = ConnectionPool()
        ok = self.connection_pool.init([(GraphDB.ip, GraphDB.port)], config)
        if not ok:
            raise Exception('fail to connect to GraphDB')

    def get_session(self) -> Session:
        return self.connection_pool.get_session(GraphDB.username, GraphDB.password)

    def close(self) -> None:
        self.connection_pool.close()

    def running(self) -> bool:
        return self.connection_pool is not None

client = Client()
client.start()
ses