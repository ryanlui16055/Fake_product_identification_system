import hashlib
from time import time
import json

from numpy import block


class blockchain(object):
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.CreateBlock(
            previous_hash="First hash",
            proof=100,
        )

    def CreateBlock(self, proof, previous_hash=None):
        block = {
            # length of blockchain
            "index": len(self.chain) + 1,
            # timestamp when created a block
            "timestamp": time(),
            # pending list
            "trainsactions": self.pendingTransactions,
            # valid 'nonce'
            "proof": proof,
            # the most recent approved block
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.pendingTransactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {"sender": sender, "recipient": recipient, "amount": amount}
        self.pendingTransactions.append(transaction)
        return self.last_block["index"] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        # encode obj to binary form
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain_1 = blockchain()
t1 = blockchain_1.new_transaction("Satoshi", "Mike", "5 BTC")
t2 = blockchain_1.new_transaction("Mike", "Satoshi", "1 BTC")
t3 = blockchain_1.new_transaction("Satoshi", "Hal Finney", "5 BTC")
blockchain_1.CreateBlock(12345)

t4 = blockchain_1.new_transaction("Mike", "Alice", "1 BTC")
t5 = blockchain_1.new_transaction("Alice", "Bob", "0.5 BTC")
t6 = blockchain_1.new_transaction("Bob", "Mike", "0.5 BTC")
blockchain_1.CreateBlock(6789)

print("Genesis block: ", blockchain_1.chain)
