import hashlib
from time import time
import json
from numpy import block


class blockchain(object):
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.CreateBlock(
            previous_hash="",
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


blockchain_Apple = blockchain()
t1 = blockchain_Apple.new_transaction("Satoshi", "Mike", "Apple")
# blockchain_Apple.CreateBlock(12345)
t2 = blockchain_Apple.new_transaction("Mike", "Satoshi", "Apple")
# blockchain_Apple.CreateBlock(5,)
t3 = blockchain_Apple.new_transaction("Satoshi", "Hal Finney", "Apple")
blockchain_Apple.CreateBlock(6)
print(t1)

blockchain_Melon = blockchain()
t4 = blockchain_Melon.new_transaction("Mike", "Alice", "Melon")
t5 = blockchain_Melon.new_transaction("Alice", "Bob", "Melon")
t6 = blockchain_Melon.new_transaction("Bob", "Mike", "Melon")
blockchain_Melon.CreateBlock(6789)
print(t4)
blockchain_Stawberry = blockchain()
t7 = blockchain_Stawberry.new_transaction("Mike", "Alice", "Stawberry")
t8 = blockchain_Stawberry.new_transaction("Alice", "Bob", "Stawberry")
t9 = blockchain_Stawberry.new_transaction("Bob", "Mike", "Stawberry")
blockchain_Stawberry.CreateBlock(6789)

print("Genesis block: ", blockchain_Apple.chain)
