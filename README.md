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

`Flask: Python 3.6`, <br>
`SQLAlchemy`, <br>
`Solidity (version 0.5.11)`, <br>
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

<br><br>

**Metamask:** <br>
For the working of this repository, we need at least 






REPOSITORY STRUCTURE
--------------------
* **project**
  * contracts
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


EXTENSION
---------

* **React**  <br><br>
* ** ** <br><br>
* **x4:** y4


 MAINTAINERS
 -----------

This project has been developed in  *KJSCE Hack 2019*, at K.J. Somaiya College of Engineering, Vidyavihar, India in the time period of 24 hours.
The contributors to the project and this repository are :

Ms. Nidhee Kamble (nidheekamble)<br>
Mr. Shreyansh Chheda (shrey-c)<br>
Ms. Vidhi Rambhia (VidhiRambhia)<br>

