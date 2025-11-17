import datetime as date
import alpCoinBlock as newBlock

def nextBlock(lastBlock):
    thisIndex = lastBlock.index + 1
    thisTimestamp = date.datetime.now()
    thisData = "Hi i am Block" + str(thisIndex)
    thisHash = lastBlock.hash
    return newBlock.Block(thisIndex, thisTimestamp, thisData, thisHash)
