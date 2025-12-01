import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

# Thiết lập phong cách hiển thị của 1 sơ đồ
sns.set_theme(style="whitegrid")

# Tạo ra 1 dữ liệu mẫu
# dataSource = sns.load_dataset("data-demo")
tips = sns.load_dataset("tips")

# Tạo figure thông qua plt
plt.figure(figsize=(8, 6))

# hisplot
# sns.histplot(
#     data=iris,
#     x="sepal_length",
#     bins=20, # Chỉ định số lượng khoảng
#     hue="species", # Phân tách giữa các cột trong biểu đồ
#     multiple="stack"
# )

# Kdeplot
# sns.kdeplot(
#     data=iris,
#     x="sepal_length",
#     bin=20,
#     hue="species"
# )

# displot
# sns.displot(
#     data=titanic,
#     x="age",
#     y="fare"
# )

# Scarterplot
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    size="size"
)


# Đặt tiêu đề và nhãn cho biểu đồ
plt.title("Tiêu đề của biểu đồ")
plt.xlabel("Trục X")
plt.ylabel("Trục Y")

# Hiển thị figure
plt.show()