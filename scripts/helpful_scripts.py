from brownie import accounts, network, config


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["local-ganache", "development"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts.add(config["wallets"]["from_key"])
    
