import json
import codecs
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

with open('novel_rank.json',encoding='utf-8') as f:
	novel_list = []
	for line in f.readlines():
		# print(line.strip())
		novel_dict = json.loads(line.strip())
		novel_list.append(novel_dict)

names,yuepiao = [],[] 
for data in novel_list[:50]:
	novel_name = data['novel_name']
	monthCount = {
		'value': int(data['monthCount']),
		'label': data['author']
	}
	names.append(novel_name)
	yuepiao.append(monthCount)

# print(names)
# print(yuepiao)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.title_font_size = 24
my_config.lable_font_size = 20
my_config.show_legend = False
my_config.major_label_font_size = 18
my_config.tuncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(my_config,style=my_style)
chart.title = "QiDian Novel Rank Top 50" 
chart.x_labels = names
chart.add('',yuepiao)
chart.render_to_file('NovelTop50.svg')













