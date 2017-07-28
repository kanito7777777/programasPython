import urllib, urllib2

try:
    for i in xrange(1, 1001):
        #parametros post
        txtCuenta = 'hack' + str(i)
        txtClave = 'hack' + str(i)
        txtNombre = 'protege'
        txtDesc = 'tu aplicacion'
        
        parametros = urllib.urlencode({"txtCuenta":txtCuenta, 
                                       "txtClave":txtClave, 
                                       "txtNombre":txtNombre, 
                                       "txtDesc":txtDesc})
        peticion = urllib2.urlopen("http://localhost/muna/nuevoController.php?%s", parametros)
        
        print peticion.read()
        peticion.close()
    
except HTTPError, e:
    print "Ocurrio un Error"
    print e.code
except URLError, e:
    print "Ocurrio un error"
    print e.reason
