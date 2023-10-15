from django.shortcuts import render
from django.http import HttpResponse
from conversionesApp.models import Simulation
import datetime

# Create your views here.

#Renderizar la plantilla de listado de simulaciones. 
def simulationData(request):
    simulations = Simulation.objects.all()
    data = {'simulations': simulations}
    return render(request,'conversionesApp/listado-consultas.html',data)

# Renderizar la plantilla conversiones
def crearSimulacionForm(request):
    return render(request, 'conversionesapp/simular-conversion.html')

#_________________________________________________CÁLCULOS ______________________________________________
#Calcular el total del pedido en USD
def calculateTotalAmountUSD(p_unitsAmount, p_unitPriceUSD):
    totalAmountUSD = float(p_unitsAmount)*float(p_unitPriceUSD)
    return totalAmountUSD

#Calcular impuesto de Aduana USD (custom)
def calculateCIF(p_usdShippingPrice, totalAmountUSD):
    usdCIF = float(p_usdShippingPrice) + float(totalAmountUSD)
    return usdCIF

#Calcular el impuesto de aduana correspondiente al 6% sobre el CIF
def calculateCustomUSD(CIF):
    customUSD = float(CIF)* 0.06
    return customUSD

#Calcular el impuesto al valor agregado correspondiente al 19% sobre CIF
def calculateIVA(CIF):
    ivaUSD = float(CIF)*0.19
    return ivaUSD

#Calcular el valor total de impuestos
def calculateTotalTaxes(customUSD, ivaUSD):
    totalTaxesUSD = float(customUSD)+float(ivaUSD)
    return totalTaxesUSD

#Calcular el costo total de la compra (Pedido + Envío + Impuestos) USD
def calculateTotalPurchase(totalTaxes, totalAmount):
    totalPurchase = float(totalTaxes) + float(totalAmount)
    return totalPurchase

#Transformar de USD a CLP
def usd_to_clp(usd_amount):
    clp_rate = 890  # Tasa de cambio de USD a CLP
    usd_amount = float(clp_rate) * float(usd_amount)
    return usd_amount

def displayActualSimulation(request):
    #Capturar los datos desde el formulario
    p_unitsAmount = request.POST['txt_unitsAmount']
    p_unitPriceUSD = request.POST['txt_usdUnitPrice']
    p_unitName = request.POST['txt_unitName']
    p_unitCode = request.POST['txt_unitCode']
    p_supplierName = request.POST['txt_supplierName']
    p_usdShippingPrice = request.POST['txt_usdShippingPrice']

    #Capturar la fecha y hora de ingreso:
    dt=datetime.datetime.now()
    actualDate = dt.strftime("%d-%m-%Y")
    actualTime = dt.strftime("%H:%M:%S")

    #Efectuamos los cálculos llamando las funciones creadas anteriormente:
    totalAmountsCLP = usd_to_clp(calculateTotalAmountUSD(p_unitsAmount,p_unitPriceUSD))
    shippingPriceCLP = usd_to_clp(p_usdShippingPrice)
    clpCIF= (calculateCIF(shippingPriceCLP, totalAmountsCLP))
    customCLP = round(calculateCustomUSD(clpCIF),2)
    ivaCLP = round(calculateIVA(clpCIF),2)
    totalTaxes = round(calculateTotalTaxes(customCLP, ivaCLP),2)
    totalPurchaseCLP = round(calculateTotalPurchase(clpCIF, totalTaxes))
    totalPurchaseUSD = round((totalPurchaseCLP/890),2)

    #Creamos un objeto de la clase Simulation
    simulation = Simulation(
        unitName = p_unitName,
        unitCode = p_unitCode,
        supplierName = p_supplierName,
        unitAmount = p_unitsAmount,
        totalAmountCLP = totalAmountsCLP,
        shippingCLP = shippingPriceCLP,
        customCLP = customCLP,
        ivaCLP = ivaCLP,
        totalTaxesCLP = totalTaxes,
        totalPurchaseCLP = totalPurchaseCLP,
        totalPurchaseUSD= totalPurchaseUSD,
        date = actualDate,
        time =actualTime
    )
    # Efectuamos el registro de la nueva simulación
    simulation.save()
    #Renderizar la plantilla de listado de simulaciones. 
    simulations = Simulation.objects.all()
    data = {'simulations': simulations,
            "totalAmount": totalAmountsCLP,
            "name": p_unitName,
            "unitsAmount":p_unitsAmount,
            "unitCode": p_unitCode,
            "shippingPrice":shippingPriceCLP,
            "CIF":clpCIF,
            "supplier": p_supplierName,
            "customCLP": customCLP,
            "ivaCLP":ivaCLP,
            "totalTaxes": totalTaxes,
            "totalPurchase": totalPurchaseUSD,
            "totalPurchaseCLP": totalPurchaseCLP,
            "date":actualDate,
            "time": actualTime
            }
    
    return render(request, 'conversionesapp/ultima-consulta.html', data)

