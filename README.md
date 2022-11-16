

# 工具生成
目录文件夹下运行
- sudo python3 setup.py install
验证是否安装成功
- DataTools -v

使用方法，将需要处理文件放入 data/old/目录下
- 必选参数
```
--path  源文件名
    - 举例 --path NAC_客户端测试用例.xlsx
常用参数
--type 文件类型              指定处理的文件类型 暂时只支持xlsx  不传也行
--index n                   用来处理excel读取前几列数据 默认为6列 不传也行
-sc 统计有多少页数据
-ad 打印出当前文件的所有数据
-ca 统计表格中每页有多少数据
--nf 新文件名         新生成的文件目录 data/对应类型/文件名
    - 举例  --nf demo1.xlsx  新生成 文件
--fi 需要筛选的字段所在列  筛选字段
    - 举例  --fi  4 p1,p2  统计第4列包含p1,p2的元素   区分大小写
--cs sheet页下标
    - 举例   --cs 1,2,3,4 复制第1，2，3，4页用例  从0开始
--cs sheet页下标 --fi row field
    筛选指定页的数据
```
