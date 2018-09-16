#!/usr/bin/env python
import web
import time

from datetime import datetime  
from datetime import timedelta  

urls = (
    '/process/*', 'serve_requests',
    '/stats', 'list_stats'
)

app = web.application(urls, globals())

service_count = 0

active_get_count = 0
active_post_count = 0
active_put_count = 0
active_delete_count = 0
get_dict = []
post_dict = []
put_dict = []
del_dict = []

class serve_requests:

    def increment(self, var):
        return var + 1

    def GET(self):
        dd = datetime.now()
        global service_count
        service_count = service_count + 1
        global active_get_count
        active_get_count = active_get_count + 1
        time.sleep(15)
        endd = datetime.now()
        #get_dict[dd] = endd

        response = {
            "time": str(dd),
            "query_type": "GET",
            "headers": "NaN",
            "path": "/process/",
            "query": "NaN",
            "body": "NaN",
            "duration": str(endd - dd)
        }
        return response

    
    def POST(self):
        dd = datetime.now()
        global service_count
        service_count = service_count + 1
        global active_get_count
        active_post_count = active_post_count + 1
        time.sleep(15)
        endd = datetime.now()
        #get_dict[dd] = endd

        response = {
            "time": str(dd),
            "query_type": "POST",
            "headers": "NaN",
            "path": "/process/",
            "query": "NaN",
            "body": "NaN",
            "duration": str(endd - dd)
        }
        return response

    
    def PUT(self):
        dd = datetime.now()
        global service_count
        service_count = service_count + 1
        active_put_count = increment(active_put_count)
        time.sleep(15)
        endd = datetime.now()
        put_dict[dd] = endd
        response = {
            time: dd,
            method: "PUT",
            headers: "NaN",
            path: "/process/",
            query: "NaN",
            body: "NaN",
            duration: endd - dd
        }
        return response

    
    def DELETE(self):
        dd = datetime.now()
        global service_count
        service_count = service_count + 1
        active_delete_count = increment(active_delete_count)
        time.sleep(15)
        endd = datetime.now()
        del_dict[dd] = endd
        response = {
            time: dd,
            method: "DELET",
            headers: "NaN",
            path: "/process/",
            query: "NaN",
            body: "NaN",
            duration: endd - dd
        }
        return response


class list_stats:
    
    def find_http_data(self, dic, hour_time, min_time, curr_time):
        hr_count = 0
        min_count = 0
        hr_avg = 0.0
        min_avg = 0.0
        for key, value in dic.iteritems():
            if value >= hour_time and value <= curr_time:
                hr_count = hr_count+1
                hr_avg = hr_avg + (value - key)

        for key, value in dic.iteritems():
            if value >= min_time and value <= curr_time:
                min_count = min_count+1
                min_avg = min_avg + (value - key)
                
        hr_avg = hr_avg/hr_count
        min_avg = min_avg/min_count

        min_data = {
            count : min_count,
            avg : min_avg
        }

        hr_data = {
            count : hr_count,
            avg : hr_avg
        }

        return  min_data, hr_data

    def GET(self):
        curr_time = datetime.now()
        min_time = curr_time - timedelta(minutes=1)
        hour_time = curr_time - timedelta(minutes=60)
        
        get_min_data, get_hr_data = find_http_data(get_dict, hour_time, min_time, curr_time)
        post_min_data, post_hr_data = find_http_data(post_dict, hour_time, min_time, curr_time)
        put_min_data, put_hr_data = find_http_data(put_dict, hour_time, min_time, curr_time)
        del_min_data, del_hr_data = find_http_data(del_dict, hour_time, min_time, curr_time)


        active_count = { get_count : active_get_count,
            post_count : active_post_count,
            put_count : active_put_count,
            delete_count : active_delete_count
        }

        http_min_data = { get_min_data : get_min_data,
        post_min_data : post_min_data,
        put_min_data : put_min_data,
        del_min_data : del_min_data
        }

        http_hr_data = { get_hr_data : get_hr_data,
        post_hr_data : post_hr_data,
        put_hr_data : put_hr_data,
        del_hr_data : del_hr_data
        }

        http_hr_data = { get_data : get_data,
        post_data : post_data,
        put_data : put_data,
        del_data : del_data
        }

        response = {
            service_count : service_count,
            active_count : active_count,
            http_min_data : http_min_data,
            http_hr_data : http_hr_data
        }
        return response


if __name__ == "__main__":
    app.run()
