import pymongo
from Lesson09.Core.MongoInstance import MongoInstance


class SampleBlocks:
    def __init__(self):
        self.db_name = 'Lesson9'
        self.blocks_collection_name = 'SampleBlocks'
        self.samples_collection_name = 'Samples'

    def do_work(self):
        sensor_id = 7
        for i in range(10):
            data = [i * 10 + j for j in range(10)]
            block_record = {
                'sensor_id': sensor_id, 'block_index': i,
                'data': data}
            self.take_block(block_record)

    def take_block(self, block_record):
        MongoInstance.connect(self.db_name, self.blocks_collection_name)
        sensor_id = block_record['sensor_id']
        MongoInstance.insert(block_record)
        # get management record
        query = {'sensor_id': sensor_id, 'block_index': -1}
        records = MongoInstance.find(query)
        if len(records) == 0:
            # management record not yet exist. update will create it
            management_record = {'sensor_id': sensor_id, 'block_index': -1}
        else:
            management_record = records[0]
        # use field update atomic operation
        if 'counter' in management_record:
            del management_record['counter']
        update_cmd = {'$set': management_record, '$inc': {'counter': 1}}
        result_record = MongoInstance.find_and_update(query, update_cmd)
        counter = result_record['counter']
        if counter >= 10:
            # all blocks arrived. get them
            self.handle_completed(sensor_id)
        MongoInstance.disconnect()

    def handle_completed(self, sensor_id):
        query = {'sensor_id': sensor_id}
        print(f'completed for {query}')
        sort_cmd = [('block_index', pymongo.ASCENDING)]
        blocks = MongoInstance.find(query, sort_cmd)
        # delete the blocks
        MongoInstance.delete(query)
        MongoInstance.replace_collection(
            self.samples_collection_name)
        # concatenate blocks data
        real_blocks = [block for block in blocks
                       if block['block_index'] != -1]
        data = []
        for block in real_blocks:
            data += block['data']
        record = {'sensor_id': sensor_id, 'data': data}
        MongoInstance.insert(record)


if __name__ == '__main__':
    worker = SampleBlocks()
    worker.do_work()

