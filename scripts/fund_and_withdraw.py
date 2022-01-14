from brownie import FundMe
from scripts.helpfull_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    balance = fund_me.balance()
    print("1 Balance: " + str(balance))
    price = fund_me.getPrice()
    entrance_fee = fund_me.getEntraceFee()
    print(entrance_fee)
    print(price)

    fund_me.fund({"from": account, "value": entrance_fee})
    balance = fund_me.balance()
    print("2 Balance: " + str(balance))


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    balance = fund_me.balance()
    print("3 Balance: " + str(balance))
    fund_me.withdraw({"from": account})
    balance = fund_me.balance()
    print("4 Balance: " + str(balance))


def main():
    fund()
    withdraw()
