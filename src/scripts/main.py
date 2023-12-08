import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__)) # Directorio del script actual
project_dir = os.path.abspath(os.path.join(script_dir, '../..')) # Directorio del proyecto
sys.path.insert(0, project_dir)

from src.modules.util import configuraciones_ldap  # Asegúrate de que el path sea correcto
from src.modules.LDAPManager import LDAPManager  # Asegúrate de que el path sea correcto

if __name__ == '__main__':
    configuracion_ldap = configuraciones_ldap(project_dir) # Obtiene la configuración del archivo de configuración
    LDAPManager = LDAPManager(configuracion_ldap['ldap_server'],
                              configuracion_ldap['ldap_port'],
                              configuracion_ldap['ldap_base_dn'],
                              configuracion_ldap['ldap_user'],
                              configuracion_ldap['ldap_password']) # Crea un objeto LDAPManager
    if(LDAPManager.bind()): # Realiza la conexión al servidor LDAP 
        print('Conexión exitosa')
        # Aquí puedes realizar operaciones adicionales en el servidor LDAP
        LDAPManager.unbind()