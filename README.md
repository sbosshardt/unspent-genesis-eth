# Unspent Genesis ETH

## Description
Connects to a locally running geth node via json-rpc and finds genesis addresses that have balances that match the balance that they originally had.

This is a way of identifying addresses that haven't had any transactions (although, the script does not attempt to exclude addresses that sent and received an equal amount of wei).

## Running the Program
`python genesis_addresses.py`

## Dependencies
Geth needs to be running and the JSON-RPC server available. i.e. `geth --http`

Python needs to be installed.

You might also need the following (TBD):
`pip install json-rpc`
