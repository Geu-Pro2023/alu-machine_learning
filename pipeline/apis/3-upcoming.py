#!/usr/bin/env python3
"""
Fetches the next upcoming SpaceX launch and prints its details in the format:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)
"""

import requests

if __name__ == "__main__":
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch launch data")
        exit(1)

    results = response.json()

    if not results:
        print("No upcoming launches found.")
        exit(1)

    # Initialize to find the earliest launch
    upcoming_launch = None

    for launch in results:
        if upcoming_launch is None or launch['date_unix'] < upcoming_launch['date_unix']:
            upcoming_launch = launch

    if not upcoming_launch:
        print("No valid upcoming launch found.")
        exit(1)

    launch_name = upcoming_launch.get('name', 'Unknown')
    date = upcoming_launch.get('date_local', 'Unknown')
    rocket_id = upcoming_launch.get('rocket')
    launchpad_id = upcoming_launch.get('launchpad')

    # Fetch Rocket details
    rocket_name = "Unknown"
    if rocket_id:
        rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
        rocket_response = requests.get(rocket_url)
        if rocket_response.status_code == 200:
            rocket_name = rocket_response.json().get('name', 'Unknown')

    # Fetch Launchpad details
    launchpad_name = "Unknown"
    location = "Unknown"
    if launchpad_id:
        launchpad_url = "https://api.spacexdata.com/v4/launchpads/{}".format(
            launchpad_id
        )
        launchpad_response = requests.get(launchpad_url)
        if launchpad_response.status_code == 200:
            launchpad_data = launchpad_response.json()
            launchpad_name = launchpad_data.get('name', 'Unknown')
            location = launchpad_data.get('locality', 'Unknown')

    # Print launch details
    print(
        "{} ({}) {} - {} ({})".format(
            launch_name, date, rocket_name, launchpad_name, location
        )
    )
