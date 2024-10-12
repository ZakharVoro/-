import PySimpleGUI as sg      
import time
import math
#строение программы 

sg.theme('DarkAmber')    

layout = [[sg.Text('Введите ширину профеля в метрах.')],
      	[sg.InputText()],
      	[sg.Text('Введите длину профеля в метрах.')],
      	[sg.InputText()],
      	[sg.Text('Введите длину крыши в метрах.')],
      	[sg.InputText()],
      	[sg.Text('Введите ширину крыши в метрах.')],
      	[sg.InputText()],
      	[sg.Text('Нужно листов:'),sg.Text(key ='-OUTPUT-')],
      	[sg.Button('Считать'), sg.Button('Выход')]]      

window = sg.Window('СтройСчет', layout)                                  

#главный цикл
while True:
	try:
		event, values = window.read()   


		length = float(values[0])
		width = float(values[1])
		l_area = float(values[2])
		w_area = float(values[3])

		if event in (None, 'Считать'):
			def calculate_number_of_sheets(w_area,l_area, width, length):
				length = float(values[0])
				width = float(values[1])
				l_area = float(values[2])
				w_area = float(values[3])
				sheet_area = length * width
				area = l_area * w_area
				num = math.ceil((area // sheet_area))
				if num == 0:
					num = 1
				print(num)
				window['-OUTPUT-'].update(num)
			calculate_number_of_sheets(w_area,l_area, width, length)
	except:
		pass		
	if event == sg.WIN_CLOSED or event == 'Выход':
		break
		window.close()

window.close()
		