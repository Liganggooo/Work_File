from os import path
import jieba
import jieba.analyse as analyse
import jieba.posseg as pseg
#提取当前文件的绝对路径
d = path.dirname(__file__)
text_path = 'littledoc.txt'
#拼接文件路径
text = open(path.join(d,text_path)).read()

# with open(path.join(d,text_path),'r') as f:
# 	text  = f.read()

#自定义词库
# jieba.add_word('邵俊杰')
# 	print(text)

#自定义词库
jieba.load_userdict('userdict.txt')
#全模式cut_all = true
# seg_list = jieba.cut(text,cut_all = True,HMM = False)
# print(','.join(seg_list))
#默认模式cut_all = false
seg_list = jieba.cut(text,cut_all = False,HMM = True)
print(' '.join(seg_list))
print('*'*90)
#词性标注
results = pseg.cut(text)
for result in results:
	print(result.word,result.flag)

#搜索引擎模式 
# seg_list = jieba.cut(text,HMM = False)
# print(','.join(seg_list))

#g关键词提取
# for key in analyse.extract_tags(text,50,withWeight = False):
# 	print(key)





