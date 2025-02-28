def flatten(lst):
    result = []
    for i in lst:
        print("Instance from 1",isinstance(i, list))
        if isinstance(i, list):
            result.extend(flatten(i))
            print("value of result ",result.extend(flatten(i)))
        else:
            result.append(i)
    return result

print(flatten([[1, 2, [3]], 4, 5]))

#output
Instance from 1 True
Instance from 1 False
Instance from 1 False
Instance from 1 True
Instance from 1 False
Instance from 1 False
value of result  None
Instance from 1 False
Instance from 1 False
Instance from 1 True
Instance from 1 False
Instance from 1 False
value of result  None
value of result  None
Instance from 1 False
Instance from 1 False
[1, 2, 3, 3, 1, 2, 3, 3, 4, 5]
