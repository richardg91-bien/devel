#!/usr/bin/python
#coding: utf-8


import urllib
import cookielib 
import mechanize 
import requests
import urllib2
from BeautifulSoup import BeautifulSoup 
#import cv2.cv as cv 
#import tesseract 

 
 
class PrettifyHandler(mechanize.BaseHandler): 
    def http_response(self, request, response): 
        if not hasattr(response, "seek"): 
            response = mechanize.response_seek_wrapper(response) 
         # only use BeautifulSoup if response is html 
        if response.info().dict.has_key('content-type') and ('html' in response.info().dict['content-type']): 
            soup = BeautifulSoup(response.get_data()) 
            response.set_data(soup.prettify()) 
        return response 



#----------------------------------
# Browser 
br = mechanize.Browser(factory=mechanize.RobustFactory())
br.add_handler(PrettifyHandler())

cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 


# Browser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( False ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

# Set Headers
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 


parameters = {	'a' : 'l',
				'usuario' : 'broker21',
				'pass' : 'qpalzm12',
				'ingresar' : 'Enviar'
			}

# authenticate 
data = urllib.urlencode(parameters)
response = br.open('http://www.cordobavende.com/do.php?action=login', data) 
print 'Logged in!\n'

# ---- seccion de posteo ----

parameters = { 'id_prod' : '0',
				'id_eshop' : '0',
				'categoria' : '38',
				'subcategoria' : '185',
				'subcategoria2' : '1555',
				'Submit' : 'Siguiente'
			}

data = urllib.urlencode(parameters)

response = br.open('http://www.cordobavende.com/tmp_panel.php?content=carga-paso2-mp', data)

#print response.geturl()

br.form = list(br.forms())[3]

id_prod =  str(br [ 'id_prod' ])


#gray = cv.LoadImage('captcha.jpeg', cv.CV_LOAD_IMAGE_GRAYSCALE) 
#cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY) 
#api = tesseract.TessBaseAPI() 
#api.Init(".","eng",tesseract.OEM_DEFAULT) 
#api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz") 
#api.SetPageSegMode(tesseract.PSM_SINGLE_WORD) 
#tesseract.SetCvImage(gray,api) 
#print api.GetUTF8Text() 


print "---Tokens---"
print "id_prod : " + id_prod

print response.get_data().find('s3.amazonaws.com/brandcaptcha-st1/captchas/')

#--------- END LOGIN ---------------



parameters = {	'id_prod' : id_prod,
				'a' : 'p',
				'precarga' : '0',
				'error_captcha' : '0',
				'producto' : 'tester',
				'moneda' : '$',
				'pesos' : '111',
				'tipo' : 'Nuevo',
				'especial' : 'inmuebles',
				'direccion_m' : 'cordoba',
				'lat' : '0',
				'lng' : '0',
				'provincias' : '0',
				'localidad' : '0',
				'localidad2' : '',
				'barrio' : '',
				'direccion' : '',
				'antiguedad' : '',
				'metros_cubiertos' : '',
				'superficie_total' : '',
				'tipo_campo' : '',
				'tipo_comercio' : '',
				'disposicion_lote' : '',
				'vialidad_acceso' : '',
				'hectarea' : '',
				'ambientes' : '',
				'banios' : '',
				'lugar' : '',
				'orientacion' : '',
				'dormitorios' : '',
				'garages' : '',
				'edificacion' : '',
				'tipodescripcion' : '0',
				'titulo_principiante' : '',
				'descripcion_principiante' : '',
				'precio_principiante' : '',
				'descripcion' : '',
				'telefono-contacto' : '',
				'mail-contacto' : '',
				'horario-contacto' : '',
				'keywords' : '',
				'dias_publicacion_id' : '8',
				'brand_cap_answer' : 'RBRRA',
				'brand_cap_challenge' : '58780346c758ea4c0e8b45d7',
			}

data = urllib.urlencode(parameters)
response = br.open('http://www.cordobavende.com/tmp_panel.php?content=carga-paso2-mp', data) 

#print response.geturl()
			
print "Success!\n"