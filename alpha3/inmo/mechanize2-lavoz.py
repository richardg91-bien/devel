#!/usr/bin/python
#coding: utf-8

import sys, logging
import urllib
import cookielib 
import mechanize



#----------------------------------
# Start the Browser 
br = mechanize.Browser() 
cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 

# Browser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( False ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 
br.set_handle_refresh( mechanize.HTTPRefreshProcessor, max_time = 1 ) 

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

br.set_debug_redirects(True)
# authenticate 
response = br.open('http://www.clasificadoslavoz.com.ar/home') 

#for form in br.forms():
#    print "Form name:", form.name
#    print form



br.form = list(br.forms())[0]
br[ "name" ] = 'atpublic@hotmail.com'
br[ "pass" ] = 'qpalzm12'
br.submit() 
#--------- END LOGIN ---------------


response = br.open('http://www.clasificadoslavoz.com.ar/node/add/aviso-casa')

br.form = list(br.forms())[1]

hs_form_build_id =  str(br [ 'hs_form_build_id' ])
form_build_id = str(br [ 'form_build_id' ])
form_token =  str(br [ 'form_token' ])
#taxonomy_5_hsid =  br [ 'taxonomy[5][hsid]' ]
#taxonomy_34_hsid =  br [ 'taxonomy[34][hsid]' ]
taxonomy_5_hsid =  str(32)
taxonomy_34_hsid =  str(33)


print "---Tokens---"
print "taxonomy[34][hsid] : " + taxonomy_34_hsid
print "taxonomy[5][hsid] : " + taxonomy_5_hsid
print "hs_form_build_id : " + hs_form_build_id
print "form_build_id    : " + form_build_id
print "form_token       : " + form_token
print "------------"


parameters = {'tipos-contenido' : '/node/add/aviso-casa',
				'field_aviso_tipo_unidad[value]' : '1',
				'field_aviso_operacion[value]' : '2',
				'field_aviso_cantidad_dormitorios[value]' : '1',
				'title' : 'Broker21',
				'teaser_include' : '1',
				'body' : '<p>Broker1</p>',
				'format' : '4',
				'field_aviso_apto_escritura[value]' : '',
				'field_aviso_emprendimiento[nid][nid]' : '',
				'taxonomy[5][hsid]' : taxonomy_5_hsid,
				'taxonomy[5][hierarchical_select][selects][0]' : '3173',
				'taxonomy[5][hierarchical_select][selects][1]' : '3194',
				'taxonomy[5][hierarchical_select][selects][2]' : '5116',
				'field_aviso_tipo_barrio[value]' : '',
				'field_aviso_zona' : '',
				'field_aviso_zona_turistica' : '',
				'field_aviso_calle[0][value]' : 'San Jeronimo',
				'field_aviso_calle_altura[0][value]' : '1234',
				'field_aviso_confidencial[value][1]' : '1',
				'field_aviso_tel_vendedor[0][value]' : '3513193111',
				'field_aviso_ocultar_tel[value][1]' : '1',
				'field_aviso_mail_vendedor[0][value]' : 'atpublic@hotmail.com',
				'field_aviso_ocultar_mail[value][1]' : '1',
				'field_aviso_precio[0][value]' : '999999999',
				'field_aviso_moneda[value]' : '1',
				'field_aviso_ocultar_precio[value][1]' : '1',
				'field_aviso_forma_pago[value]' : '1',
				'taxonomy[18][5278]' : '5278',
				#'op' : 'Siguiente >',
				'taxonomy[34][hsid]' :  taxonomy_34_hsid,
				'taxonomy[34][hierarchical_select][selects][0]' :  '6330',
				'taxonomy[34][hierarchical_select][selects][1]' :  '6331',
				'hs_form_build_id' : hs_form_build_id,
				'form_build_id' : form_build_id,
				'form_token' : form_token,
				'form_id' : 'aviso_casa_node_form'
			}
#-------------------------------------------------

 
data = urllib.urlencode(parameters)
response = br.open('http://www.clasificadoslavoz.com.ar/node/add/aviso-casa', data)


#request = br.request
#print request.header_items()
#print response.info()

print "Server Response: " + str(response.code)
print "Post Creado! - " + str(response.geturl())

print "Success!\n"