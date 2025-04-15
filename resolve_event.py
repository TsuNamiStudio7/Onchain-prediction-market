from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
admin_account = w3.eth.accounts[0]

with open('PredictionMarket_abi.json') as f:
    abi = json.load(f)

contract_address = "0xYourContractAddressHere"
contract = w3.eth.contract(address=contract_address, abi=abi)

def resolve_event(winning_outcome):
    tx = contract.functions.resolveEvent(winning_outcome).buildTransaction({
        "from": admin_account,
        "gas": 100000,
        "gasPrice": w3.toWei("20", "gwei"),
        "nonce": w3.eth.getTransactionCount(admin_account),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key="0xYourPrivateKeyHere")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Event resolved with tx hash: {w3.toHex(tx_hash)}")

resolve_event(True)  # Resolving event with 'True' outcome
