 ## 1. flask起服务器
 ### 1.1 服务搭建
    from flask import Flask, jsonify, request
    from flask_restful import Api, Resource, reqparse, abort

    app = Flask(__name__)
    api = Api(app)

    # 获取json
    def parse_images(name='image'):
        args = request.get_json()

    # 定义响应函数
    class IdcardPhotoClassify(Resource):
        @staticmethod
        def post():
            ...
            except Exception as e:
                traceback.print_exc()
                ret['message'] = str(e)
            finally:
                return jsonify(ret)
    # 绑定
    api.add_resource(IdcardPhotoClassify, '/img_idcard_photo_classify', '/img/idcard_photo_classify')

    if __name__ == '__main__':
        port = 25610
        app.run(debug=False, host='0.0.0.0', port=port)
### 1.2 测试
    import requests,json
    # 将python对象转成字符串
    data_json = json.dumps({'images':[data_s, data_s, data_s]})   
    # 变成json
    data_json=json.loads(data_json)
    # post形式发送
    r_json = requests.post(url,json = data_json)
