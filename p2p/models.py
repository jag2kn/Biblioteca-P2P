#!/usr/bin/python
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
	nombre = models.CharField(max_length=512)
	nacionalidad = models.CharField(max_length=200)
	enlaces_externos = models.TextField()
	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=512)
	def __unicode__(self):
		return self.nombre

class Medio(models.Model):
	titulo = models.CharField(max_length=512)
	categoria = models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.titulo
	
class Comentario(models.Model):
	autor = models.ForeignKey(User)
	comentario = models.TextField()
	medio = models.ForeignKey(Medio)
	def __unicode__(self):
		return self.autor+" "+self.medio+" "+comentario

class PropiedadesMedio(models.Model):
	medio = models.ForeignKey(Medio)
	nombre = models.CharField(max_length=512)
	valor = models.CharField(max_length=512)
	def __unicode__(self):
		return self.medio+" "+self.nombre+" "+self.valor

	'''
		editorial
		ciudad
		año edición
		titulo
		traduccion (si/no)
		traduccion por
		idioma
		Palabras claves
		numero de paginas
		Tamanho, dimensiones
		capitulos
		volumen
		anexos
		isbn
		// revistas
		issn
		volumen numero
		
	'''

class CopiaMedio(models.Model):
	medio = models.ForeignKey(Medio)
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.usuario+" "+self.medio

class Prestamo(models.Model):
	usuario = models.ForeignKey(User)
	copia_medio = models.ForeignKey(CopiaMedio)
	def __unicode__(self):
		return self.usuario+" "+self.copia_medio

class CondicionesPrestamo(models.Model):
	copia_medio = models.ForeignKey(CopiaMedio)
	condicion = models.TextField()
	def __unicode__(self):
		return self.condicion

