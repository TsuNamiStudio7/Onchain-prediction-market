from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
private_key = "0xYourPrivateKeyHere"
account = w3.eth.account.privateKeyToAccount(private_key)

with open('PredictionMarket_abi.json') as f:
    abi = json.load(f)

bytecode = "0xYourContractBytecodeHere"

PredictionMarket = w3.eth.contract(abi=abi, bytecode=bytecode)
tx = PredictionMarket.constructor().buildTransaction({
    "from": account.address,
    "gas": 3000000,
    "gasPrice": w3.toWei('20', 'gwei'),
    "nonce": w3.eth.getTransactionCount(account.address),
})

signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Contract deployed at: {w3.toHex(tx_hash)}")
