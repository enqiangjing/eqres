# 全局返回工具
定义统一的 http 接口返回信息

```shell
# 安装
pip install eqres
# 升级
pip install --upgrade eqres
# 卸载
pip uninstall eqres
```
## 使用
```python
from eqres import SetResponse
res = SetResponse()

def http_api_success():
    # data 为要返回的数据信息
    data = {
        'info': '这是一个返回信息'
    }
    return res.success(data)

def http_api_res():
    # code 为指定的响应码信息
    code = 'sys_error'
    # data 为要返回的数据信息
    data = {
        'info': '这是一个返回信息'
    }
    return res.res(code, data)

def http_api_msg():
    # data 为要返回的数据信息
    data = {
        'info': '这是一个返回信息'
    }
    # msg 为自定义的返回码和信息
    msg = {
        'code': 2000,
        'message': '响应成功'
    }
    return res.msg(data, msg)
```
> 输出数据格式
```json
{
  'code': 2000,
  'message': 'success',
  'data': 'abc',
  'end_time': '2022-01-19 17:47:05.858000',
  'start_time': '2022-01-19 17:47:06.858373'
}
```