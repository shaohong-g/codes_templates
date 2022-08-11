############################################
# Test install_local_packages
############################################
from TestPackage.one import *
print(test_function()) # test_function
test_data_files() # display dataframe from test.csv

from TestPackage.two import *
two_instance = two_another_test()
print(two_instance.print()) # Printing attribute: two_attribute
print(two_instance.print_other()) # Printing attribute: attribute

