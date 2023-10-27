from borg_singleton import ChildBorg
from test_1 import from_main_import



def from_testdotpy():
    childBorg = ChildBorg()

    # print(childBorg is childBorg)  # Check if childBorg is an instance of ChildBorg
    # print(childBorg.shared_variable)  # Access the shared variable
    status1 = childBorg is childBorg
    status2 = childBorg.shared_variable

    result1,result2 = from_main_import()

    return status1,status2,result1,result2


