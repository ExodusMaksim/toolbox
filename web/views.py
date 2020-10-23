from django.shortcuts import render
import requests
import pandas as pd
from sqlalchemy import create_engine
from pandas import DataFrame
# Create your views here.


def toolbox_page(request):
    """
    返回基础页面
    @param request:
    """
    return render(request, "toolbox.html")


def query_req(request):
    connect_info = r'mysql+pymysql://msad_test3_ro:gpVeL2OTvFaeQT3s@172.16.129.148:3306' \
                   r'/msad_gr_notice_00?charset=utf8'
    engine = create_engine(connect_info)  # use sqlalchemy to build link-engine

    sql = "SELECT * FROM sms_message_content order by id desc limit 0,10 "  # SQL query
    return None