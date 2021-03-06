import tkinter as tk
import time
from random import randint

# answer generater
def random_ans():
	ans = ""
	tmp = ""
	cnt = 0
	while 1:
		if cnt == 4:
			break
		else:
			tmp = str(randint(0, 9))
			if tmp in ans:
				cnt -= 1
			else:
				ans += tmp
		cnt += 1
	return ans

# buttom funtion
def print_num():
	# announce start
	statustext.set("processing...")
	statusbar.update()
	# working
	num = num_string.get() 
	main(num, ans)
	time.sleep(0.25)
	# announce done
	statustext.set("done")
	statusbar.update()

# size
app = tk.Tk()
app.title("幾A幾B(不重複)")
app.geometry('400x100')

# set frame
# input frame
div_input = tk.Frame(app, width=400, height=10)
div_input.pack(anchor=tk.W)
# output frame
div_output = tk.Frame(app, width=400, height=30)
div_output.pack()

# 輸入欄位
input_num = tk.Label(div_input, text = "input: ")
input_num.pack(side=tk.LEFT, padx=20, pady=10)
num_string = tk.StringVar()
input_div = tk.Entry(div_input, width=20, textvariable=num_string)
input_div.pack(side=tk.LEFT, padx=20, pady=10)

# 確定按鈕
result_button = tk.Button(div_input, text = 'Get Result',command=print_num)
result_button.pack(side=tk.LEFT, padx=20, pady=10)

# 結果欄位
result_string=tk.StringVar()
result_label = tk.Label(div_output, textvariable=result_string)
result_label.pack()

# 狀態列
statustext = tk.StringVar()
statustext.set('ready')
statusbar = tk.Label(app, textvariable=statustext, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)


def split(word):
    return [char for char in word]
# main
def main(num, ans):
	a=0
	b=0
	ans = split(ans)
	num = split(num)
	for i in range(4):
		if num[i] == ans[i]:
			a+=1
		elif num[i] in ans:
			b+=1
	if a == 4:
		result_string.set("You win the game!")
		statustext.set("THE_END")
		statusbar.update()
		time.sleep(2)
		app.destroy()
	else:
		result_string.set("%dA %dB"%(a,b))

	

# run
ans = random_ans()
app.mainloop()
