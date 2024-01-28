from web3 import Web3
from solcx import compile_standard
import json

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/20ce49a5087e442395df6bacbc7f0b6e'))

if w3.is_connected():
    
    file_path = "abi2.json"
    
    wallet = "0xF290F7F1Fbe8665dC2e3A478Ee797C7Fb691E21F"
    
    gas_price = w3.eth.gas_price
    with open(file_path, 'r') as file:
        abi_data = json.load(file)

    file_path2 = "bytecodes2.json"
    with open(file_path2, 'r') as file:
        bytecodes = json.load(file)

    with open('transaction_details2.json' ,'r') as file:
         data = json.load(file)

    # Interact with the deployed contract
    print(data['transaction_receipt']['contractAddress'])
    contract_instance = w3.eth.contract(address=data['transaction_receipt']['contractAddress'], abi=abi_data)

    wallet_address = "0xF290F7F1Fbe8665dC2e3A478Ee797C7Fb691E21F"
    area_sqft = 22
    ocationAddress = "surat"
    price= 100
    propertyId = 100
    surveyNumber = 100
    lat = 100
    long = 100
    
    new_nonce = w3.eth.get_transaction_count(wallet)
    
    transaction = contract_instance.functions.storeProperty(
        wallet_address, area_sqft,ocationAddress,price,propertyId,surveyNumber,lat,long
    ).build_transaction({
        'chainId': 11155111,
        'gasPrice': gas_price,
        'from': wallet,
        'nonce': new_nonce,
    })

    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=data['private_key'])
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print("Transaction Hash:", transaction_hash)

    # Wait for the transaction receipt
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("Transaction Receipt:", transaction_receipt)

    # func_call = contract_instance..call()
    # print("Nonce Value", func_call)

