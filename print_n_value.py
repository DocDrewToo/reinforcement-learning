from tkinter import *

def print_table(total_visits_table, initial_rewards_table):
    n_value_maze = Tk()
    n_value_maze.title("Windy Maze 'n' Values")

    Total_visits_value_A1 = Label(n_value_maze, text=total_visits_table["A1"]["NORTH"], padx=10, pady=10)
    Total_visits_value_A2 = Label(n_value_maze, text=total_visits_table["A2"]["NORTH"], padx=10, pady=10)
    Total_visits_value_A3 = Label(n_value_maze, text=total_visits_table["A3"]["NORTH"], padx=10, pady=10)
    Total_visits_value_A4 = Label(n_value_maze, text=total_visits_table["A4"]["NORTH"], padx=10, pady=10)
    Total_visits_value_A5 = Label(n_value_maze, text=total_visits_table["A5"]["NORTH"], padx=10, pady=10)
    Total_visits_value_A6 = Label(n_value_maze, text=total_visits_table["A6"]["NORTH"], padx=10, pady=10)
    Total_visits_value_A7 = Label(n_value_maze, text=total_visits_table["A7"]["NORTH"], padx=10, pady=10)

    Total_visits_value_B1 = Label(n_value_maze, text=total_visits_table["B1"]["NORTH"], padx=10, pady=10)
    Total_visits_value_B2_W = Label(n_value_maze, text=total_visits_table["B2"]["WEST"], padx=10, pady=10)
    Total_visits_value_B2_N = Label(n_value_maze, text=total_visits_table["B2"]["NORTH"], padx=10, pady=10)
    Total_visits_value_B2_E = Label(n_value_maze, text=total_visits_table["B2"]["EAST"], padx=10, pady=10)
    Total_visits_value_B2_S = Label(n_value_maze, text=total_visits_table["B2"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_B3_W = Label(n_value_maze, text=total_visits_table["B3"]["WEST"], padx=10, pady=10)
    Total_visits_value_B3_N = Label(n_value_maze, text=total_visits_table["B3"]["NORTH"], padx=10, pady=10)
    Total_visits_value_B3_E = Label(n_value_maze, text=total_visits_table["B3"]["EAST"], padx=10, pady=10)
    Total_visits_value_B3_S = Label(n_value_maze, text=total_visits_table["B3"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_B4_W = Label(n_value_maze, text=total_visits_table["B4"]["WEST"], padx=10, pady=10)
    Total_visits_value_B4_N = Label(n_value_maze, text=total_visits_table["B4"]["NORTH"], padx=10, pady=10)
    Total_visits_value_B4_E = Label(n_value_maze, text=total_visits_table["B4"]["EAST"], padx=10, pady=10)
    Total_visits_value_B4_S = Label(n_value_maze, text=total_visits_table["B4"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_B5_W = Label(n_value_maze, text=total_visits_table["B5"]["WEST"], padx=10, pady=10)
    Total_visits_value_B5_N = Label(n_value_maze, text=total_visits_table["B5"]["NORTH"], padx=10, pady=10)
    Total_visits_value_B5_E = Label(n_value_maze, text=total_visits_table["B5"]["EAST"], padx=10, pady=10)
    Total_visits_value_B5_S = Label(n_value_maze, text=total_visits_table["B5"]["SOUTH"], padx=10, pady=10)
    B6_Wall = Label(n_value_maze, text=initial_rewards_table["B6"], padx=10, pady=10)
    Total_visits_value_B7 = Label(n_value_maze, text=total_visits_table["B7"]["NORTH"], padx=10, pady=10)

    Total_visits_value_C1 = Label(n_value_maze, text=total_visits_table["C1"]["NORTH"], padx=10, pady=10)
    C2_Wall = Label(n_value_maze, text=initial_rewards_table["C2"], padx=10, pady=10)
    Total_visits_value_C3_W = Label(n_value_maze, text=total_visits_table["C3"]["WEST"], padx=10, pady=10)
    Total_visits_value_C3_N = Label(n_value_maze, text=total_visits_table["C3"]["NORTH"], padx=10, pady=10)
    Total_visits_value_C3_E = Label(n_value_maze, text=total_visits_table["C3"]["EAST"], padx=10, pady=10)
    Total_visits_value_C3_S = Label(n_value_maze, text=total_visits_table["C3"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_C4_W = Label(n_value_maze, text=total_visits_table["C4"]["WEST"], padx=10, pady=10)
    Total_visits_value_C4_N = Label(n_value_maze, text=total_visits_table["C4"]["NORTH"], padx=10, pady=10)
    Total_visits_value_C4_E = Label(n_value_maze, text=total_visits_table["C4"]["EAST"], padx=10, pady=10)
    Total_visits_value_C4_S = Label(n_value_maze, text=total_visits_table["C4"]["SOUTH"], padx=10, pady=10)
    C5_Wall = Label(n_value_maze, text=initial_rewards_table["C5"], padx=10, pady=10)
    Total_visits_value_C6_W = Label(n_value_maze, text=total_visits_table["C6"]["WEST"], padx=10, pady=10)
    Total_visits_value_C6_N = Label(n_value_maze, text=total_visits_table["C6"]["NORTH"], padx=10, pady=10)
    Total_visits_value_C6_E = Label(n_value_maze, text=total_visits_table["C6"]["EAST"], padx=10, pady=10)
    Total_visits_value_C6_S = Label(n_value_maze, text=total_visits_table["C6"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_C7 = Label(n_value_maze, text=total_visits_table["C7"]["NORTH"], padx=10, pady=10)

    Total_visits_value_D1 = Label(n_value_maze, text=total_visits_table["D1"]["NORTH"], padx=10, pady=10)
    D2_Wall = Label(n_value_maze, text=initial_rewards_table["D2"], padx=10, pady=10)
    Total_visits_value_D3_W = Label(n_value_maze, text=total_visits_table["D3"]["WEST"], padx=10, pady=10)
    Total_visits_value_D3_N = Label(n_value_maze, text=total_visits_table["D3"]["NORTH"], padx=10, pady=10)
    Total_visits_value_D3_E = Label(n_value_maze, text=total_visits_table["D3"]["EAST"], padx=10, pady=10)
    Total_visits_value_D3_S = Label(n_value_maze, text=total_visits_table["D3"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_D4_goal = Label(n_value_maze, text=total_visits_table["D4"]["NORTH"], padx=10, pady=10)
    D5_Wall = Label(n_value_maze, text=initial_rewards_table["D5"], padx=10, pady=10)
    Total_visits_value_D6_W = Label(n_value_maze, text=total_visits_table["D6"]["WEST"], padx=10, pady=10)
    Total_visits_value_D6_N = Label(n_value_maze, text=total_visits_table["D6"]["NORTH"], padx=10, pady=10)
    Total_visits_value_D6_E = Label(n_value_maze, text=total_visits_table["D6"]["EAST"], padx=10, pady=10)
    Total_visits_value_D6_S = Label(n_value_maze, text=total_visits_table["D6"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_D7 = Label(n_value_maze, text=total_visits_table["D7"]["NORTH"], padx=10, pady=10)

    Total_visits_value_E1 = Label(n_value_maze, text=total_visits_table["E1"]["NORTH"], padx=10, pady=10)
    Total_visits_value_E2_W = Label(n_value_maze, text=total_visits_table["E2"]["WEST"], padx=10, pady=10)
    Total_visits_value_E2_N = Label(n_value_maze, text=total_visits_table["E2"]["NORTH"], padx=10, pady=10)
    Total_visits_value_E2_E = Label(n_value_maze, text=total_visits_table["E2"]["EAST"], padx=10, pady=10)
    Total_visits_value_E2_S = Label(n_value_maze, text=total_visits_table["E2"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_E3_W = Label(n_value_maze, text=total_visits_table["E3"]["WEST"], padx=10, pady=10)
    Total_visits_value_E3_N = Label(n_value_maze, text=total_visits_table["E3"]["NORTH"], padx=10, pady=10)
    Total_visits_value_E3_E = Label(n_value_maze, text=total_visits_table["E3"]["EAST"], padx=10, pady=10)
    Total_visits_value_E3_S = Label(n_value_maze, text=total_visits_table["E3"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_E4_W = Label(n_value_maze, text=total_visits_table["E4"]["WEST"], padx=10, pady=10)
    Total_visits_value_E4_N = Label(n_value_maze, text=total_visits_table["E4"]["NORTH"], padx=10, pady=10)
    Total_visits_value_E4_E = Label(n_value_maze, text=total_visits_table["E4"]["EAST"], padx=10, pady=10)
    Total_visits_value_E4_S = Label(n_value_maze, text=total_visits_table["E4"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_E5_W = Label(n_value_maze, text=total_visits_table["E5"]["WEST"], padx=10, pady=10)
    Total_visits_value_E5_N = Label(n_value_maze, text=total_visits_table["E5"]["NORTH"], padx=10, pady=10)
    Total_visits_value_E5_E = Label(n_value_maze, text=total_visits_table["E5"]["EAST"], padx=10, pady=10)
    Total_visits_value_E5_S = Label(n_value_maze, text=total_visits_table["E5"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_E6_W = Label(n_value_maze, text=total_visits_table["E6"]["WEST"], padx=10, pady=10)
    Total_visits_value_E6_N = Label(n_value_maze, text=total_visits_table["E6"]["NORTH"], padx=10, pady=10)
    Total_visits_value_E6_E = Label(n_value_maze, text=total_visits_table["E6"]["EAST"], padx=10, pady=10)
    Total_visits_value_E6_S = Label(n_value_maze, text=total_visits_table["E6"]["SOUTH"], padx=10, pady=10)
    Total_visits_value_E7 = Label(n_value_maze, text=total_visits_table["E7"]["NORTH"], padx=10, pady=10)

    Total_visits_value_F1 = Label(n_value_maze, text=total_visits_table["F1"]["NORTH"], padx=10, pady=10)
    Total_visits_value_F2 = Label(n_value_maze, text=total_visits_table["F2"]["NORTH"], padx=10, pady=10)
    Total_visits_value_F3 = Label(n_value_maze, text=total_visits_table["F3"]["NORTH"], padx=10, pady=10)
    Total_visits_value_F4 = Label(n_value_maze, text=total_visits_table["F4"]["NORTH"], padx=10, pady=10)
    Total_visits_value_F5 = Label(n_value_maze, text=total_visits_table["F5"]["NORTH"], padx=10, pady=10)
    Total_visits_value_F6 = Label(n_value_maze, text=total_visits_table["F6"]["NORTH"], padx=10, pady=10)
    Total_visits_value_F7 = Label(n_value_maze, text=total_visits_table["F7"]["NORTH"], padx=10, pady=10)

    Total_visits_value_A1.grid(row=1, column=2)
    Total_visits_value_A2.grid(row=1, column=5)
    Total_visits_value_A3.grid(row=1, column=8)
    Total_visits_value_A4.grid(row=1, column=11)
    Total_visits_value_A5.grid(row=1, column=14)
    Total_visits_value_A6.grid(row=1, column=17)
    Total_visits_value_A7.grid(row=1, column=20)

    Total_visits_value_B1.grid(row=4, column=2)
    Total_visits_value_B2_W.grid(row=4, column=4)
    Total_visits_value_B2_N.grid(row=3, column=5)
    Total_visits_value_B2_E.grid(row=4, column=6)
    Total_visits_value_B2_S.grid(row=5, column=5)
    Total_visits_value_B3_W.grid(row=4, column=7)
    Total_visits_value_B3_N.grid(row=3, column=8)
    Total_visits_value_B3_E.grid(row=4, column=9)
    Total_visits_value_B3_S.grid(row=5, column=8)
    Total_visits_value_B4_W.grid(row=4, column=10)
    Total_visits_value_B4_N.grid(row=3, column=11)
    Total_visits_value_B4_E.grid(row=4, column=12)
    Total_visits_value_B4_S.grid(row=5, column=11)
    Total_visits_value_B5_W.grid(row=4, column=13)
    Total_visits_value_B5_N.grid(row=3, column=14)
    Total_visits_value_B5_E.grid(row=4, column=15)
    Total_visits_value_B5_S.grid(row=5, column=14)
    B6_Wall.grid(row=4, column=17)
    Total_visits_value_B7.grid(row=4, column=20)

    Total_visits_value_C1.grid(row=7, column=2)
    C2_Wall.grid(row=7, column=5)
    Total_visits_value_C3_W.grid(row=7, column=7)
    Total_visits_value_C3_N.grid(row=6, column=8)
    Total_visits_value_C3_E.grid(row=7, column=9)
    Total_visits_value_C3_S.grid(row=8, column=8)
    Total_visits_value_C4_W.grid(row=7, column=10)
    Total_visits_value_C4_N.grid(row=6, column=11)
    Total_visits_value_C4_E.grid(row=7, column=12)
    Total_visits_value_C4_S.grid(row=8, column=11)
    C5_Wall.grid(row=7, column=14)
    Total_visits_value_C6_W.grid(row=7, column=16)
    Total_visits_value_C6_N.grid(row=6, column=17)
    Total_visits_value_C6_E.grid(row=7, column=18)
    Total_visits_value_C6_S.grid(row=8, column=17)
    Total_visits_value_C7.grid(row=7, column=20)

    Total_visits_value_D1.grid(row=10, column=2)
    D2_Wall.grid(row=10, column=5)
    Total_visits_value_D3_W.grid(row=10, column=7)
    Total_visits_value_D3_N.grid(row=9, column=8)
    Total_visits_value_D3_E.grid(row=10, column=9)
    Total_visits_value_D3_S.grid(row=11, column=8)
    Total_visits_value_D4_goal.grid(row=10, column=11)
    D5_Wall.grid(row=10, column=14)
    Total_visits_value_D6_W.grid(row=10, column=16)
    Total_visits_value_D6_N.grid(row=9, column=17)
    Total_visits_value_D6_E.grid(row=10, column=18)
    Total_visits_value_D6_S.grid(row=11, column=17)
    Total_visits_value_D7.grid(row=10, column=20)

    Total_visits_value_E1.grid(row=13, column=2)
    Total_visits_value_E2_W.grid(row=13, column=4)
    Total_visits_value_E2_N.grid(row=12, column=5)
    Total_visits_value_E2_E.grid(row=13, column=6)
    Total_visits_value_E2_S.grid(row=14, column=5)
    Total_visits_value_E3_W.grid(row=13, column=7)
    Total_visits_value_E3_N.grid(row=12, column=8)
    Total_visits_value_E3_E.grid(row=13, column=9)
    Total_visits_value_E3_S.grid(row=14, column=8)
    Total_visits_value_E4_W.grid(row=13, column=10)
    Total_visits_value_E4_N.grid(row=12, column=11)
    Total_visits_value_E4_E.grid(row=13, column=12)
    Total_visits_value_E4_S.grid(row=14, column=11)
    Total_visits_value_E5_W.grid(row=13, column=13)
    Total_visits_value_E5_N.grid(row=12, column=14)
    Total_visits_value_E5_E.grid(row=13, column=15)
    Total_visits_value_E5_S.grid(row=14, column=14)
    Total_visits_value_E6_W.grid(row=13, column=16)
    Total_visits_value_E6_N.grid(row=12, column=17)
    Total_visits_value_E6_E.grid(row=13, column=18)
    Total_visits_value_E6_S.grid(row=14, column=17)
    Total_visits_value_E7.grid(row=13, column=20)

    Total_visits_value_F1.grid(row=16, column=2)
    Total_visits_value_F2.grid(row=16, column=5)
    Total_visits_value_F3.grid(row=16, column=8)
    Total_visits_value_F4.grid(row=16, column=11)
    Total_visits_value_F5.grid(row=16, column=14)
    Total_visits_value_F6.grid(row=16, column=17)
    Total_visits_value_F7.grid(row=16, column=20)

    n_value_maze.mainloop()