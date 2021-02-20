from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pymongo import MongoClient
from bson.json_util import dumps, loads

def db_connect():
    client = MongoClient("jersey.optonline.net", 27017)
    mydatabase = client.inventory  # Connect to DataBase
    thecollection = mydatabase.servers  # Connecting to the Collection
    return thecollection


def server_info(request):
    mycollection = db_connect()
    cursor = mycollection.find()  # Getting all the entries from the Collection
    list_cur = list(cursor)
    json_data = dumps(list_cur, indent=2)
    return Response(json_data)


def hp_info(request):
    mycollection = db_connect()
    cursor = mycollection.find({'make': 'HP'})  # Getting all the entries from the Collection
    list_cur = list(cursor)
    json_data = dumps(list_cur, indent=2)
    return Response(json_data)


def mac_servers(request):
    mycollection = db_connect()
    cursor = mycollection.find({'make': 'Apple MacBook'})  # Getting all the entries from the Collection
    list_cur = list(cursor)
    json_data = dumps(list_cur, indent=2)
    return Response(json_data)


def dell_servers(request):
    mycollection = db_connect()
    cursor = mycollection.find({'make': 'Dell'})  # Getting all the entries from the Collection
    list_cur = list(cursor)
    json_data = dumps(list_cur, indent=2)
    return Response(json_data)


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('servers', '/')
        config.add_route('hpservers', '/hp')
        config.add_route('macbook', '/macbook')
        config.add_route('dellservers', '/dell')
        config.add_view(server_info, route_name='servers')
        config.add_view(hp_info, route_name='hpservers')
        config.add_view(mac_servers, route_name='macbook')
        config.add_view(dell_servers, route_name='dellservers')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()