from blockchain import Blockchain

bc = Blockchain()
# bc.new_transaction('Dave', 'Sammy', 30)

last_proof = 72608
proof = last_proof + 1
while True:
    guess = bc.valid_proof(last_proof, proof)
    if guess[:4] == "0000":
        print(str(proof) + ": " + guess)
        break

    proof = proof + 1
