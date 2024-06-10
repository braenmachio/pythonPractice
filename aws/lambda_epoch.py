import json, boto3
from boto3.dynamodb.conditions import Attr, Key
import datetime, pytz
from datetime import datetime
from distance_calculation import calculate_distance

dynamodb = boto3.resource('dynamodb')
"""
The table contains data that is valid for 24 hours
The timestamp from devices are received in epoch format
"""
device_table = dynamodb.Table('epoch_ttl_test_table_for_devicedate')
vehicle_device = dynamodb.Table('vehicleDeviceRegistrationTable')

def lambda_handler(event, context):
    # list the devices we have in the table
    device_list = [unique_id['deviceId'] for unique_id in device_table.scan()['Items']]
    regnum_list = [reg_num['vehicle_device'] for reg_num in vehicle_device.scan()['Items']]

    for device_id, reg_num in zip(device_list, regnum_list):
        vehicle_reg_number = reg_num


def create_item(device_id: str, vehicle_reg_number: str, table: str, t_dist: str):
    table.put_item(
        Item={
            'deviceId': device_id,
            'vehicle_device': vehicle_reg_number,
            'totalDistanceCovered': t_dist,
            'coordinates': {},
            'dailyDistances': [], # make use of the updated list
            
        }
    )

def distance_calculation(device_id: str):
    device_data = device_table.scan(FilterExpression=Attr('deviceId').contains(device_id))
    recordsList = []
    for device_data in device_data['Items']:
        coordinates_string  = device_data['coordinates']
        try:
            latitude, longitude = coordinates_string.split(',')
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            print(f"Error parsing coordinates for device {item['device_id']} : {coordinates_string}")
            continue
        recordsList.append((latitude, longitude))