from decimal import Decimal
from brownie import  FundMe, network,config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3
#if whatever network we are on, is not development or ganache-localm then go ahead and use config

from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()

# def deploy_fund_me():
    account = get_account()
    #pass price fee address to fund me address
    #if we are on persistent network such as rinkbet use tge associated address

    if network.show_active() != LOCAL_BLOCKCHAIN_ENVIRONMENTS: #if we are not on development section
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        #print(f"The active network is {network.show_active()}")
        #print("Deploying Mocks...")
        #if len(MockV3Aggregator) <=0:
    #     mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from":account}) #this to wei will add 18 decimal to 2000. converting the eth to wei for transaction
    #mock_aggregator.address is replaced. we sayong use most recently deployed
    #3 print("Mocks Deployed")

    #we imported the function from the helpful scripts instead of writing it here and making it lengthy


    fund_me = FundMe.deploy("0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
    {"from":account},
    publish_source = config["networks"][network.show_active()].get("verify")), #this will make things easier if we forget to verify

    print(f"Contract deployed to {fund_me.address}")

# def main():
    #deploy_fund_me()


