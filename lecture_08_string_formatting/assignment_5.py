#  Print progress bar, each second add new symbol
# Example of progress bar can be:
# [>              ] 0.00 %
# [=>             ] 6.67 %
# [==>            ] 13.33 %
# [===>           ] 20.00 %
# [====>          ] 26.67 %
# [=====>         ] 33.33 %
# [======>        ] 40.00 %
# [=======>       ] 46.67 %
# [========>      ] 53.33 %
# [=========>     ] 60.00 %
# [==========>    ] 66.67 %
# [===========>   ] 73.33 %
# [============>  ] 80.00 %
# [=============> ] 86.67 %
# [==============>] 93.33 %
# [===============] 100.00 %

from time import sleep
bar_length = 15

for i in range(bar_length+1):
    bar = "="*i + ">"
    percentage = i/bar_length
    print(f"[{bar:15.15}] {percentage:.2%}")

    sleep(1)
