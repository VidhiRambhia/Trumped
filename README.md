CONTENTS OF THIS FILE 
---------------------

 * Introduction
 * Techstack
 * Setup
 * Repository Structure
 * Extension
 * Maintainers

INTRODUCTION
------------

***Trumped**: News served by ML, verified by Blockchain* <br> 
<img src="https://github.com/VidhiRambhia/Trumped/blob/master/project/static/overview.png" width=1000> <hr>
<br>
*Trumped* has three parts of the working project:<br>
  * **Machine Learning model:**<br> For classfying a given article as fake or real and blacklisting the publishers accordingly <br><br>
  * **Smart Contracts:** Users pay ether to authentic news Publishers; each Publisher is asked for a security deposit before publishing their news article <br><br>
  * **Website:** Where the Publishers publish their news for the Users to see <br><br>

TECHSTACK
---------

`SQLAlchemy`, <br>
`Solidity (version 0.5.11)`, <br>
`Ganache (v2.1.1.) + Metamask (version 7.2.1.)`, <br>
`Python-Flask (version 1.1.1),` <br>
`Pandas (version 0.25.1),` <br>
`Numpy (version 1.17.2),` <br>
`Sklearn` <br>


SETUP
-----

### Prerequisites
**Modules:**<br>
Clone this repository.<br>
In `Trumped/`, do:
` pip install -r dependencies.txt` on terminal.

<br>

**Metamask:** <br>
To simulate the working of this *Trumped* on a local blockchain, we need at least 4 wallets. <br>
For the purpose of this repository, the accounts used are as follows:
* **trumped:** Platform (Website's wallet)
* **Spyder:** FakeNews Publisher
* **Harishchandra:** AuthenticNews Publisher
* **Mocha:** User (viewer)
<br>
The aforementioned users are stored locally in the Ropsten network connected the host browser. The payments made by *Mocha*, *Sypder*, and *Harichandra* are done using Metamask. Solidity files, stored in `contracts`, user the active wallet address in Metamask, and have the receiver address value hardcoded.

### Running *Trumped*
To set up user and/or publisher accounts on local Ethereum, Ganache transactions can be used to connect to Metamask wallets. Change to `Custom RPC` on Metamask to the RPC server on Ganache. Import account using Ganache account key.
<br><br>
In `Trumped/`, run:
`python run.py`.
<br>Select appropriate accounts for respective transactions.

REPOSITORY STRUCTURE
--------------------
* **project**
  * contracts (Solidity smart contracts)
    * SecurityDeposit.sol
    * Refund.sol
    * FeeForAuthentic.sol
  * data
  * static
  * templates
  * FakeNewsClassifier.py
  * NSV.db
  * NewsTypeClassifier.py
  * _init_.py
  * forms.py
  * models.py
  * news  (data set for training News Category Identifier)
  * routes.py
  * test_fake.csv (data set for testing Fakes News Classifier)
  * train_fake.csv (data set for testing Fakes News Classfier)
* **.gitignore**
* **createDb.py**
* **dependancies.txt**
* **run.py**
* **LICENSE**
* **README.md**


MAINTAINERS
-----------

This project has been developed in  *KJSCE Hack 2019*, at K.J. Somaiya College of Engineering, Vidyavihar, India in the time period of 24 hours.
The contributors to the project and this repository are :

Ms. Nidhee Kamble (nidheekamble)<br>
Mr. Shreyansh Chheda (shrey-c)<br>
Ms. Vidhi Rambhia (VidhiRambhia)<br>

