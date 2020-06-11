# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:20:36 2020


功能说明：
	本脚本用于将 markdown 格式的图片链接转换为 html 格式的 img 标签
	用来解决博客导入 MD 文件后出现的图片插入失败问题

使用说明：
    transform 
    读取文件 URL，将所有 md 格式的 img 标签转换为 html 格式
    输出到当前文件夹下

@author: Yugar
"""

import re
import os

def transform(input_path, output_path, file_name):
    '''
        read
    '''
    src_url = os.path.join(input_path, file_name)
    dst_url = os.path.join(output_path, file_name)
    
    with open(src_url,'r',encoding='utf-8',errors='ignore') as f:
        lines = f.readlines()
    
    '''
        process
    '''
    pattern = r"\!\[([\d\D]*)\]\((https:[\d\D]*)\)"
    rpl = r'<img src="\2" alt="\1" style="zoom:100%;" />'
    
    res_lines = []
    
    '''
        output
    '''
    f_out = open(dst_url, 'w', encoding='utf-8')

    # head_line = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">"
    # f_out.write(head_line)
    # f_out.write("\n\n")
    
    for raw_line in lines:
        line = raw_line
        res = re.sub(pattern, rpl, line)
        
        res_lines.append(res)
        f_out.write(res)
        
    f_out.close()


def isMarkdown(file_name):
    '''
    test if the file is a markdown file
    '''
    pattern = r"[\d\D]*\.md$"
    if re.match(pattern, file_name) is not None:
        return True
    
    return False
    

if __name__ == "__main__":
    
    input_path = "input"
    output_path = "output"
    
    g = os.walk(input_path,"r")    
    
    # test if the input & output folder exists
    # if not, create them
    if not os.path.exists(input_path):
        os.makedirs(input_path)
        raise Exception("input 文件夹不存在") 

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        raise Exception("output 文件夹不存在")
				 	
    # start transforming 
    for path,dir_list,file_list in g:      
        for file_name in file_list:  
            if isMarkdown(file_name):# if the file is markdown file, than transform it
                transform(input_path, output_path, file_name)
                