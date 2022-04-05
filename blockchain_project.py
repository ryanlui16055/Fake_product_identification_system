import hashlib
import json
from time import time

class Block:
    def __init__(self, index, data, timestamp, previous_hash, nonce=0):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def calculate_hash(self):
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_str.encode()).hexdigest()

    def __repr__(self):
        return 'Block: {}'.format(self.__dict__)

class Blockchain:
    def __init__(self):
        self.newdata = []
        self.chain = []
        self.difficulty = 1
        self.create_genesis()

    def create_genesis(self):
        genesis_block = Block(0, [], time.time(), 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_new_data(self, data):
        self.new_data.append(data)

    def mine(self):
        if not self.new_data:
            return False
        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
                          data=self.new_data,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.__proof_of_work(new_block)
        self.__add_block(new_block, proof)
        self.new_data = []
        return new_block.index

    @property
    def last_block(self):
        return self.chain[-1]