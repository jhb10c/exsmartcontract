#!/usr/bin/env python
# coding: utf-8

# ## What is Defi?
# 
# Decentralized finance is a finanical system that permits an exchange of funds defined through a set of rules implemented by a distributed (blockchain) state machine. The participants of decentralized finance agree on the state of the machine, hence the order of transactions, through a consensus system. This is a permissionless-type system. 
# 
# The first decentralized financial system appeared on Ethereum. Other blockchains, such as Solana, Avalanche, Fantom, have recently developed their own defi system. We will explore how transactions work, what are automated market makers and decentralized banks. In this blog, we will explore Defi as a participant in the Ethereum ecosystem.
# 
# This blog is a constant work in progress, running on the build fast and break things philosophy. Most of the sections will contain interactive code that can be accessed using the mybinder tab above. The code will be written to interact with the ethereum test net kovan. A guide on how to interact with kovan can be found in the next section.   
# 
# If you have questions or notice mistakes, please email me at jhb10c@protonmail.com. 

# ## What is Ethereum?
# 
# Ethereum is a distributed state machine where there exists one cannonical state. This state contains all accounts, balances, and transactional history. The state of ethereum can be altered according to specific machine code specified by the etheruem virtual machine. To understand how the state is organized, refer to Preethi Kasireddy's survey "How does Ethereum work, anyway?". Any participant can alter the state on ethereum. However only one specific account type can intiate a state change.  
# 
# 

# ## Accounts
# 
# There are two types of accounts on Ethereum: Externally Owned Accounts and Contracts. Both account types have an address and the following properties: a nonce which represents the number of transactions completed; a balance of ether; code (hash); and storage (hash). 
# 
# Externally Owned Accounts are controlled by users. They contain an empty code hash and an empty storage hash. They are allowed to generate transactions without receiving any data from other accounts. 
# 
# Contracts contain a nonempty code hash and may contain a nonempty storage hash. These types of accounts are controlled by their code hash. Contracts are only allowed to generate a transaction if it has received (call) data from another account.   

# ## Transactions 
# 
# We have been abusing the phrase transaction. Techinally there are two types of transactional calls: transactions and message calls. 
# 
# Transactions are only generated by an externally owned account. They are recorded in the state. While message calls are sent to contract accounts. These are function calls to a contract's code. A transaction may contain numerous message calls which in turn may call other contracts. Message calls are not stored in the state.  
# 
# 
# Ethereum executes transactions in sequential order. This is to prevent different transactions from modifiying the state of the same account. For example, if two users called a contract to mint an NFT that had a mint limit of one. The order in which transactions are executed is determined by Miner. As such frontrunning transactions are a reality on Ethereum. To read more about this, please see Dan Robinson's 'Ethereum is a Dark Forest'. 
