import os
from configparser import ConfigParser

def configuraciones_ldap(project_dir):
    """
    Carga la configuración desde un archivo config.ini y devuelve un diccionario con los valores de configuración.

    Args:
        project_dir (str): Ruta del directorio del proyecto.

    Returns:
        dict: Diccionario con los valores de configuración.
            - ldap_server (str): Servidor LDAP.
            - ldap_port (int): Puerto LDAP.
            - ldap_user (str): Usuario LDAP.
            - ldap_password (str): Contraseña LDAP.
            - ldap_base_dn (str): Base DN LDAP.

        None: Si ocurre un error al leer la configuración o si el archivo config.ini no existe.
    """
    config_path = os.path.join(project_dir, 'config.ini') # Ruta completa al archivo config.ini
    if not os.path.exists(config_path):
        print(f"Error: No se encontró el archivo {config_path}") # Si no existe, mostrar el error
        return None

    # Crear un objeto ConfigParser y leer la configuración desde el archivo
    config = ConfigParser()
    config.read(config_path) # Leer la configuración desde el archivo

    # Acceder a las secciones y opciones necesarias
    try:
        return {
            'ldap_server': config.get('LDAP', 'Server'),
            'ldap_port': config.getint('LDAP', 'Port'),
            'ldap_user': config.get('LDAP', 'User'),
            'ldap_password': config.get('LDAP', 'Password'),
            'ldap_base_dn': config.get('LDAP', 'base_dn')
        }
    except Exception as e:
        print(f"Error al leer la configuración: {e}") # Si hay un error, mostrarlo
        return None