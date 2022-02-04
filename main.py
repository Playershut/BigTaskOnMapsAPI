import sys

from libr.geocoder import get_coordinates
from libr.mapapi_PG import show_map


def main():
    toponym_to_find = ' '.join(sys.argv[1:])
    if toponym_to_find:
        lat, lon = get_coordinates(toponym_to_find)
        ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
        show_map(ll_spn, 'map')


if __name__ == '__main__':
    main()
