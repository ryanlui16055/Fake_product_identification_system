import hashlib
from time import time
import json
import rsa
import os.path


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

    def new_transaction(self, sender, recipient, Product):
        transaction = {"sender": sender, "recipient": recipient, "Product": Product}
        self.pendingTransactions.append(transaction)
        return self.last_block["index"] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)

        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


# add new transaction block to product blockchain
def addition_chain(sender, recevier, proof, product):
    name_list = []

    with open(
        r".\blockchain_project\blockchain_project\login\username.txt", "r"
    ) as usernames:
        for name in usernames.readlines():
            name = name.strip()
            name_list.append(name)

        if sender not in name_list:
            return "No such sender"
        if recevier not in name_list:
            return "No such receiver"

    if product == 1:
        New_t = blockchain_Apple.new_transaction(sender, recevier, "Apple")
        blockchain_Apple.CreateBlock(proof)
        with open(
            r".\blockchain_project\blockchain_project\Chain_data\Apple.json", "w"
        ) as f:
            f.write(json.dumps(blockchain_Apple.chain))
    elif product == 2:
        New_t = blockchain_Melon.new_transaction(sender, recevier, "Melon")
        blockchain_Melon.CreateBlock(proof)
        with open(
            r".\blockchain_project\blockchain_project\Chain_data\Melon.json", "w"
        ) as f:
            f.write(json.dumps(blockchain_Melon.chain))
    elif product == 3:
        New_t = blockchain_Stawberry.new_transaction(sender, recevier, "Stawberry")
        blockchain_Stawberry.CreateBlock(proof)
        with open(
            r".\blockchain_project\blockchain_project\Chain_data\Stawberry.json", "w"
        ) as f:
            f.write(json.dumps(blockchain_Stawberry.chain))

    return "Successfully added transaction in blockchain"


# decryption the content of QRcode and check whether is fake or not
def identify_product(product_chain_RSA):
    product_chain = RSA_decryption(product_chain_RSA)
    if product_chain == False:
        return "Incorrect Key"

    product = product_chain[1]["trainsactions"][0]["Product"]
    real_chain = []
    if product == "Apple":
        real_chain = blockchain_Apple.chain
    elif product == "Melon":
        real_chain = blockchain_Melon.chain
    elif product == "Stawberry":
        real_chain = blockchain_Stawberry.chain
    else:
        return "Cannot identify product"

    for i, t_chain, r_chain in zip(
        range(len(product_chain)), product_chain, real_chain
    ):
        if json.dumps(t_chain) != json.dumps(r_chain):
            return "Fake Product!"
    return "Genuine Prodcut!"


# -------------------------------------------------------------------

# generate RSA KEY
def Gen_key():
    (public_key, private_key) = rsa.newkeys(8000)
    with open(
        r".\blockchain_project\blockchain_project\key\publicKey.pem", "wb"
    ) as key:
        key.write(public_key.save_pkcs1("PEM"))
    with open(
        r".\blockchain_project\blockchain_project\key\privateKey.pem", "wb"
    ) as key:
        key.write(private_key.save_pkcs1("PEM"))


# RSA encryption
def RSA_encryption(txt):
    (public_key, private_key) = get_keys()
    txt = json.dumps(json.dumps(txt))
    result = rsa.encrypt(txt.encode("ascii"), public_key)
    return result


# RSA decryption
def RSA_decryption(RSA_content):

    (public_key, private_key) = get_keys()
    try:
        result = rsa.decrypt(RSA_content, private_key).decode("ascii")
        result = json.loads(json.loads(result))
        return result
    except:
        return False


# get key from folder
def get_keys():
    with open(
        r".\blockchain_project\blockchain_project\key\publicKey.pem", "rb"
    ) as key:
        publicKey = rsa.PublicKey.load_pkcs1(key.read())
    with open(
        r".\blockchain_project\blockchain_project\key\privateKey.pem", "rb"
    ) as key:
        privateKey = rsa.PrivateKey.load_pkcs1(key.read())
    return publicKey, privateKey


if (
    os.path.exists(r".\blockchain_project\blockchain_project\key\publicKey.pem")
    == False
):
    Gen_key()

# ---------------------------------------------------------------------------------

# create default block in the beginning
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
    blockchain_Stawberry.CreateBlock(13515515)

with open(
    r".\blockchain_project\blockchain_project\Chain_data\Stawberry.json", "w"
) as Stawberry_chain:
    Stawberry_chain.write(json.dumps(blockchain_Stawberry.chain))
