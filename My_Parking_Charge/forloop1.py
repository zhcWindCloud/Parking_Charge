from  . import  models
import  random,datetime
list=["丽",'互','大','达','你']
def fo():
    for i in range(10):
        models.VIPuserInfo.objects.create(user_nanme=random.choice(list),
                                      user_ID= "皖D.489"+str(i),
                                      user_phone= "78965"+str(i)+"369",user_birth=datetime.datetime.now(),user_sex="男",
                                      user_grade=str(i+7)+"8")


