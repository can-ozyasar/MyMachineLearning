
#pandas genelde veri analizi ve veri manipülasyonu için kullanılan bir kütüphanedir.
#pandas modülü ağırlıklı olarak dataframe adı verilen bir tür tablo benzeri yapılar ile çalışır 
#çalışacağımız veri setini önce indirememiz gerekiyor.


#biz bu örnekte imdb_top_1000.csv adlı veri setini kullanacağız.

import pandas as pd


df=pd.copy("imdb_top_1000.csv")

df.head(5)
# df.tail(5)
# df.shape
# len(df)
# df.columns