# # # # import pandas as pd
# # # # import seaborn as sns
# # # # import matplotlib.pyplot as plt
# # # # df=pd.read_csv("Titanic1.csv")
# # # # sns.histplot(
# # # #     data=df,
# # # #     x="age",
# # # #     kde=True,
# # # # )
# # # # plt.show()
# # # import pandas as pd
# # # import seaborn as sns
# # # import matplotlib.pyplot as plt
# # #
# # # df = pd.read_csv("Titanic1.csv")
# # #
# # # sns.displot(data=df,x="age")
# # # plt.show()
# #
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # df=pd.read_csv("Titanic1.csv")
# # # sns.displot(
# # #     data=df,
# # #     x="age",
# # #     kde=True,
# # #     color="blue",
# # #     col="sex"
# # # )
# # sns.displot(
# #     data=df,
# #     x="age",
# #     color="green",
# #     col="sex"
# # )
# # plt.title("Fare distribution")
# #
# # plt.show()
#
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# df=pd.read_csv("Titanic1.csv")
# # sns.displot(
# #     data=df,
# #     x="age",
# #     kde=True,
# #     color="blue",
# #     col="sex"
# # )
# sns.displot(
#     data=df,
#     x="fare",
#     color="green",
#     col="pclass"
# )
# plt.title("Fare distribution")
#
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.ma.core import size

df=pd.read_csv("Titanic1.csv")
# sns.displot(
#     data=df,
#     x="age",
#     kde=True,
#     color="blue",
#     col="sex"
# )
sns.displot(
    data=df,
    x="fare",
    row="sex",
    col="pclass"

)
plt.title("Fare distribution")

plt.show()
