import requests
import json

def get_current_balance(address):
    url = "http://localhost:8545/"
    payload = {
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()
    hex_result = response["result"][2:]
    wei_result = int(hex_result, 16)
    return wei_result

def eth_from_wei(wei):
    eth = wei / 1000000000000000000
    return eth

with open('genesis_block_etherscan.json', 'r') as genesis_file:
    genesis_data = json.load(genesis_file)

total_account_count = 0
total_ethereum = 0.0
total_match_account_count = 0
total_match_ethereum = 0.0

for result in genesis_data["result"]:
    total_account_count += 1
    gen_address = result["to"]
    gen_init_balance = int(result["value"])
    gen_cur_balance = get_current_balance(gen_address)
    cur_eth = eth_from_wei(gen_cur_balance)
    total_ethereum += cur_eth
    if gen_init_balance == gen_cur_balance:
        total_match_account_count += 1
        total_match_ethereum += cur_eth
        cur_eth_str = "{:.2f}".format(cur_eth)
        print (gen_address + " genesis account amount matches current amount (" + cur_eth_str + " eth)")

print ("Total genesis accounts: " + str(total_account_count))
total_ethereum_str = "{:.2f}".format(total_ethereum)
print ("Total genesis ethereum: " + total_ethereum_str)
print ("Total genesis accounts with amount matching current amount: " + str(total_match_account_count))
total_match_ethereum_str = "{:.2f}".format(total_match_ethereum)
print ("Total genesis ethereum from matching genesis accounts: " + total_match_ethereum_str)
