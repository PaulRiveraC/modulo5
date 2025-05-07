from libro import Libro

libro_musica=Libro(titulo="Fur Elisse", autor="Ludwing Van Bethoven", paginas=200)
libro_terror=Libro(titulo="IT", autor="Stephen King", paginas=400)
libro_ciencia=Libro(titulo="Teoría de la relatividad", autor="Albert Eintein", paginas=700)

Libro.libros.append(libro_musica)
Libro.libros.append(libro_terror)
Libro.libros.append(libro_ciencia)

print("**MOSTRAR INFORMACION**")
libro_musica.mostrar_info()
libro_terror.mostrar_info()
libro_ciencia.mostrar_info()
print("**TAMAÑO**")
tamanio=libro_ciencia.es_grande(libro_terror.paginas)
print(f"{tamanio}")
print("**TOTAL LIBROS**")
total=libro_ciencia.total_libros()
print(f"{total}")