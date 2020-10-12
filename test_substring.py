import argparse

def check_sub(in_str,in_sub):
    j=len(in_sub)
    results=[]
    for i in range(len(in_str)-j+1):
        #print(in_str[i:i+j])
        if in_str[i:i+j] == in_sub:
           results.append(i)
    return len(results)

def check_sub_2(in_str,in_sub):
    from collections import Counter
    results=Counter([ in_str[i : i+len(in_sub)] for i in range(len(in_str) - len(in_sub)+1) ])
    print(results)
    return results[in_sub]



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the occurences of a substring in a string")
    parser.add_argument("--in_string",'-s',required=True)
    parser.add_argument("--in_sub","-u",required=True)
    args=parser.parse_args()
    in_str=args.in_string
    in_sstr = args.in_sub
    #print(f'{in_str}, {in_sstr}')
    #result=check_sub(in_str,in_sstr)
    result=check_sub_2(in_str,in_sstr)
    print(f'{result}')

