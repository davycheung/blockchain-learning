from blockchain import Blockchain

class BlockchainClient(object):

    def __init__(self):
        self.bc = Blockchain()

    def mine(self):
        last_proof = self.bc.last_block['proof']
        return self.bc.proof_of_work(last_proof)

client = BlockchainClient()
proof = client.mine()
print(proof)
