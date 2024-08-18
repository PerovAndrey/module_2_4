# list = ['one', 'two', 'three']
# for i in list:
#     if i == 'three':
#         list.remove(i)
# print(list)
# list = ['one', 'two', 'three']
# for i in range(len(list)):
#     list[i] = ' :( '
#     print(list[i])
# list = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i*j}')
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i, dict_[i])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not Primes: ', not_primes)