from pymongo import MongoClient


class CopyMongoIndexes:
    def __init__(self):
        self.db_name = 'MyDB'
        self.connect_str_src = "mongodb://localhost:27017"
        self.connect_str_dst = "mongodb://localhost:27017"

        self.client_src:MongoClient = None
        self.client_dst:MongoClient = None
        self.db_src = None
        self.db_dst = None

    def do_work(self):
        print(f'Copy Indexes')
        print(f'-- Connect')
        self.connect(self.db_name)
        print(f'-- List collections - src')
        self.list_collections(self.db_src)
        print(f'-- Copy indexes')
        self.copy_indexes()
        # print(f'-- List collections - dst')
        # self.list_collections(self.db_dst)
        print(f'-- Disconnect')
        self.disconnect()
        print(f'Terminated ok')

    def connect(self, db_name: str):
        try:
            self.client_src = MongoClient(self.connect_str_src)
            self.db_src = self.client_src[db_name]
            self.client_dst = MongoClient(self.connect_str_dst)
            self.db_dst = self.client_dst[db_name]
        except Exception as ex:
            print(f'Connect exception {ex}')

    def disconnect(self):
        self.client_src.close()
        self.client_dst.close()

    def list_collections(self, db):
        collection_names = db.list_collection_names()
        for collection_name in collection_names:
            print(f'---- {collection_name}')
            collection_src = db[collection_name]
            indexes_dict = collection_src.index_information()
            for index_name, index_info in indexes_dict.items():
                keys = index_info['key']
                print(f'------ keys:{keys}, name:{index_name}, info:{index_info}')

    def copy_indexes(self):
        collections = self.db_src.list_collection_names()
        for collection_name in collections:
            print(f'---- {collection_name}')
            collection_src = self.db_src[collection_name]
            collection_dst = self.db_dst[collection_name]
            collection_dst.drop_indexes()
            indexes_dict = collection_src.index_information()
            for index_name, index_info in indexes_dict.items():
                if index_name == '_id_':
                    continue
                # collection_dst.drop_index(index_name)
                keys = index_info['key']
                del index_info['ns']
                del index_info['v']
                del index_info['key']
                unique = True if 'unique' in index_info else False
                # collection_dst.create_index(keys, name=index_name, unique=unique)
                collection_dst.create_index(keys, name=index_name, **index_info)


if __name__ == '__main__':
    worker = CopyMongoIndexes()
    worker.do_work()


