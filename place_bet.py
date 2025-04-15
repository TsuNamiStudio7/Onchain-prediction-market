from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
account = w3.eth.accounts[0]

with open('PredictionMarket_abi.json') as f:
    abi = json.load(f)

contract_address = "0xYourContractAddressHere"
contract = w3.eth.contract(address=contract_address, abi=abi)

def place_bet(amount, predicted_outcome):
    tx = contract.functions.placeBet(predicted_outcome).buildTransaction({
        "from": account,
        "value": w3.toWei(amount, "ether"),
        "gas": 100000,
        "gasPrice": w3.toWei("20", "gwei"),
        "nonce": w3.eth.getTransactionCount(account),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key="0xYourPrivateKeyHere")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Bet placed with tx hash: {w3.toHex(tx_hash)}")

place_bet(1, True)  # Place a bet with 1 ETH on 'True' outcome
