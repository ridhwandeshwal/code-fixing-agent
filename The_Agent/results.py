from tools.validate import validate_patch
from tools.extract_code import extract_code
from tools.write_temp import write_patch
from tools.llm_call import generate_fix
from tools.context_extract import extract_context
p_names=[ 'breadth_first_search',
          'bucketsort', 'depth_first_search',
          'detect_cycle', 
          'find_in_sorted', 'flatten', 'gcd', 'get_factors', 'hanoi', 
          'is_valid_parenthesization', 'kheapsort', 'knapsack', 'kth', 
          'lcs_length', 'levenshtein', 'lis', 'longest_common_subsequence', 
          'max_sublist_sum', 'mergesort', 'minimum_spanning_tree', 
          'next_palindrome', 'next_permutation', 
          'node', 'pascal', 'possible_change', 'powerset', 'quicksort', 
          'reverse_linked_list',  'rpn_eval', 
          'shortest_paths', 'shortest_path_length', 
          'shortest_path_lengths', 'shunting_yard', 'sieve', 
          'subsequences', 'topological_ordering', 
          'to_base', 'wrap']
for program_name in p_names:
    res=validate_patch(program_name)
    print(res)