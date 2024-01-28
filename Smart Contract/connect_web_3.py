from web3 import Web3
from solcx import compile_standard
import json

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/20ce49a5087e442395df6bacbc7f0b6e'))

if w3.is_connected():
    
    file_path = "abi.json"
    
    wallet = "0xF290F7F1Fbe8665dC2e3A478Ee797C7Fb691E21F"
    
    gas_price = w3.eth.gas_price
    with open(file_path, 'r') as file:
        abi_data = json.load(file)

      
    file_path2 = "bytecodes.json"
    with open(file_path2, 'r') as file:
        bytecodes = json.load(file)

    with open('transaction_details.json' ,'r') as file:
         data = json.load(file)

    # Interact with the deployed contract
    contract_instance = w3.eth.contract(address=data['transaction_receipt']['contractAddress'], abi=abi_data)

    name = "Vatsal Chauhan"
    wallet_address = "0xF290F7F1Fbe8665dC2e3A478Ee797C7Fb691E21F"
    email_id = "vlakhani1000@gmail.com"
    aadhar_number = "3434"
    pan_card_number = "34343"
    age = 33
    address = "hello"
    city = "surat"
    
    new_nonce = w3.eth.get_transaction_count(wallet) 
    
    transaction = contract_instance.functions.storeUserData(
        name, wallet_address, email_id, aadhar_number, pan_card_number, age, address, city
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

    nonce_stored = contract_instance.functions.getLatestNonce().call()
    print(nonce_stored)
    func_call = contract_instance.functions.getUserData(nonce_stored-1).call()
    print("User Data:", func_call)
    func_call = contract_instance.functions.getUserData(nonce_stored).call()
