from brownie import FundMe,network,accounts
from scripts.deploy import fund_me
from scripts.helpful_script import (get_account , local_blockchain_environment)
import pytest

def test():
    account = get_account()
    fund_me_ = fund_me()
    get = fund_me_.getEntranceFee()+100
    tx = fund_me_.fund({"from":account , "value":get})
    assert fund_me_.addressToAmountFunded(account.address)==get



def test_only_owner_cn_withdraw():
    if network.show_active() in local_blockchain_environment:
        pytest.skip("only for local testing")
        # pytest will skip this test 
    fund_me = fund_me()
    bad_actor = accounts.add()
    # randomly generate new account
    fund_me.withdraw({"from":bad_actor})
    
def main():
    test()
    test_only_owner_cn_withdraw()