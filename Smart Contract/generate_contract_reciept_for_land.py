import json
from web3 import Web3
from solcx import compile_standard
import json

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/20ce49a5087e442395df6bacbc7f0b6e'))

if w3.is_connected():
   
    file_path = "abi2.json"
    
    with open(file_path, 'r') as file:
        abi_data = json.load(file)
        
    file_path2 = "bytecodes2.json"
    with open(file_path2, 'r') as file:
            bytecodes = json.load(file)
            bytecode = bytecodes['object']
            
    contract = w3.eth.contract(abi=abi_data, bytecode=bytecode)
    wallet = "0xF290F7F1Fbe8665dC2e3A478Ee797C7Fb691E21F"
    nonce = w3.eth.get_transaction_count(wallet)
    print("Nonce:", nonce)

    constructor = contract.constructor()
    gas_estimate = constructor.estimate_gas()
    gas_price = w3.eth.gas_price
    transaction = constructor.build_transaction({
            'chainId': 11155111,
            'gas': gas_estimate,
            'gasPrice': gas_price,
            'from': wallet,
            'nonce': nonce,
        })

    private_key = "0x608e40985f701303c54c219a009c269310256ba07cfe6b0e1be54f41fce58643"
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print("Transaction Hash:", transaction_hash)

        # Wait for the transaction receipt
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("Transaction Receipt:", transaction_receipt)


    transaction_details = {
        "private_key": private_key,
        "transaction_hash": transaction_hash.hex(),
        "transaction_receipt": {
            "transactionHash": transaction_receipt.transactionHash.hex(),
            "blockHash": transaction_receipt.blockHash.hex(),
            "blockNumber": transaction_receipt.blockNumber,
            "contractAddress":transaction_receipt.contractAddress
        }
    }

    # Save the transaction details to a JSON file
    with open('transaction_details2.json', 'w') as json_file:
        json.dump(transaction_details, json_file, indent=4)

    print("Transaction details saved to 'transaction_details2.json'")
