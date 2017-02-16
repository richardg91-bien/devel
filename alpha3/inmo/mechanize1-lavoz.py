#!/usr/bin/python
#coding: utf-8


import cookielib 
import mechanize 

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
response = br.open('http://www.clasificadoslavoz.com.ar/home') 

#for form in br.forms():
#    print "Form name:", form.name
#    print form


br.form = list(br.forms())[0]
#br.select_form( name="user-login-form" ) 
br[ "name" ] = 'atpublic@hotmail.com'
br[ "pass" ] = 'qpalzm12'
br.submit() 

#print response.read()
#print cookiejar


response = br.open('http://www.clasificadoslavoz.com.ar/node/add/aviso-casa')
br.form = list(br.forms())[1]
#print br.form



parameters = {'categoria' : 'Inmuebles',
parameters = {

				'tipos-contenido' : '/node/add/aviso-casa',
				'field_aviso_tipo_unidad[value]' :  '1',
				'field_aviso_operacion[value]' :  '2',
				'field_aviso_cantidad_dormitorios[value]' :  '3',
				'title' :  'Broker21',
				'teaser_include' :  '1',
				'body' :  '<p>Broker1</p>',
				'format' :  '4',
				'field_aviso_apto_escritura[value]' :  '2',
				'field_aviso_emprendimiento[nid][nid]' :  '',
				#'taxonomy[5][hsid]' :  '0',
				'taxonomy[5][hierarchical_select][selects][0]' :  '3173',
				#br [ "op' :  'Actualizar',
				#'taxonomy[5][hierarchical_select][selects][1]' :  '3194',
				#'taxonomy[5][hierarchical_select][selects][2]' :  '5116',
				
				
				'field_aviso_tipo_barrio[value]' :  '1',
				#'field_aviso_zona=[*, 1, 2, 3, 4, 5],
				#'field_aviso_zona_turistica' :  [*, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
				'field_aviso_calle[0][value]' :  'San Jeronimo',
				'field_aviso_calle_altura[0][value]' :  '1234',
				'field_aviso_confidencial[value][1]' :  '1',
				'field_aviso_tel_vendedor[0][value]' :  '3513193581',
				'field_aviso_ocultar_tel[value][1]' :  '1',
				'field_aviso_mail_vendedor[0][value]' :  'atpublic@hotmail.com',
				'field_aviso_ocultar_mail[value][1]' :  '1',

				'field_aviso_precio[0][value]' :  '999999999',
				'field_aviso_moneda[value]' :  '2',
				#'field_aviso_ocultar_precio[value][1]' :  [1],

				'field_aviso_forma_pago[value]' :  '1'
			
			
			}


#-------------------------------------------------

br[ "tipos-contenido" ] = ['/node/add/aviso-casa',]
br[ "field_aviso_tipo_unidad[value]" ] = ['1',]
br[ "field_aviso_operacion[value]" ] = ['2',]
br[ "field_aviso_cantidad_dormitorios[value]" ] = ['3',]
br[ "title" ] = 'Broker21'
br[ "teaser_include" ] = ['1',]
br[ "body" ] = '<p>Broker1</p>'
br[ "format" ] = ['4',]
br[ "field_aviso_apto_escritura[value]" ] = ['2',]
br[ "field_aviso_emprendimiento[nid][nid]" ] = ['',]
#br[ "taxonomy[5][hsid]" ] = '0'
br[ "taxonomy[5][hierarchical_select][selects][0]" ] = ['3173',]
#br [ "op" ] = 'Actualizar'
#br[ "taxonomy[5][hierarchical_select][selects][1]" ] = ['3194',]
#br[ "taxonomy[5][hierarchical_select][selects][2]" ] = ['5116',]

 
br[ "field_aviso_tipo_barrio[value]" ] = ['1',]
#br[ "field_aviso_zona=[*, 1, 2, 3, 4, 5]
#br[ "field_aviso_zona_turistica" ] = [*, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
br[ "field_aviso_calle[0][value]" ] = 'San Jeronimo'
br[ "field_aviso_calle_altura[0][value]" ] = '1234'
br[ "field_aviso_confidencial[value][1]" ] = ['1',]
br[ "field_aviso_tel_vendedor[0][value]" ] = '3513193581'
br[ "field_aviso_ocultar_tel[value][1]" ] = ['1',]
br[ "field_aviso_mail_vendedor[0][value]" ] = 'atpublic@hotmail.com'
br[ "field_aviso_ocultar_mail[value][1]" ] = ['1',]

br[ "field_aviso_precio[0][value]" ] = '999999999'
br[ "field_aviso_moneda[value]" ] = ['2',]
#br[ "field_aviso_ocultar_precio[value][1]" ] = [1]

br[ "field_aviso_forma_pago[value]" ] = ['1',]
#br[ "field_aviso_apto_credito" ] = [*, 1, 2, 3]
#br[ "field_aviso_antiguedad[0]" ] = 
#br[ "field_aviso_estrenar[1]" ] = [1]
#br[ "field_aviso_etapa_construccion" ] = [*, 1, 2, 3]
#br[ "field_aviso_cantidad_plantas" ] = [*, 1, 2, 3, 4]
#br[ "field_aviso_cantidad_banios" ] = [*, 1, 2, 3, 4, 5]
#br[ "field_aviso_cantidad_cocheras" ] = [*, 1, 2, 3, 4, 5]
#br[ "field_aviso_cobertura_cochera" ] = [*, 1, 2, 3]
#br[ "field_aviso_superficie_total[0]" ] = 
#br[ "field_aviso_superficie_cubierta[0]" ] = 
#br[ "field_aviso_propiedad_ocupada[1]" ] = [1]
#br[ "field_aviso_video[0][embed]" ] = 


#br[ "taxonomy[34][hsid]" ] = 1) (readonly
#br[ "taxonomy[34][hierarchical_select][selects][0]" ] = [label_0, 8688, 6323, 7016, *6330, 6282, 6106, 6000, 6017]
#br[ "taxonomy[34][hierarchical_select][selects][1]" ] = [label_1, 6338, *6331, 6339, 6334, 6332, 6337, 6335, 6336, 6333]


#br[ "hs_form_build_id" ] = hs_form_2e177b2ac387595a97738bbeb4b3a868) (readonly
#br[ "changed" ] = ) (readonly
#br[ "form_build_id" ] = form-f5a686424ee25385699a3a96a95f3040) (readonly
#br[ "form_token" ] = a9ec5a4e68a612a6e49d32967450736e) (readonly
#br[ "form_id" ] = aviso_casa_node_form) (readonly
#br[ "field_aviso_mapa[0][locpick][user_latitude]" ] = 
#br[ "field_aviso_mapa[0][locpick][user_longitude]" ] = 
#br[ "field_aviso_apto_profesional" ] = [*, 1, 2]>

br.submit()
print response.read


print "Success!\n"