## general code remarks

* no conftest file -  all fixtures went to the python file
* pytest.ini file typo in addopts - try to run from command line
* usually we use thr root as the dir to run the tests
* try to use as less as possible paths in the code- for config
* git ignore- use it for your convenience 
* git commit messages- please write more explainable messages
* dont do import *


## general test remarks
* logic in the tests is no good
* xfail tests doesn't have a reason
* test admin tests are good but not necessary
* no custom markers
* no parametrization
* random creation is good but not for regression tests, we want the tests to be consistent and repeatable
* reading json objects from the test is not a good idea
* deleting the db after the test ran- maybe it would be better to delete the db in the beginning of a test
