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
response = br.open('http://clasificados.cadena3.com/mis-avisos.asp') 
#print response.read()

br.select_form( name="usuarios" ) 
br[ "usuario" ] = 'Broker21'
br[ "clave" ] = 'qpalzm12'
br.submit() 

#print res.read()
#print cookiejar


response = br.open('http://clasificados.cadena3.com/publicar.asp?categoria=Inmuebles&accion=&codigo=&rubro=1')


br.select_form( name="frmForm" ) 

print br.form.get_value('provincia')
print br.form.get_value_by_label('provincia')

#br.form.set_all_readonly(False)

#br.form.find_control('provinciaid').readonly = False

#br[ "categoria" ] = 'Inmuebles'
#br[ "rubro" ] = '1'
#br[ "accion" ] = ''
#br[ "codigo" ] = ''
br[ "operacion" ] = ['V',]
br[ "titulo" ] = 'titulobroker21'
br[ "cuerpo" ] = 'descripcionbroker21'

#br[ "provinciaid" ] = '7856'
br[ "provincia" ] = ['Seleccionar',]

#br[ "ciudadid" ] = '7923'
br[ "ciudad" ] = ['',]

#br[ "barrioid" ] = ''
br[ "barrio" ] = ['',]

br[ "tipobarrio" ] = ['Abierto',]
br[ "calle" ] = 'broker21calle'
br[ "altura" ] = '1234'
#br[ "lat" ] = ''
#br[ "lng" ] = ''
br[ "precioentero" ] = '111222'
br[ "moneda" ] = ['$',]
br[ "formapago" ] = ['Contado',]
br[ "aptocredito" ] = ['No',]
br[ "aptoescritura" ] = ['No',]
br[ "antiguedad" ] = ['11',]
br[ "aestrenar" ] = ['Si',]
br[ "ambiente" ] = ['11',]
br[ "plantas" ] = ['1']
br[ "banios" ] = ['1',]
br[ "m2terreno" ] = '1111'
br[ "m2cubiertos" ] = '1111'
br[ "pileta" ] = ['No',]
br[ "cochera" ] = ['No',]
br[ "habservicio" ] = ['No',]
br[ "comedor" ] = ['No',]
br[ "patio" ] = ['No',]
br.submit()


print "Success!\n"