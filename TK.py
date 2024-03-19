import tkinter as tk
from tkinter import messagebox
from Model.Try_LogisticRegression import LogisticR

class SimpleGUI:
    def __init__(self, model):
        self.model = model  # 模型实例
        self.window = tk.Tk()
        self.window.title("特征输入")
        # 添加标签和输入框
        self.entries = []
        for i in range(self.model.input_dim):  # 假设模型有一个属性input_dim表示输入特征的数量
            tk.Label(self.window, text=f'特征 {i+1}:').grid(row=i, column=0)
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=1)
            self.entries.append(entry)
        # 添加预测按钮
        predict_button = tk.Button(self.window, text='预测', command=self.predict)
        predict_button.grid(row=self.model.input_dim, column=1)
        # 运行主循环
        self.window.mainloop()

    def predict(self):
        # 获取输入特征
        features = []
        for entry in self.entries:
            try:
                features.append(float(entry.get()))
            except ValueError:
                messagebox.showerror("输入错误", "请确保所有输入都是数值")
                return

        # 调用模型预测
        prediction = self.model.predict([features])[0]

        # 显示结果
        result = f"判决结果：{'类别1' if prediction == 1 else '类别0'}"
        messagebox.showinfo("预测结果", result)

# 假设你的模型实例为model，并且模型预期接收两个特征
model = LogisticR()  # 模型初始化
model.input_dim = 18  # 假设我们的模型需要两个特征输入
# 创建并运行GUI
app = SimpleGUI(model)
