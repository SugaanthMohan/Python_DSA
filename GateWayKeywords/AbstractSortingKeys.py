from collections import defaultdict

sorting_keywords = {
    'Your_File_Name': '__Execution__Function__',
    'Merge_Sort': 'mergesort'
}

sorting_keywords = defaultdict(lambda: 'process', sorting_keywords)
