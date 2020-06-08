# -*- coding: utf-8 -*-
# from fun import *
# from albertk import *
from transformers import BertForSequenceClassification, BertTokenizer,BertConfig
import torch
import numpy as np
import os
class TextClassification:
    """
    文本相似匹配



    """
    def __init__(self):
        pass
    def __del__(self):
        # print("释放Text()")
        try:
            pass
        except:
            pass
    def load(self,path):
        """
        加载模型
        """
        vocab_file = os.path.join(path,'vocab.txt')
        self.tokenizer = BertTokenizer.from_pretrained(vocab_file)
        # print(tokenizer)
        config = BertConfig.from_pretrained(path)
        self.model = BertForSequenceClassification.from_pretrained(path,config=config)
        # return model,tokenizer      
    def pre(self,sentence_1,sentence_2):
        """
        计算分类
        """
        # cmodel,tokenizer=load_albert_classification("tkitfiles/bert_sentence_similarity/")
        input_ids  = self.tokenizer.encode_plus(sentence_1,sentence_2)
        # print(input_ids)
        out = self.model(input_ids=torch.tensor(input_ids['input_ids']).unsqueeze(0),
                    token_type_ids= torch.tensor(input_ids['token_type_ids']).unsqueeze(0))
        # print(out)
        self.logits=out[0]
        
        self.logits.detach().numpy()
        n = self.logits.detach().numpy()
        preds = np.argmax(n, axis=1)
        return preds[0]

