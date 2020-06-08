# -*- coding: utf-8 -*-

class TextClassification:
    """
    文本分类



    """
    def __init__(self,ht_model=None):
        self.ht_model=ht_model
        pass
    def __del__(self):
        # print("释放Text()")
        try:
           del self.ht_model
        except:
            pass
       
    