# coding: utf-8

"""
    weather.gov API

    weather.gov API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alerts_active_area_area_get(self):
        """Test case for alerts_active_area_area_get

        """
        pass

    def test_alerts_active_count_get(self):
        """Test case for alerts_active_count_get

        """
        pass

    def test_alerts_active_get(self):
        """Test case for alerts_active_get

        """
        pass

    def test_alerts_active_region_region_get(self):
        """Test case for alerts_active_region_region_get

        """
        pass

    def test_alerts_active_zone_zone_id_get(self):
        """Test case for alerts_active_zone_zone_id_get

        """
        pass

    def test_alerts_get(self):
        """Test case for alerts_get

        """
        pass

    def test_alerts_id_get(self):
        """Test case for alerts_id_get

        """
        pass

    def test_alerts_types_get(self):
        """Test case for alerts_types_get

        """
        pass

    def test_glossary_get(self):
        """Test case for glossary_get

        """
        pass

    def test_gridpoints_wfo_xy_forecast_get(self):
        """Test case for gridpoints_wfo_xy_forecast_get

        """
        pass

    def test_gridpoints_wfo_xy_forecast_hourly_get(self):
        """Test case for gridpoints_wfo_xy_forecast_hourly_get

        """
        pass

    def test_gridpoints_wfo_xy_get(self):
        """Test case for gridpoints_wfo_xy_get

        """
        pass

    def test_gridpoints_wfo_xy_stations_get(self):
        """Test case for gridpoints_wfo_xy_stations_get

        """
        pass

    def test_icons_get(self):
        """Test case for icons_get

        """
        pass

    def test_icons_set_time_of_day_first_second_get(self):
        """Test case for icons_set_time_of_day_first_second_get

        """
        pass

    def test_offices_office_id_get(self):
        """Test case for offices_office_id_get

        """
        pass

    def test_offices_office_id_headlines_get(self):
        """Test case for offices_office_id_headlines_get

        """
        pass

    def test_offices_office_id_headlines_headline_id_get(self):
        """Test case for offices_office_id_headlines_headline_id_get

        """
        pass

    def test_points_point_forecast_get(self):
        """Test case for points_point_forecast_get

        """
        pass

    def test_points_point_forecast_hourly_get(self):
        """Test case for points_point_forecast_hourly_get

        """
        pass

    def test_points_point_get(self):
        """Test case for points_point_get

        """
        pass

    def test_points_point_stations_get(self):
        """Test case for points_point_stations_get

        """
        pass

    def test_products_get(self):
        """Test case for products_get

        """
        pass

    def test_products_locations_get(self):
        """Test case for products_locations_get

        """
        pass

    def test_products_locations_location_id_types_get(self):
        """Test case for products_locations_location_id_types_get

        """
        pass

    def test_products_product_id_get(self):
        """Test case for products_product_id_get

        """
        pass

    def test_products_types_get(self):
        """Test case for products_types_get

        """
        pass

    def test_products_types_type_id_get(self):
        """Test case for products_types_type_id_get

        """
        pass

    def test_products_types_type_id_locations_get(self):
        """Test case for products_types_type_id_locations_get

        """
        pass

    def test_products_types_type_id_locations_location_id_get(self):
        """Test case for products_types_type_id_locations_location_id_get

        """
        pass

    def test_radar_profilers_station_id_get(self):
        """Test case for radar_profilers_station_id_get

        """
        pass

    def test_radar_queues_host_get(self):
        """Test case for radar_queues_host_get

        """
        pass

    def test_radar_servers_get(self):
        """Test case for radar_servers_get

        """
        pass

    def test_radar_servers_id_get(self):
        """Test case for radar_servers_id_get

        """
        pass

    def test_radar_stations_get(self):
        """Test case for radar_stations_get

        """
        pass

    def test_radar_stations_station_id_alarms_get(self):
        """Test case for radar_stations_station_id_alarms_get

        """
        pass

    def test_radar_stations_station_id_get(self):
        """Test case for radar_stations_station_id_get

        """
        pass

    def test_stations_get(self):
        """Test case for stations_get

        """
        pass

    def test_stations_station_id_get(self):
        """Test case for stations_station_id_get

        """
        pass

    def test_stations_station_id_observations_current_get(self):
        """Test case for stations_station_id_observations_current_get

        """
        pass

    def test_stations_station_id_observations_get(self):
        """Test case for stations_station_id_observations_get

        """
        pass

    def test_stations_station_id_observations_latest_get(self):
        """Test case for stations_station_id_observations_latest_get

        """
        pass

    def test_stations_station_id_observations_time_get(self):
        """Test case for stations_station_id_observations_time_get

        """
        pass

    def test_thumbnails_satellite_area_get(self):
        """Test case for thumbnails_satellite_area_get

        """
        pass

    def test_zones_forecast_zone_id_observations_get(self):
        """Test case for zones_forecast_zone_id_observations_get

        """
        pass

    def test_zones_forecast_zone_id_stations_get(self):
        """Test case for zones_forecast_zone_id_stations_get

        """
        pass

    def test_zones_get(self):
        """Test case for zones_get

        """
        pass

    def test_zones_type_get(self):
        """Test case for zones_type_get

        """
        pass

    def test_zones_type_zone_id_forecast_get(self):
        """Test case for zones_type_zone_id_forecast_get

        """
        pass

    def test_zones_type_zone_id_get(self):
        """Test case for zones_type_zone_id_get

        """
        pass


if __name__ == '__main__':
    unittest.main()