import json


def sum_up_distance(data: int) -> int:
    """
    The function takes a json payload and sums up the total distance 
    travelled since the data was saved

    Args:
        data (int): A json payload containing vehicle information
        totalDistanceCovered - this is the odometer reading

    Returns:
        int: The sum of the total_distance_covered and the sum of distances
        travelled each day.
    """

    total_distance = int(data["totalDistanceCovered"]) # convert str to integer
    for days_payload in data["dailyDistances"]:
        total_distance += int(days_payload["distance"])
    return total_distance

# sample implementation
data = json.loads(
    """
{
  "id": "1",
  "regNumber": "KBM 124J",
  "totalDistanceCovered": "1000",
  "location": {
    "lat": -0.719234,
    "lng": 36.436410
  },
  "dailyDistances": [
    { "distance": "200", "date": "2024-03-25" },
    { "distance": "150", "date": "2024-03-26" },
    { "distance": "80", "date": "2024-03-27" },
    { "distance": "120", "date": "2024-03-28" },
    { "distance": "50", "date": "2024-03-29" },
    { "distance": "150", "date": "2024-03-29" }
  ]
}
    """
)

# print(data)
total_distance_travelled = sum_up_distance(data)
print(f"{total_distance_travelled}")