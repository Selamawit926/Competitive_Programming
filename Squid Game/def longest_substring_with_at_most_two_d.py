def take_input():
    given_string = input()
    return  given_string

def longest_substring_with_at_most_two_distinct_characters( input_string ):
     
    letters = {}
    result =0
    start =0
    
    for ed in range(len(input_string)):
        if input_string[ed] not in letters and len(letters) < 2:
            letters[input_string[ed]] = 1
            result = max(result, ed-start + 1)
        elif input_string[ed] in letters:
            letters[input_string[ed]] += 1
            if input_string[start]!=input_string[ed]:
                result = max(result, ed-start + 1)
        else:
            while len(letters) == 2:
                letters[input_string[start]] -= 1
                if letters[input_string[start]] == 0 :
                    del letters[input_string[start]]
                start += 1
            letters[input_string[ed]] = 1   
               
    return result
    

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        input_string = take_input()
        answer = longest_substring_with_at_most_two_distinct_characters( input_string )
        print(answer) 