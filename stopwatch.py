import PySimpleGUI as sg
from time import time

cross = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAACwElEQVR4nO2YP2gUURDGf5OchkSx8w8iGkFQDIK6t4UgmtbA7VVprERC1EYE7RRB0MoqjQpBUlkFhOxZKFgoNmL2BIVoYRFFJKKl0RCjjkWiibnbN+9t4Gwy1d2bme/7+Obd3tsHq7GykFaSabV8EeUqMEXHTLeMTny3elomUJPyNLCuSWZI0vq5vL5cgZqUdbFKTsrY+MgKxD0CjrpqJM2aamm6qH0HdlBqf9scSbbL2Ph7b3H9hzqZnftmFzIgtey2l0BY5mBjfJY02+Ql0I2zKCTHwTYH9CsH3kZNyl8tUq1GZ01lAKpN9uZ85AqUtN5jwHZppXzLTSxDBgagw1Kr524Bh4MA+sGZFk7ldlbiO4ayeYi0PujKOwVKWt9mEeTuMdHjVm/evlsahoOAcMkq0eTgrn+/l1+auCXdatbgIVDGsmseMG+WLewzUD/J3fqUjevjIH6j0Ep8AvweK5KOb/bhBU+BC7AP3Gkd0aT81IRpb9vtzxn4X+z70HUSekxjaQQ4CHTsLAXVL4tQcRAoUEZHfwKToSQLYf+ym3EWaSoy6iLuQeiI/4aeD2x4WIxnBQfWEBeLugeFHWxdtESgVqI9RXsLCdQkPhLUIPK6CA8U/5E8Du5I4htFmIIFaiU6XIQI9EyRrnAHRZ4UIYJiz88ggZpEE6EEDRjV+HJIvbdA7e0tgex1Fv1q249ScwPpFV9OCHFww/ScUfFc7j17IbUsAZxvfCGj9hKoSZxZNZJm0ZLP603ManTdh9sUqIPRGtDIKLvfsJJmbmyVCxY3+Dj4UewbqDQ71rAGCjrs6vMZtVOgVqMBCwCYyUtY77wA2t/j3A7WGJwOzIvIuoy8+yQz2/nFlbZuFlz3MwA/jPwCTP7dC/zZ583D65ymSTQJ0t3QHHDO0754CyV9B6wNwQl9q7sJnA4Vtxr/M34DYiDT2TtHLPgAAAAASUVORK5CYII='

def create_window():
	sg.theme('black')
	layout = [
		[sg.Push(), sg.Image(cross, pad = 0, enable_events = True, key = '-CLOSE-')],
		[sg.VPush()],
		[sg.Text('', font = 'Young 50', key = '-TIME-')],
		[
			sg.Button('Start', button_color = ('#FFFFFF','#FF0000'), border_width = 0, key = '-STARTSTOP-'),
			sg.Button('Lap', button_color = ('#FFFFFF','#FF0000'), border_width = 0, key = '-LAP-', visible = False)
		],
		[sg.Column([[]], key = '-LAPS-')],
		[sg.VPush()]
	]

	return sg.Window(
		'Stopwatch', 
		layout,
		size = (300,300),
		no_titlebar = False,
		element_justification = 'center')

window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
	event, values = window.read(timeout = 10)
	if event in (sg.WIN_CLOSED, '-CLOSE-'):
		break

	if event == '-STARTSTOP-': 
		if active:
			# from active to stop
			active = False
			window['-STARTSTOP-'].update('Reset')
			window['-LAP-'].update(visible = False)
		else:
			# from stop to reset
			if start_time > 0:
				window.close()
				window = create_window()
				start_time = 0
				lap_amount = 1
			# from start to active 
			else:
				start_time = time()
				active = True
				window['-STARTSTOP-'].update('Stop')
				window['-LAP-'].update(visible = True)

	if active:
		elapsed_time = round(time() - start_time,1)
		window['-TIME-'].update(elapsed_time)

	if event == '-LAP-':
		window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount),sg.VSeparator(),sg.Text(elapsed_time)]])
		lap_amount += 1
		
window.close()