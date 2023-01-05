from brownie import FundMe, config,network, MockV3Aggregator
from scripts.helpful_script import (get_account , deploy_mock,local_blockchain_environment,LOCAL_MAINNET_FORK_ENVIRONMENT)


# ifI add account through terminal then it is added in brownie not acces through accouts[0], 
# account = account.load()

def fund_me():
    account = get_account()
    # if network.show_active()!="development":
    # since ganache is not a development network but its a local network
    
    if network.show_active() not in local_blockchain_environment:
        price_feed = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed = MockV3Aggregator[-1].address

    #price feed as a argument is needed to pass becuase every testnet has different rpicefeed address
    # this price feed aggregator contain all the information about the rate of eth vs dollar
    #interfaces allow us to itnereact eith external real time event
    fund_me = FundMe.deploy(price_feed , {"from": account} , publish_source = config["networks"][network.show_active()].get("verify"))
    return fund_me


'''API not set for this network when try to deploy on ganache because etherscan dont know about ganache'''
def main():
    fund_me()