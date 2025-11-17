import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(self.previousHash).encode())
        return sha.hexdigest()
