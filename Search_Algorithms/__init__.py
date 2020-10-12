# <<<<<<<<<<<<<<<<<< MODULES LIST >>>>>>>>>>>>>>>>>
# OS OPERATION MODULES TO BE IMPORTED
import os
# IMPORT SYS BASED MODULES
import sys
# IMPORT PKG Utilities
import pkgutil
# IMPORT LIB MODULE FOR DYNAMIC IMPORT
import importlib
# ADD THE KEYWORDS MAPPING
from GateWayKeywords import AbstractSearchingKeys


__functions_list__ = AbstractSearchingKeys.searching_keywords

# GET THE PACKAGE PATH
package_path = os.path.dirname(__file__)

# GET THE BASE PACKAGE NAME
package_name = os.path.basename(package_path)

__package_key_pairs__ = dict()

# GET THE LIST OF MODULES THAT ARE PRESENT IN THE DIRECTORY
for _, module_name, _ in pkgutil.iter_modules([package_path]):
    __package_key_pairs__[module_name] = importlib.import_module(
        package_name + "." + module_name
    )

