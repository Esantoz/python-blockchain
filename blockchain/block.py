import hashlib
from blockchain import proof

class Blockchain:
    blocks = []

    def __init__(self,block):
        self.blocks.append(block)

    def addBlock(self, data):
        prevBlock = self.blocks[len(self.blocks)-1]
        new = createBlock(data,prevBlock.hash)
        self.blocks.append(new)

class Block:
    hash = []
    data = []
    prevHash = []
    nonce = 0

    def __init__(self, data, prevHash,nonce):
        self.data = data
        self.prevHash = prevHash
        self.nonce = nonce

    def newProof(self):
        target = 1
        target = target << 256 - proof.DIFFICULTY
        pow = proof.ProofOfWork(self,target)
        return pow


def createBlock(data,prevHash):
    block = Block(data,prevHash,0)
    pow = Block.newProof(block)
    nonce, hash = pow.run()

    block.hash = hash[:]
    block.nonce = nonce

    return block 

def genesis():
    return createBlock("Genesis", " ")

def initBlockchain():
    return Blockchain(genesis())
