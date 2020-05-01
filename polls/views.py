from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def prueba(response):
	doc = open("C:/Users/pablo/Desktop/calculator/mysite/html/index.html")
	plt = Template(doc.read())
	doc.close()
	ctx = Context({})
	response = plt.render(ctx)
	return HttpResponse(response)

def search(response):
	pn = float(response.GET["pn"])
	marketcap = float(response.GET["mc"])
	years = int(response.GET["years"])
	roe = float(response.GET["roe"])

	discount = pn/marketcap
	valor = (100 * discount) * (1 + roe)**years
	valor = round(valor,2)

	return HttpResponse(f"If you invest 100$ the value of the company after {years} years will be {valor}, sme equity = {valor*(1/discount)}")

