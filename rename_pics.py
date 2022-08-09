import datetime
import os.path, os

folder_path = '/Volumes/My passport/Fotos/2018-02'

os.chdir(folder_path)

if __name__ == '__main__':
    # Contador para fotos repetidas
    contador = 0
    # Recorremos los archivos del directorio
    for file_name in os.listdir(folder_path):
        # Separamos nombre y extension del archivo
        name, extension = os.path.splitext(file_name)
        # Evaluamos la extension para trabajar con los archivos necesarios
        if extension in ['.jpg', '.jpeg', '.png', '.mp4', '.MP4']:
            # Evaluamos que la longitud del nombre del archivo sea menor que 8 
            if len(name) < 8:
                # Extraemos la fecha de creacion del archivo y la almacenamos con formato YYYY-MM-DD HH/MM/SS
                date_image = datetime.datetime.fromtimestamp(os.path.getctime(file_name))
                # Verificamos si el nombre ya existe de ser asi aumentamos un contador en 1 y lo agregamos al final
                if os.path.exists(f'{date_image}{extension}'):
                    contador += 1
                    os.rename(name+extension, f'{date_image}_{contador}{extension}') 
                else:
                    os.rename(name+extension, f'{date_image}{extension}') 
                    contador = 0

            
            