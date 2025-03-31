# Fixed Point Calculator
# Author: Mark Nemet
# Date: 31.03.2025
# Description: This script provides a GUI for converting natural numbers to fixed point representations and vice versa.
# https://github.com/nmark19/fixpointcalculator

import tkinter

window = tkinter.Tk()
window.title("Fixed point calculator")
window.geometry("400x400")

def Input_RAW_CONVERTER():
    input_number_LSB=float(input_number_user.get())
    Input_to_LSB_Spinbox_int=int(Input_to_LSB_Spinbox.get())
    output_number_variable=(input_number_LSB*2**Input_to_LSB_Spinbox_int)
    output_number_LSB.delete(0, tkinter.END)
    output_number_LSB.insert(0, str(output_number_variable))
    output_number_LSB_r.delete(0, tkinter.END)
    output_number_LSB_r.insert(0, str(round(output_number_variable)))

def Output_RAW_CONVERTER():
    B_input_number_LSB=float(B_input_number_user.get())
    B_Input_to_LSB_Spinbox_int=int(B_Input_to_LSB_Spinbox.get())
    B_output_number_variable=(B_input_number_LSB/2**B_Input_to_LSB_Spinbox_int)
    B_output_number_LSB.delete(0, tkinter.END)
    B_output_number_LSB.insert(0, str(B_output_number_variable))


frame = tkinter.Frame(window)
frame.pack()

# saving user
user_info_frame = tkinter.LabelFrame(frame, text="Natural number to fixed point")
user_info_frame.grid(row=0,column=0)

#Normal number to LSB shift
Input_to_LSB=tkinter.Label(user_info_frame, text="Input number")
Input_to_LSB.grid(row=0, column=0)

input_number_user =tkinter.Entry(user_info_frame,)
input_number_user.grid(row=1, column=0)

Input_to_LSB=tkinter.Label(user_info_frame, text="Resolution (bit)")
Input_to_LSB.grid(row=2, column=0)

Input_to_LSB_Spinbox=tkinter.Spinbox(user_info_frame, from_=1, to = 30)
Input_to_LSB_Spinbox.grid(row=3, column=0)

LSB_button = tkinter.Button(user_info_frame, text="Calculate", font=("Arial", 12),command=Input_RAW_CONVERTER)
LSB_button.grid(row=4, column=0)


output_number_text=tkinter.Label(user_info_frame, text="-------------------------------")
output_number_text.grid(row=5, column=0)

output_number_LSB =tkinter.Entry(user_info_frame)
output_number_LSB.grid(row=6, column=0)

output_number_text=tkinter.Label(user_info_frame, text="Round value")
output_number_text.grid(row=7, column=0)

output_number_LSB_r =tkinter.Entry(user_info_frame)
output_number_LSB_r.grid(row=8, column=0)
#user_info_frame.pack()


#########################back
# saving user
user_info_frame_B = tkinter.LabelFrame(frame, text="Fixed point to natural number")
user_info_frame_B.grid(row=0,column=1)

#Normal number to LSB shift
B_Input_to_LSB=tkinter.Label(user_info_frame_B, text="Fixed point input number")
B_Input_to_LSB.grid(row=0, column=1)

B_input_number_user =tkinter.Entry(user_info_frame_B)
B_input_number_user.grid(row=1, column=1)

B_Input_to_LSB=tkinter.Label(user_info_frame_B, text="Resolution (bit)")
B_Input_to_LSB.grid(row=2, column=1)

B_Input_to_LSB_Spinbox=tkinter.Spinbox(user_info_frame_B, from_=1, to = 30)
B_Input_to_LSB_Spinbox.grid(row=3, column=1)

B_LSB_button = tkinter.Button(user_info_frame_B, text="Calculate", font=("Arial", 12),command=Output_RAW_CONVERTER)
B_LSB_button.grid(row=4, column=1)


B_output_number_text=tkinter.Label(user_info_frame_B, text="-------------------------------")
B_output_number_text.grid(row=5, column=1)

B_output_number_LSB =tkinter.Entry(user_info_frame_B)
B_output_number_LSB.grid(row=6, column=1)

B_output_number_text=tkinter.Label(user_info_frame_B, text="")
B_output_number_text.grid(row=7, column=1)

B_output_number_text=tkinter.Label(user_info_frame_B, text="")
B_output_number_text.grid(row=8, column=1)


window.mainloop()



