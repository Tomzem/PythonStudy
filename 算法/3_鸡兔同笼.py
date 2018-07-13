head_num = int(input("头："))
foot_num = int(input("脚："))

K = foot_num - 2*head_num
if K % 2 != 0 or K <= 0 or K >= 2*head_num:
    print("无解")
else:
    Z = int(K/2)
    J = int(head_num - Z)
    print("兔子有{}只，鸡有{}只".format(Z, J))
