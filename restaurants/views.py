from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	restlist= [
	{
		"restaurant_name" :"Sunny Sideup",
		"food_type" : "Breakfast"
	},
	{
		"restaurant_name" :"Dead Land",
		"food_type" : "Brains for Zombies"
	},
	{
		"restaurant_name" :"Suger Rush",
		"food_type" : "Candies and Cakes"
	}

	]
	context = {
	"my_list" : restlist
	}
	return render(request, 'list.html', context)


def restaurant_detail(request):
	dictionary ={
		"restaurant_name" :"Dead Land",
		"food_type" : "Brains for Zombies"

	}
	context = {
	"my_object" : dictionary
	}
	return render(request, 'detail.html', context)
