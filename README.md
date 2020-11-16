# ToolScripts
常用工具脚本、封装方法积累，具体使用方法见脚本中注释
#### 不定期更新中，如有疑问或建议请随时通过 Issues 联系 ^_^，感谢star鼓励或fork，谢谢！

## 功能目录
1. Superstore/superstore_process.py 美剧Superstore字幕转换为剧本
2. common/utils.py 常用函数封装模块
   - common_log 捕获异常并打印错误信息
   - pprint 高亮打印，常用于调试
   - local_logger 二次封装logger模块，提供全局日志对象生成，并保存到本地
   - get_file_enc 获取文件编码
   - change_file_enc 递归转换给定目录下的所有文件编码
   - auto_copytree 递归拷贝给定文件夹及所有文件
3. common/transfer.py 大文件切分、合并方法封装
4. professional/exchange_pyqt.py PyQt文件转换
4. interesting/pressure_gun.py 压枪脚本（鼠标键盘监控）
5. test/* 个人测试脚本

and more...
