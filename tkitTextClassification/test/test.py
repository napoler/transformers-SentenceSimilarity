#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import tkitTextClassification as tkitclass

tc=tkitclass.TextClassification()

sentence_1="近期上映的电影"
sentence_2="近期上映的电影有哪些"
tc.load("/mnt/data/dev/github/描述信息提交/data_description_web/tkitfiles/bert_sentence_similarity/")
c=tc.pre(sentence_1,sentence_2)
print("相关吗？",c)
