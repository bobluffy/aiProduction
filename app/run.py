# -*- coding: utf-8 -*-
"""
   File Name：     run.py
   Description :  web APIs
   Author :       yuanfang
   date：         2020/12/09
"""

import uuid
from flask import Flask, request, render_template, jsonify
import json
import traceback

from app.modules.main.core import  AIFlow
from app.modules.util.tools import logger
from app.inner_confs.constants_config import ResponseCode

from app.modules.util.error import Addr_St_Error

app = Flask(__name__)

ai_flow = AIFlow()

@app.errorhandler(404)
def error(error_no):
    return "您访问的路径不存在...,可以访问/demo"



@app.route("/smart_tager/v1.0/aiTagger", methods=["POST"])
def smart_tagger():
    """
    @api {post} /smart_tager/v1.0/aiTagger文本自动识别标签
    @apiSampleRequest http://ip:port/smart_tager/v1.0/aiTagger
    @apiVersion 1.0.0
    @apiName textFinder
    @apiGroup text
    @apiDescription
    @apiHeader {String} Content-Type application/json;charset=utf-8
    @apiParam {JsonArray} instances (必填) 查询文本数组
    @apiParam (instances) {String} id (必填) 查询唯一标识
    @apiParam (instances) {String} text (必填) 查询文本
    @apiParamExample {json} Request-Example:
    {
        "keywords":{"现金、纪念币":["like的值1","like的值2"],"现金":["like的值1","like的值2"]},
        "descriptions":{"现金、纪念币":["特征值１","特征值２"],"现金":["特征值１","特征值２"]},
        "instances":[
                        {
                         "id":"0000001",
                         "text": "上午８点门锁被撬开了mei，放桌子上的不见了"
                       },
                        {
                            "id": "0000002",
                            "text": "ada  ad"
                        }
                    ]
    }

    @apiSuccess {String} status_code 错误码 </br>
    000000 成功状态 </br>
    010001 转人工 </br>
    100001 系统异常 </br>
    @apiSuccess {String} status_info 错误信息
    @apiSuccess {String} description （业务异常则必传）错误描述
    @apiSuccess {JsonArray} results 结果
    @apiSuccess (results) {String} id原样返回
    @apiSuccess (results) {String} labels为识别后的文本的标签索引
    @apiSuccessExample Success-Example:
    {
        "status_code": "000000",
        "status_info": "成功", "log_id": "7cc33e84b16c4283bf1036aedbff40e0",
        "result": [
                    {
                        "id": "0000001",
                        "labels": "2"
                    },
                    {
                        "id": "0000002",
                        "labels": "51,23,423"
                    }
                ]
    }
    """
    log_id = str(uuid.uuid4()).replace('-', '')
    response_json = {"status_code": ResponseCode.TEXT_TAGER_SUCCESS_CODE,
                     "status_info": ResponseCode.TEXT_TAGER_SUCCESS_INFO,
                     "log_id": log_id}
    try:
        # raw_data = request.json #the java end ask to remove the key of 'instances' for a batch-task, {instances:[{},{}]} -> [{},{}]
        data_body = json.loads(request.data)
        logger.info(f" [api] Begin smart_tager log_id:{log_id}, body:{data_body}")
        results = ai_flow.main_flow(data_body)
        response_json['result'] = results
        logger.debug(f" [api] smart_tager done，log_id：{log_id}, result:{response_json}")
    except Addr_St_Error as e:
        logger.error(f" [api]smart_tager exception：{traceback.format_exc()}")
        response_json['status_code'] = ResponseCode.TEXT_TAGER_SYSTEM_ERROR_CODE
        response_json['status_info'] = e.error_info
        response_json['description'] = e.message
    except Exception as e:
        logger.error(f" [api]smart_tager Exception：{traceback.format_exc()}")
        response_json['status_code'] = ResponseCode.TEXT_TAGER_SYSTEM_ERROR_CODE
        response_json['status_info'] = ResponseCode.TEXT_TAGER_SYSTEM_ERROR_INFO
    finally:
        json_str = json.dumps(response_json, ensure_ascii=False)
        logger.info(f" [api] End smart_tager，log_id：{log_id}，response：{json_str}")
        return json_str




if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port='6661', debug=True)
