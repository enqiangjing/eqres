from eqres import SetResponse

if __name__ == '__main__':
    res = SetResponse()
    print(res.error('error'))
    print(res.msg('abc', 'abc'))
    print(res.msg('abc', {'code': 200, 'message': 'success'}))
