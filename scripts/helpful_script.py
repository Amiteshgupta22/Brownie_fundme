from brownie import network,config,accounts , MockV3Aggregator
from web3 import Web3
decimal = 18
Starting_value = 200
LOCAL_MAINNET_FORK_ENVIRONMENT = ["mainnet-fork"]
local_blockchain_environment = ["development","ganache-local"]

def get_account():
    # every local blockhcian its own accoutns and accoutns give it 


    if network.show_active() in local_blockchain_environment or LOCAL_MAINNET_FORK_ENVIRONMENT:
        return accounts[0]

    account = accounts.add(config["wallets"]["from_key"])
    return account

def deploy_mock():
    account= get_account()
    print(f"Deploying to mock{network.show_active()}")
    MockV3Aggregator.deploy(decimal , Web3.toWei(Starting_value,"ether"),{"from":account})
    price_feed = MockV3Aggregator[-1].address
    
def main():
    print(get_account())