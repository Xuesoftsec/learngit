def sum_number(num):
    print(num)
    # 一定要有递归的出口，当参数满足某个条件时，不再执行函数
    if num == 1:
        return

    # 自己调用自己
    sum_number(num -1)

sum_number(3)

