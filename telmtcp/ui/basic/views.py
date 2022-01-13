from django.shortcuts import render
from django.http import HttpResponse

from telmtcp.module.telmtcp import common as mcm
from telmtcp.module.telmtcp import constant as mcs
from telmtcp.module.glb.ret_code import *
from telmtcp.database.orm.models import *
from geopy.geocoders import Nominatim

def dashboard(request):
	data = {
		"menu_data": mcm.get_user_menu_data(),
		"menu_id": 1,
		"page_title": "Dashboard",
	}
	return render(request, 'user/dashboard.html', data)

def search_address(request):
	try:
		param = request.POST

		geolocator = Nominatim(user_agent=mcs.EMAIL_NOMINATIM_HTTP_REFERER)
		pair = "%s, %s" % (param['latitude'], param['longitude'])
		location = geolocator.reverse(pair)

		new_param = {}
		new_param['username'] = param['username']
		new_param['latitude'] = param['latitude']
		new_param['longitude'] = param['longitude']
		new_param['accuracy'] = param['accuracy']
		new_param['location'] = location._address

		obj = geolocation(**new_param)
		obj.save()

		# gmaps = googlemaps.Client(key=mcs.GOOGLE_GETLOCATION_API_KEY)
		# reverse_geocode_result = gmaps.reverse_geocode((param['latitude'], param['longitude']))
		return HttpResponse("success")
	except Exception as e:
		return HttpResponse("error")