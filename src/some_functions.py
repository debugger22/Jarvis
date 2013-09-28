import os

def words_to_nums(text):
	data = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'ninteen':19,'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninty':90,'hundred':100,'thousand':1000, 'lac':100000}

	words = text.split(' ')
	for i in range(len(words)):
		if words[i] in data:
			words[i] = `data[words[i]]`
	return " ".join(words)

def play_music(name = '/home/mrsud/Music/Breaking\ The\ Habit.mp3'):
	os.system("mplayer "+name)