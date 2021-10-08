import os

def read_text_from_file(file_name):
	data = None
	try:
		with open(f'info_pages\info_texts\{file_name}', 'r', encoding='utf-8') as f:
			data = f.read()
	except FileNotFoundError:
		pass
	finally:
		return data