import os
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_tree(path, prefix=""):
    tree_str = ""
    try:
        items = os.listdir(path)
    except PermissionError:
        return prefix + "└── [Permission Denied]\n"

    items.sort(key=lambda x: os.path.isdir(os.path.join(path, x)), reverse=True)

    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = (i == len(items) - 1)

        connector = "└── " if is_last else "├── "
        tree_str += prefix + connector + item + "\n"

        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(full_path, prefix + extension)

    return tree_str


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("目录结构导出器")
        self.root.geometry("700x500")

        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.X)

        tk.Button(btn_frame, text="选择目录并生成结构", command=self.select_dir).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(btn_frame, text="复制到剪贴板", command=self.copy).pack(side=tk.LEFT, padx=10)

        self.text = tk.Text(root, wrap="none")
        self.text.pack(fill=tk.BOTH, expand=True)

        self.result = ""

    def select_dir(self):
        path = filedialog.askdirectory()
        if not path:
            return

        self.result = os.path.basename(path) + "\n"
        self.result += generate_tree(path)

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, self.result)

    def copy(self):
        if not self.result:
            messagebox.showwarning("提示", "请先生成目录结构")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(self.result)
        messagebox.showinfo("成功", "已复制到剪贴板")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()