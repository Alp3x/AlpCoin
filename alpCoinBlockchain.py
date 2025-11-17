import alpCoinGenesis as GenesisBlock  
import alpCoinNewBlock as newBlock

#Create a list with the GenesisBlock
#A blockchain is a merely an immutable list
blockchain = [GenesisBlock.createGenesisBlock()]
previousBlock = blockchain[0]

#How many blocks to add in the blockchain
blocksToAdd=35

#add Blocks to the chain 
for i in range(0,blocksToAdd):
    blockToAdd = newBlock.nextBlock(previousBlock)
    blockchain.append(blockToAdd)
    previousBlock = blockToAdd
    print("Block #{} has been added to the BlockChain".format(blockToAdd.index))
    print("Hash > {}".format(blockToAdd.hash))
    print("Timestamp > #{}\n".format(blockToAdd.timestamp))

