from django.db import models


class Clase(models.Model):
    """
    clase representando una clase de ave
    """
    name = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

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
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

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
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

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
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

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
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

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
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name


def directory_path_images(instance, filename):
    return '{0}/{1}/{2}/{3}/{4}/{5}'.format(instance.clase, instance.orden, instance.suborden, instance.familia, instance.genero, filename)


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
    # la imagen es un url guardado en S3, un droplet o el filesystem
    # image = models.URLField(default=None, blank=True)
    mainImage = models.ImageField(upload_to=directory_path_images)

    # coleccion de imagenes adicionales
    # otherImages = models.ManyToManyField(Image)

    # descripcion del ave
    description = models.CharField(max_length=10000)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Tira representando el model (util en /admin/)
        """
        return self.name

    def getSummaryDescription(self):
        return self.description[:300] + "..."


class Image(models.Model):
    """
    tabla/modelo que guardara las imagenes
    """
    Ave = models.ForeignKey(Ave, on_delete=models.CASCADE)
    image = models.ImageField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
