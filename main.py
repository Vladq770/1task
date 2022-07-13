def decorator_with_hashing(func):
    def wrapper(number: int):
        key = str(number)
        res = wrapper.dict_of_hash.get(key)
        print(wrapper.dict_of_hash)
        if res is None:
            wrapper.dict_of_hash[key] = func(number)
            print("It was the first function call with given parameters")
            return wrapper.dict_of_hash.get(key)
        else:
            print("It wasn't the first function call with given parameters")
            return res

    wrapper.dict_of_hash = {}
    return wrapper


@decorator_with_hashing
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(10))
    print(multiplier(13))
    print(multiplier(5))
    print(multiplier(10))
    print(multiplier(10))
