from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class CrearProductoPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,5)
    
    seleccionar_product = (By.CSS_SELECTOR,"#datatable > tbody > tr")
    editar_button = (By.ID,"edit_record")
    codigo_input = (By.ID,"id_codigo")    
    nombre_input = (By.ID,"id_nombre")    
    descripcion_input = (By.ID,"id_descripcion")    
    cantidad_minima_input = (By.ID,"id_cantidad_minima")    
    precio_input = (By.ID,"id_precio")    
    guardar_button = (By.CSS_SELECTOR,"body > div > div.content-wrapper > section.content > div > div > div > div > form > div.card-footer > button")
    
    def abrir(self,url):
        self.driver.get(url)
    
    def seleccionar_producto(self):
        
     self.wait.until(EC.element_to_be_clickable(self.seleccionar_product)).click()
    
    def editar_producto(self):
        self.wait.until(EC.element_to_be_clickable(self.editar_button)).click()    
    
    def ingresar_codigo(self,codigo):        
        codigo_campo = self.wait.until(EC.element_to_be_clickable(self.codigo_input))
        codigo_campo.clear()
        codigo_campo.send_keys(codigo)
        
    def ingresar_nombre(self,nombre):        
        nombre_campo = self.wait.until(EC.element_to_be_clickable(self.nombre_input))
        nombre_campo.clear()
        nombre_campo.send_keys(nombre)
        
    def ingresar_descripcion(self,descripcion):        
        descripcion_campo = self.wait.until(EC.element_to_be_clickable(self.descripcion_input))
        descripcion_campo.clear()
        descripcion_campo.send_keys(descripcion)
        
    def ingresar_cantidad_minima(self,cantidad_minima):
        cantidad_minima_campo = self.wait.until(EC.element_to_be_clickable(self.cantidad_minima_input))
        cantidad_minima_campo.clear()
        cantidad_minima_campo.send_keys(cantidad_minima)
        
    def ingresar_precio(self,precio):
        precio_campo = self.wait.until(EC.element_to_be_clickable(self.precio_input))
        precio_campo.clear()
        precio_campo.send_keys(precio)
        
    def guardar_producto(self):
        self.wait.until(EC.element_to_be_clickable(self.guardar_button)).click()