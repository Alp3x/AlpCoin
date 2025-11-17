from flask import Flask
from flask import request
node = Flask(__name__)

#store the transaction that this node has in a list
thisNodesTransaction = []

@node.route('/txion',methods=['POST'])
def transaction():
  if request.method == 'POST':
    # On each new POST request,
    # extract the transaction data
    new_txion = request.get_json()
    # Then we add the transaction to our list
    this_nodes_transactions.append(new_txion)
    #Transaction was sucesseful there for we log it in the console
    print "FROM: {}".format(new_txion['from'])
    print "TO: {}".format(new_txion['to'])
    print "AMOUNT: {}\n".format(new_txion['amount'])
    # Then we let the client know it worked out
    return "Transaction submission successful\n"

node.run()
