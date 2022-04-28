import hashlib
from time import time
import json
from numpy import block, empty
import json


class blockchain(object):
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.CreateBlock(
            previous_hash="NAN",
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

        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


# ---------------------------------------------------------------------------------
blockchain_Apple = blockchain()
blockchain_Melon = blockchain()
blockchain_Stawberry = blockchain()


with open(
    r".\blockchain_project\blockchain_project\Chain_data\Apple.json", "r"
) as apple_chain:

    apple = json.loads(apple_chain.read())

    if apple != "":
        blockchain_Apple.chain = apple

    t1 = blockchain_Apple.new_transaction("Satoshi", "Mike", "Apple")
    blockchain_Apple.CreateBlock(12345)

    t2 = blockchain_Apple.new_transaction("Mike", "Satoshi", "Apple")
    blockchain_Apple.CreateBlock(56867)

    t3 = blockchain_Apple.new_transaction("Satoshi", "Hal Finney", "Apple")
    blockchain_Apple.CreateBlock(54245)

with open(
    r".\blockchain_project\blockchain_project\Chain_data\Apple.json", "w"
) as apple_chain:
    apple_chain.write(json.dumps(blockchain_Apple.chain))

# ---------------------------------------------------------------------------------

with open(
    r".\blockchain_project\blockchain_project\Chain_data\Melon.json", "r"
) as Melon_chain:

    Melon = json.loads(Melon_chain.read())

    if Melon != "":
        blockchain_Melon.chain = Melon

    t4 = blockchain_Melon.new_transaction("Mike", "Alice", "Melon")
    blockchain_Melon.CreateBlock(53463463)
    t5 = blockchain_Melon.new_transaction("Satoshi", "Mike", "Melon")
    blockchain_Melon.CreateBlock(6763463489)
    t6 = blockchain_Melon.new_transaction("Satoshi", "Alice", "Melon")
    blockchain_Melon.CreateBlock(6764363489)

with open(
    r".\blockchain_project\blockchain_project\Chain_data\Melon.json", "w"
) as Melon_chain:
    Melon_chain.write(json.dumps(blockchain_Melon.chain))

# ---------------------------------------------------------------------------------
with open(
    r".\blockchain_project\blockchain_project\Chain_data\Stawberry.json", "r"
) as Stawberry_chain:

    Stawberry = json.loads(Stawberry_chain.read())

    if Stawberry != "":
        blockchain_Stawberry.chain = Stawberry

    t7 = blockchain_Stawberry.new_transaction("Mike", "Bob", "Stawberry")
    blockchain_Stawberry.CreateBlock(6789)
    t8 = blockchain_Stawberry.new_transaction("Alice", "Bob", "Stawberry")
    blockchain_Stawberry.CreateBlock(6789)
    t9 = blockchain_Stawberry.new_transaction("Alice", "Mike", "Stawberry")
    blockchain_Stawberry.CreateBlock(6789)

with open(
    r".\blockchain_project\blockchain_project\Chain_data\Stawberry.json", "w"
) as Stawberry_chain:
    Stawberry_chain.write(json.dumps(blockchain_Stawberry.chain))
