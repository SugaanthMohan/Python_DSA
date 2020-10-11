# <<<<<<<<<<<<<<<<<< MODULES LIST >>>>>>>>>>>>>>>>>
# USED FOR SHUFFLING AND BENCHMARKING MY CODE
from Utils import Shuffler
from Utils.BenchMarker import seconds_benchmark
# SORTING ALGORITHMS IMPORTS USED HERE
import Sorting_Algorithms
# USED FOR SYSTEM OPERATIONS
import sys


def set_modules(algorithm_names: list = None):
    """
    Used for Dynamic import of the modules.
    :param algorithm_names: Name list of algorithms
    :return: None
    """
    if algorithm_names is None:
        sys.modules.update(Sorting_Algorithms.__package_key_pairs__)
    else:
        for algorithm_name in algorithm_names:
            sys.modules[algorithm_name] = Sorting_Algorithms.__package_key_pairs__.get(algorithm_name)


def get_algorithm_pairs(package_, algorithm_names: list = None):
    """
    Get their corresponding functions and their runnable function names.
    :param package_ : The package module used for importing module necessities
    :param algorithm_names: Name list of algorithms
    :return:
    """

    # RUN ALL ALGORITHMS IF THE TEST SET IS EMPTY
    if algorithm_names is None:
        algorithm_names = package_.__package_key_pairs__.keys()
        modules = package_.__package_key_pairs__.values()
    else:
        modules = [
            package_.__package_key_pairs__.get(algorithm_name)
            for algorithm_name in algorithm_names
        ]

    function_mapping = [
        str("{" + algorithm_name + "}").format_map(package_.__functions_list__)
        for algorithm_name in algorithm_names
    ]

    return list(zip(algorithm_names, modules, function_mapping))


@seconds_benchmark
def execute_by_wrappers(exec_items, container_: any = None):
    """
    Used for execution functions by dynamic calling.
    :param exec_containers_: The list of base arguments for execution
    :param container_: the container containing the set of values
    :return:
    """

    name, module, function = exec_items

    func_obj = getattr(module, function)

    return {
            'Name': name,
            'Module_Name': module.__name__,
            'Function_Name': function,
            'Module': module,
            'Function': function,
            'Input': container_.copy(),
            'Output': func_obj(container_)
        }



def execute_sorting_algorithms(algorithm_names: list = None, container_: any = None, shuffle_: bool = False):
    """
    Used for executing selective present algorithms
    :param algorithm_names: The names list of the algorithms
    :param container_: The name of the container
    :param shuffle_: Boolean to check if the input needs to be shuffled or not
    :return:
    """
    # SHUFFLE THE INPUTS IF SHUFFLE IS REQUESTED
    if shuffle_:
        container_ = Shuffler.randomize_iterable_shuffler(container_)

    # SET THE MODULES USED FOR THE OPERATION OF THE PACKAGE
    set_modules(algorithm_names=algorithm_names)

    execution_wrappers = get_algorithm_pairs(package_=Sorting_Algorithms, algorithm_names=algorithm_names)

    results = list()

    for exec_items in execution_wrappers:
        entry = execute_by_wrappers(exec_items, container_=container_)
        print("Name :", entry['Name'])
        print("Module :", entry['Module_Name'])
        print("Function :", entry['Function_Name'])
#        print("Input :", entry['Input'])
#        print("Output :", entry['Output'])
        print("\n\n\n")
        results.append(entry)

    return results


if __name__ == '__main__':
    # execute_sorting_algorithms(algorithm_names=None, container_=list(range(50)), shuffle_=True)
    #execute_sorting_algorithms(algorithm_names=None, container_=list(range(50000)), shuffle_=True)
    execute_sorting_algorithms(algorithm_names=None, container_=list(range(5000)), shuffle_=True)
