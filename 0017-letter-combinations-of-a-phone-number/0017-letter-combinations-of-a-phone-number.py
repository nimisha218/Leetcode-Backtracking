class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {1: [], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 
                4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
                7: ["p", "q", "r", "s"], 8: ["t", "u", "v"],
                9: ["w", "x", "y", "z"]}
        

        permutations = []
        cur_combination = ""

        for digit in digits:

            cur_combination += digit

            if len(cur_combination) == 1:
                permutations.append(phone[int(digit)])
            else:

                first_list = permutations[0]
                second_list = phone[int(digit)]
               
                temp = []
                for i in first_list:
                    for j in second_list:
                        temp.append(i+j)
                permutations.pop()
                permutations.append(temp)
  
        if len(permutations) == 1:
            return permutations[0]
        else:
            return []



