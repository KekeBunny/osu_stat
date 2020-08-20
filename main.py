from fetch_data import get_data
from scatter import load_data, show_data

mode = input("please input a game mode(0:Standard, 1:Taiko, 2:Catch The Beat, 3:Mania):")
while mode not in ['0', '1', '2', '3']:
    mode = input("Wrong input!\nplease input a game mode(0:Standard, 1:Taiko, 2:Catch The Beat, 3:Mania):")
mode = int(mode)

Min = input("please input the minimum rank you want to show:")
while not Min.isdigit() or int(Min) <= 0 or int(Min) > 100000:
    Min = input("Minimum rank should between 1 and 100,000!\nplease input the minimum rank you want to show:")
Min = int(Min)

Max = input("please input the maximum rank you want to show:")
while not Max.isdigit() or int(Max) < Min or int(Max) > 100000:
    Max = input("Minimum rank should between minimum rank and 100,000!\nplease input the minimum rank you want to show:")
Max = int(Max)

if not get_data(mode, Min, Max):
    print('Get data failed, please check your network connection.')
else:
    show_data(mode, load_data(), Min, Max)
