from django.db import models


class Clase(models.Model):
    """
    clase representando una clase de ave
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


class Orden(models.Model):
    """
    clase representando un orden (debajo de clase)
    """
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


class Suborden(models.Model):
    """
    clase representando un suborden (debajo de orden)
    """
    orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


class Familia(models.Model):
    """
    clase representando una familia (debajo de suborden)
    """
    suborden = models.ForeignKey(Suborden, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


class Genero(models.Model):
    """
    clase representando un genero (debajo de familia)
    """
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


class Especie(models.Model):
    """
    clase representando el nombre de la especie cientifico, se utilizara
    tambien en la clase de el animal
    """
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


class Image(models.Model):
    """
    tabla/modelo que guardara las imagenes
    """
    image = models.URLField()


class Ave(models.Model):
    """
    clase que representa al animal, el modelo actual usa redondancia para la
    clasificacion, es necesario para introducir los datos en /admin/
    """

    clase = models.ForeignKey(Clase, on_delete=models.PROTECT)
    orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    suborden = models.ForeignKey(Suborden, on_delete=models.PROTECT)
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    # nombre comun
    name = models.CharField(max_length=100)
    # la imagen es un url guardado en S3 o un droplet
    image = models.URLField(default=None, blank=True)
    # coleccion de imagenes adicionales
    otherImages = models.ManyToManyField(Image)
    # descripcion del ave
    description = models.CharField(max_length=10000)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name
