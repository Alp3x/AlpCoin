import datetime as date 
import alpCoinBlock as createBlock 

def createGenesisBlock():
    #Initialize the first Block manually
    return createBlock.Block(0,date.datetime.now(),"Genesis Block", "0")

