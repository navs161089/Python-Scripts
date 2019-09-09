import pygeoip
import gmplot
sample_data = pygeoip.GeoIP('/home/GeoLiteCity.dat')
def ip_req(ip):
    data = sample_data.record_by_name(ip)
    long = data['longitude']
    lati = data['latitude']
    country = data['country_name']
    print('Longitude:', long)
    print('Latitude:', lati)
    print('Country:', country)
    gmap1 = gmplot.GoogleMapPlotter(36.8512,-76.1692, 13)
    gmap1.apikey = "google_api"
    gmap1.draw("/var/www/html/gmap.html")
ip = input("Enter the IP address:")
print(ip_req(ip))
