from fun import *
from albertk import *
from transformers import BertForSequenceClassification, BertTokenizer,AlbertConfig
# import synonyms

def load_albert_classification(path):
    """
    加载模型
    """
    vocab_file = os.path.join(path,'vocab.txt')
    tokenizer = BertTokenizer.from_pretrained(vocab_file)
    # print(tokenizer)
    config = AlbertConfig.from_pretrained(path)
    model = BertForSequenceClassification.from_pretrained(path,config=config)
    return model,tokenizer



# model,tokenizer=load_albert("tkitfiles/albert_tiny")



# sen1 = "发生历史性变革"
# sen2 = "发生历史性的变革"
# r = synonyms.compare(sen1, sen2, seg=True)
# print(r)

def SentenceSimilarity(sentence_1,sentence_2):
    """
    计算相似度
    """
    cmodel,tokenizer=load_albert_classification("tkitfiles/bert_sentence_similarity/")
    input_ids  = tokenizer.encode_plus(sentence_1,sentence_2)
    # print(input_ids)
    out = cmodel(input_ids=torch.tensor(input_ids['input_ids']).unsqueeze(0),
                token_type_ids= torch.tensor(input_ids['token_type_ids']).unsqueeze(0))
    # print(out)
    logits=out[0]
    logits.detach().numpy()
    n = logits.detach().numpy()
    preds = np.argmax(n, axis=1)
    # print(preds)
    return preds[0]




file_list=["/mnt/data/dev/github/lcqmcdatatex/lcqmcdatatex/test.txt"]
a=0
r=0
for file_neme in file_list:
    with open(file_neme, "r") as f:
        for it in  f.readlines():
            print("#"*20)
            t=it.replace("\n", "").split("\t")
            print(t)
            # a="商排名11"
            # b="智商排名第11"
            p=SentenceSimilarity(t[0],t[1])
            # print(p)
            one={
                "label":p,
                'sentence':t[0],
                'sentence1':t[1]
            }
            print(one)
            a=a+1
            if p==int(t[2]):
                r=r+1
            print("统计：",r,a,r/a)


# exit()

# def auto_Similarity(data):

#     for it in range(len(data)):

#         word=data[it]['word']
#         # del data[it]
#         for item in data:
#             sent2=item['word']
#             #相似程度
#             r = synonyms.compare(word, sent2, seg=True)
#             if r>0.5:
#                 print(word,sent2)
#                 print(r)
#                 print("#"*20)




#         # print()
#     pass


# ner_input=input("实体：")
# miaoshu=get_miaoshu(ner_input,1000)
# if len(miaoshu)>10:

#     # 执行聚类操作


#     sent_miaoshu=[]
#     sent_miaoshu_ranks={}
#     for s_m in miaoshu:
#         sent_miaoshu.append(s_m['value'])
#         sent_miaoshu_ranks[s_m['value']]=s_m['rank']
#     klist=kmeans_sk_content(sent_miaoshu,tokenizer,model,int(len(sent_miaoshu)*0.10))
#     # print(klist)
#     for k in klist.keys(): 
#     # l,s=get_sumy("。".join(klist[k]))
#         if len(klist[k])>0:
#             k_data=[]
#             for k_i in klist[k]:
#                 one={"rank":sent_miaoshu_ranks[k_i],"word":k_i}
#                 k_data.append(one)
#             if len(k_data)>1:
#                 # print("k_data",len(k_data),k_data)
#                 auto_Similarity(k_data)
