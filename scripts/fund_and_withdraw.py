from brownie import FundMe,MockV3Aggregator
from scripts.helpful_script import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print("Funding")
    fund_me.fund({"from":account,"value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})

def money():
    account = get_account()
    fund_me = FundMe[-1]
    value = fund_me.addressToAmountFunded(account.address)
    print(value)

def main():
    fund()
    # money()
    # withdraw()
