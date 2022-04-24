import PySimpleGUI as sg

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def convert_mass(myNum, myCase, isInverse):
	match myCase:
		case 'kg to pound':
			if isInverse:
				output = round(myNum / 2.20462,2)
				output_string = f'{myNum} pounds are {output} kg'
			else:
				output = round(myNum * 2.20462,2)
				output_string = f'{myNum} kg are {output} pounds.'
			return output_string
		case '2': return False
		case '3': return False

def convert_length(myNum, myCase, isInverse):
	match myCase:
		case 'km to mile':
			if isInverse:
				output = round(myNum / 0.6214,2)
				output_string = f'{myNum} miles are {output} km'
			else:
				output = round(myNum * 0.6214,2)
				output_string = f'{myNum} km are {output} miles.'
			return output_string
		case '2': return False
		case '3': return False

def convert_time(myNum, myCase, isInverse):
	match myCase:
		case 'sec to min':
			if isInverse:
				output = round(myNum * 60,2)
				output_string = f'{myNum} minutes are {output} seconds'
			else:
				output = round(myNum / 60,2)
				output_string = f'{myNum} seconds are {output} minutes.'
			return output_string
		case '2': return False
		case '3': return False

mass_tab = [[sg.T("Choose a mass conversion from list")],
				[sg.Combo(['kg to pound', ''], key = '-UNITS-M')],
				[sg.Input(key = '-INPUT-M')]]
length_tab = [[sg.T("Choose a length conversion from list")],
				[sg.Combo(['km to mile', ''], key = '-UNITS-L')],
				[sg.Input(key = '-INPUT-L')]]
time_tab = [[sg.T("Choose a time conversion from list")],
				[sg.Combo(['sec to min', ''], key = '-UNITS-T')],
				[sg.Input(key = '-INPUT-T')]]

layout = [[sg.TabGroup([[sg.Tab('Mass', mass_tab), sg.Tab('Length', length_tab), sg.Tab('Time', time_tab)]], key = '-TABGROUP-')],
			[sg.Checkbox(['Convert reverse'], key = '-INVERSE-')],
			[sg.Button('Convert', key = '-CONVERT-')],
			[sg.Text('Output', key = '-OUTPUT-')]]
window = sg.Window('Converter',layout)

while True:
	event, values = window.Read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-CONVERT-':
		match values['-TABGROUP-']:
			case 'Mass':
				input_value = values['-INPUT-M']
				output_string = convert_mass(float(input_value), values['-UNITS-M'], values['-INVERSE-'])
			case 'Length': 
				input_value = values['-INPUT-L']
				output_string = convert_length(float(input_value), values['-UNITS-L'], values['-INVERSE-'])
			case 'Time': 
				input_value = values['-INPUT-T']
				output_string = convert_time(float(input_value), values['-UNITS-T'], values['-INVERSE-'])
		
		if input_value.isnumeric() or is_number(input_value):
			window['-OUTPUT-'].update(output_string)
		else:
			window['-OUTPUT-'].update('Please enter a number')

window.close()