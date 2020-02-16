# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается. Использовать функцию sorted и метод sort запрещается.

def merge_all(list1, list2):
    i = 0
    j = 0
    return_list = []
    for k in range(len(list1+list2)):
        if len(list1) == i:
            return_list.extend(list2[j:])
            break
        elif len(list2) == j:
            return_list.extend(list1[i:])
            break
        elif list1[i] <= list2[j]:
            return_list.append(list1[i])
            i += 1
        else:
            return_list.append(list2[j])
            j += 1
    return return_list

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(*merge_all(list1, list2))
