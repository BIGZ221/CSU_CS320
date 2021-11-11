from sys import argv, exit

# provided
#
# Read integers from the given filename.
#
# Return value: list of integers
def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")


# implement
#
# Return the number of inversions in the given list, by doing a merge
# sort and counting the inversions.
#
# Return value: number of inversions
def count_inversions(in_list):
  list_length = len(in_list)
  if list_length <= 1:
    return 0
  left_list = in_list[:list_length//2]
  right_list = in_list[list_length//2:]
  in_list.clear()
  left_inversions = count_inversions(left_list)
  right_inversions = count_inversions(right_list)
  total_inversions = merge_i(left_list, right_list, in_list)
  return total_inversions + left_inversions + right_inversions


# implement
#
# Merge the left & right lists into in_list.  in_list already contains
# values--replace those with the merged values.
#
# Return value: inversion count
def merge_i(l_list, r_list, in_list):
  inversions = 0
  while l_list and r_list:
    if l_list[0] > r_list[0]:
      in_list.append(r_list.pop(0))
      inversions += len(l_list)
    else:
      in_list.append(l_list.pop(0))
  in_list.extend(l_list)
  in_list.extend(r_list)
  in_list = []
  return inversions


# provided
if __name__ == '__main__':
    if len(argv) != 2:
        exit("usage: python3 "+argv[0]+" datafile")
    in_list = read_array(argv[1])
    print(count_inversions(in_list))
