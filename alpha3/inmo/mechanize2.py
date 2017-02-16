#!/usr/bin/python
#coding: utf-8


import cookielib 
import mechanize 
import urllib
# Browser 
br = mechanize.Browser() 

# Enable cookie support
cookiejar = cookielib.LWPCookieJar() 

br.set_cookiejar( cookiejar ) 

# Browser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( False ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 

# Follow refresh 0 but not hangs on refresh > 0
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

# authenticate 
response = br.open('http://clasificados.cadena3.com/mis-avisos.asp') 
#print response.read()

br.select_form( name="usuarios" ) 
br[ "usuario" ] = 'Broker21'
br[ "clave" ] = 'qpalzm12'
br.submit() 

#print res.read()
#print cookiejar


parameters = {'categoria' : 'Inmuebles',
				'accion' : '',
				'codigo' : '',
				'rubro' : '1',
				'operacion' : 'V',
				'titulo' : 'titulobroker21',
				'cuerpo' : 'descripcionbroker21',
				#'provinciaid' : '7856'
				'provincia' : 'Cordoba',
				#'ciudadid' : '7923'
				'ciudad' : 'Cordoba',
				#'barrioid' : ''
				'barrio' : 'Cordoba',
				'tipobarrio' : 'Abierto',
				'calle' : 'broker21calle',
				'altura' : '1234',
				#'lat' : '',
				#'lng' : '',
				'precioentero' : '111222',
				'moneda' : '$',
				'formapago' : 'Contado',
				'aptocredito' : 'No',
				'aptoescritura' : 'No',
				'antiguedad' : '11',
				'aestrenar' : 'Si',
				'ambiente' : '11',
				'plantas' : '1',
				'banios' : '1',
				'm2terreno' : '1111',
				'm2cubiertos' : '1111',
				'pileta' : 'No',
				'cochera' : 'No',
				'habservicio' : 'No',
				'comedor' : 'No',
				'patio' : 'No'
				}

data = urllib.urlencode(parameters)
response = br.open('http://clasificados.cadena3.com/publicar-respuesta.asp', data)
print response
print "Success!\n"