# -*- coding: utf-8 -*-

import os
import click

# 定义 GBK 转 UTF-8 函数
def gbk_to_utf8(src_file, dst_file):
    with open(src_file, 'rb') as f:
        content = f.read()
    try:
        content = content.decode('gbk').encode('utf-8')
        with open(dst_file, 'wb') as f:
            f.write(content)
        print(f"转换成功：{src_file} -> {dst_file}")
    except UnicodeDecodeError:
        print(f"文件 {src_file} 不是 GBK 编码")

# 定义 Click 命令行参数
@click.command()
@click.argument('src_dir')
@click.argument('dst_dir')

# 定义 Click 命令行函数
def convert(src_dir, dst_dir):
    # 判断源文件夹是否存在
    if not os.path.exists(src_dir):
        print(f"文件夹 {src_dir} 不存在")
        return

    # 判断目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # 遍历源文件夹中的所有文件，并调用 GBK 转 UTF-8 函数
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_dir, file)
            gbk_to_utf8(src_file, dst_file)

if __name__ == '__main__':
    convert()
