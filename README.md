AlpCoin
---
# Second Part of the Project

Nodes were created to keep a record of transactions and the node stores the transactions

We also implement a PoW(Proof-of-Work) algorithm to mine and controll coins.
PoW allows us to controll the amount of coins by being hard to generate the item but easy to verify that item.

Created a simple implementation of a PoW algorithm.

The Algorithm works like this, The miners computer will have to increment a number until its divisible by 7 and the proof number of the last block. a new alpCoin block will be mined and the miner will obtain it.

To make shure the network is descentralized each node broadcasts its version of the chain to others and allows them to recieve the other nodes chains. And they verify the other nodes chains, so that every node reaches a consensus, of what the resulting blockchain will look like, all this is achieved by implementing a Consensus Algorithm.

The consensus algorithm is a simple one if the node chain is diff, then the longest chain in the network stays and all other will be deleted. if no conflicts then we carry on.

---
Learning blockchains
Following tutorial by Gerald Nash
