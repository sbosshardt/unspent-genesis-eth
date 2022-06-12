# Unspent Genesis ETH

## Description
Connects to a locally running geth node via json-rpc and finds genesis addresses that have balances that match the balance that they originally had.

This is a way of identifying addresses that haven't had any transactions (although, the script does not attempt to exclude addresses that sent and received an equal amount of wei).

## Dependencies
You might, but probably don't need the following (TBD):
`pip install json-rpc`
