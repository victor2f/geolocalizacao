#! python
# -*- coding: utf-8 -*-
# Tratamento de geolocalizacao

import math


class Distance:

    def __init__(self):
        self.MEAN_RADIUS_OF_EARTH = 6371000  # Raio médio da Terra em metros

    def haversine(self,
                  point_1: tuple[float, float],
                  point_2: tuple[float, float]) -> float:
        """
        Calcula a distância entre dois pontos na superfície da Terra
        :param point_1: Tupla contendo latitude e longitude do ponto 1
        :param point_2: Tupla contendo latitude e longitude do ponto 2
        :return: Distância entre os dois pontos em metros
        """
        latitude_1, longitude_1 = point_1
        latitude_2, longitude_2 = point_2

        latitude_radian_1 = math.radians(latitude_1)
        longitude_radian_1 = math.radians(longitude_1)

        latitude_radian_2 = math.radians(latitude_2)
        longitude_radian_2 = math.radians(longitude_2)

        latitude_delta = latitude_radian_2 - latitude_radian_1
        longitude_delta = longitude_radian_2 - longitude_radian_1

        a = math.sin(latitude_delta / 2)**2 + math.cos(latitude_radian_1) * \
            math.cos(latitude_radian_2) * math.sin(longitude_delta / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = self.MEAN_RADIUS_OF_EARTH * c

        return distance


class DegreesMinutesSeconds:
    def __init__(self):
        pass

    def dms_to_dd(self,
                  degrees: int,
                  minutes: int,
                  seconds: float,
                  hemisphere: str) -> float:
        """
        Converte uma coordenada geográfica no formato DMS (Degrees, Minutes, Seconds) para DD (Decimal Degrees)
        :param degrees: Graus
        :param minutes: Minutos
        :param seconds: Segundos
        :param hemisphere: Hemisfério (N, S, E, W)
        :return: Coordenadas geográficas em graus decimais
        """
        decimal_value = degrees + (minutes / 60) + (seconds / 3600)

        if hemisphere in ['S', 'W']:
            decimal_value = -decimal_value

        return decimal_value


if __name__ == '__main__':

    distance = Distance()
    dms = DegreesMinutesSeconds()

    # 23°12'42.47"S 45°54'36.91"W
    # 23°12'48.71"S  45°54'38.02"W

    position_1 = (dms.dms_to_dd(23, 12, 42.47, 'S'),
                  dms.dms_to_dd(45, 54, 36.91, 'W'))

    position_2 = (dms.dms_to_dd(23, 12, 48.71, 'S'),
                  dms.dms_to_dd(45, 54, 38.02, 'W'))
    
    print(distance.haversine(position_1, position_2))
