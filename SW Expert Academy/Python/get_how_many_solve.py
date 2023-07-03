import os

D3_path = r'C:\Users\wansang\Desktop\Gitrep\Algorithm\SW Expert Academy\Python\Python D3'
D2_path = r'C:\Users\wansang\Desktop\Gitrep\Algorithm\SW Expert Academy\Python\Python D2'
D1_path = r'C:\Users\wansang\Desktop\Gitrep\Algorithm\SW Expert Academy\Python\Python D1'

def get_files_count(folder_path):
	dirListing = os.listdir(folder_path)
	return len(dirListing)
	
if __name__ == "__main__":
	print('D3 -', get_files_count(D3_path))
	print('D2 -', get_files_count(D2_path))
	print('D1 -', get_files_count(D1_path))
