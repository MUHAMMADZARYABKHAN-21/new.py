# # # # # # # import pandas as pd
# # # # # # # import seaborn as sns
# # # # # # # import matplotlib.pyplot as plt
# # # # # # # df=pd.read_csv("Titanic1.csv")
# # # # # # # sns.histplot(
# # # # # # #     data=df,
# # # # # # #     x="age",
# # # # # # #     kde=True,
# # # # # # # )
# # # # # # # plt.show()
# # # # # # import pandas as pd
# # # # # # import seaborn as sns
# # # # # # import matplotlib.pyplot as plt
# # # # # #
# # # # # # df = pd.read_csv("Titanic1.csv")
# # # # # #
# # # # # # sns.displot(data=df,x="age")
# # # # # # plt.show()
# # # # #
# # # # # import pandas as pd
# # # # # import seaborn as sns
# # # # # import matplotlib.pyplot as plt
# # # # # df=pd.read_csv("Titanic1.csv")
# # # # # # sns.displot(
# # # # # #     data=df,
# # # # # #     x="age",
# # # # # #     kde=True,
# # # # # #     color="blue",
# # # # # #     col="sex"
# # # # # # )
# # # # # sns.displot(
# # # # #     data=df,
# # # # #     x="age",
# # # # #     color="green",
# # # # #     col="sex"
# # # # # )
# # # # # plt.title("Fare distribution")
# # # # #
# # # # # plt.show()
# # # #
# # # # import pandas as pd
# # # # import seaborn as sns
# # # # import matplotlib.pyplot as plt
# # # # df=pd.read_csv("Titanic1.csv")
# # # # # sns.displot(
# # # # #     data=df,
# # # # #     x="age",
# # # # #     kde=True,
# # # # #     color="blue",
# # # # #     col="sex"
# # # # # )
# # # # sns.displot(
# # # #     data=df,
# # # #     x="fare",
# # # #     color="green",
# # # #     col="pclass"
# # # # )
# # # # plt.title("Fare distribution")
# # # #
# # # # plt.show()
# # #
# # # import pandas as pd
# # # import seaborn as sns
# # # import matplotlib.pyplot as plt
# # # from numpy.ma.core import size
# # #
# # # df=pd.read_csv("Titanic1.csv")
# # # # sns.displot(
# # # #     data=df,
# # # #     x="age",
# # # #     kde=True,
# # # #     color="blue",
# # # #     col="sex"
# # # # )
# # # sns.displot(
# # #     data=df,
# # #     x="fare",
# # #     row="sex",
# # #     col="pclass"
# # #
# # # )
# # # plt.title("Fare distribution")
# # #
# # # # plt.show()
# # # import pandas as pd
# # # import seaborn as sns
# # # import matplotlib.pyplot as plt
# # #
# # # df = pd.read_csv("Titanic1.csv")
# # # sns.ecdfplot(
# # #     data=df,
# # #     x="age",
# # # )
# # # plt.show()
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# #
# # df = pd.read_csv("Titanic1.csv")
# # sns.boxplot(
# #     data=df,
# #     x="fare"
# # )
# # plt.title("Distribution of fare ")
# # plt.show()
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Load Titanic dataset
# df = pd.read_csv("Titanic1.csv")
#
# # Select numeric columns
# numeric_df = df[["survived", "pclass", "age", "sibsp", "parch", "fare"]]
#
# # Drop rows with missing values (NaN) to avoid clustering errors
# numeric_df = numeric_df.dropna()
#
# # Create clustermap
# sns.clustermap(
#     numeric_df.corr(),   # use correlation matrix instead of raw data
#     annot=True,
#     cmap="coolwarm",
#     center=0
# )
#
# plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Titanic1.csv")

plt.figure(figsize=(8,5))

sns.regplot(
    data=df,
    x="age",
    y="fare"
)

plt.title("Age vs Fare")

plt.show()
