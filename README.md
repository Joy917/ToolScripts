# ToolScripts
常用工具脚本、自动化脚本、封装方法积累，具体使用见脚本中注释

## 功能目录
- Superstore/superstore_process.py 美剧Superstore字幕转换为剧本
- common/utils.py 常用工具函数封装模块
   - common_log 捕获异常并打印错误信息
   - pprint 高亮打印：常用于调试
   - local_logger 二次封装logger模块，提供全局日志对象生成，并保存到本地
   - get_file_enc 获取文件编码
   - change_file_enc 递归转换给定目录下的所有文件编码
   - auto_copytree 递归拷贝给定文件夹及所有文件
- common/transfer.py 大文件切分、合并方法封装
- common/date_utils.py 日期处理工具类
- professional/exchange_pyqt.py PyQt文件批量转换
- professional/translator.py Google机翻
- professional/excel_handle.py Excel处理
- interesting/pressure_gun.py 压枪脚本（鼠标键盘监控）
- test/* 个人测试脚本

#### 不定期更新中，如有疑问或建议请通过 Issues 联系 ^_^，欢迎MR，如果能赏一颗 Star 鼓励下就更好啦，谢谢！
