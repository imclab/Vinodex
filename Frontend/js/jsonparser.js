window.init = function () {
	"use strict";
	function buildList(data, isSub) {
		var html = (isSub) ? "<div>" : ""; // wrap with div if true
		html += "<ul>";
		for (var item in data) {
			if(data.hasOwnProperty(item)) {
				if (typeof (data[item]) === "object") { // array will return "object"
					html += "<li class=\"expand\"><span>" + item + "</span> {" + buildList(data[item], false) + "}"; // submenu exists, call recursively, no wrapping div
				} else {
					html += "<li><span>" + item + " : " + data[item] + "</span>"; // no submenu
				}
				html += "</li>";
			}
		}
		html += "</ul>";
		html += (isSub) ? "</div>" : "";
		return html;
	}

	var json = {
		"Status": {
			"Messages": [],
			"ReturnCode": 0
		},
		"Products": {
			"List": [{
					"Id": 95156,
					"Name": "Louis Roederer Cristal Brut 2002",
					"Url": "http:\/\/www.wine.com\/V6\/Louis-Roederer-Cristal-Brut-2002\/wine\/95156\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "95156m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/95156m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 142,
						"Name": "Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Vintage\/wine\/list.aspx?N=7155+123+142",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8079,
						"Name": "Louis Roederer",
						"Url": "http:\/\/www.wine.com\/v6\/Louis-Roederer\/learnabout.aspx?winery=988",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/988.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=988"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Louis-Roederer-Cristal-Brut-2002\/wine\/95156\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Louis-Roederer-Cristal-Brut-2002\/wine\/95156\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=988"
					},
					"PriceMax": 199.9900,
					"PriceMin": 199.9900,
					"PriceRetail": 289.0000,
					"ProductAttributes": [{
							"Id": 36,
							"Name": "Collectible Wines",
							"Url": "http:\/\/www.wine.com\/v6\/Collectible-Wines\/wine\/list.aspx?N=7155+36",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_collectable_big.gif"
						}, {
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 15419,
							"Name": "Great Bottles to Give",
							"Url": "http:\/\/www.wine.com\/v6\/Great-Bottles-to-Give\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}
					],
					"Ratings": {
						"HighestScore": 100,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 528,
					"Name": "Veuve Clicquot Brut Yellow Label",
					"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-Brut-Yellow-Label\/wine\/528\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "528m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/528m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 182,
						"Name": "Non-Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Non-Vintage\/wine\/list.aspx?N=7155+123+182",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8871,
						"Name": "Veuve Clicquot",
						"Url": "http:\/\/www.wine.com\/v6\/Veuve-Clicquot\/learnabout.aspx?winery=106",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/106.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=106"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-Brut-Yellow-Label\/wine\/528\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-Brut-Yellow-Label\/wine\/528\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=106"
					},
					"PriceMax": 52.9900,
					"PriceMin": 35.9900,
					"PriceRetail": 49.9900,
					"ProductAttributes": [{
							"Id": 0,
							"Name": "For Her",
							"Url": "",
							"ImageUrl": ""
						}
					],
					"Ratings": {
						"HighestScore": 92,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 114639,
					"Name": "Dom Perignon  2003",
					"Url": "http:\/\/www.wine.com\/V6\/Dom-Perignon-2003\/wine\/114639\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "114639m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/114639m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 142,
						"Name": "Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Vintage\/wine\/list.aspx?N=7155+123+142",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8757,
						"Name": "Dom Perignon",
						"Url": "http:\/\/www.wine.com\/v6\/Dom-Perignon\/learnabout.aspx?winery=100",
						"ImageUrl": "",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=100"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Dom-Perignon-2003\/wine\/114639\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Dom-Perignon-2003\/wine\/114639\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=100"
					},
					"PriceMax": 165.0000,
					"PriceMin": 159.9900,
					"PriceRetail": 159.9900,
					"ProductAttributes": [{
							"Id": 36,
							"Name": "Collectible Wines",
							"Url": "http:\/\/www.wine.com\/v6\/Collectible-Wines\/wine\/list.aspx?N=7155+36",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_collectable_big.gif"
						}, {
							"Id": 0,
							"Name": "Corporate Gifts",
							"Url": "",
							"ImageUrl": ""
						}, {
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 15419,
							"Name": "Great Bottles to Give",
							"Url": "http:\/\/www.wine.com\/v6\/Great-Bottles-to-Give\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}
					],
					"Ratings": {
						"HighestScore": 94,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 513,
					"Name": "Bollinger Brut Special Cuvee",
					"Url": "http:\/\/www.wine.com\/V6\/Bollinger-Brut-Special-Cuvee\/wine\/513\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "513m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/513m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 182,
						"Name": "Non-Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Non-Vintage\/wine\/list.aspx?N=7155+123+182",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8366,
						"Name": "Champagne Bollinger",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne-Bollinger\/learnabout.aspx?winery=99",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/99.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=99"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Bollinger-Brut-Special-Cuvee\/wine\/513\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Bollinger-Brut-Special-Cuvee\/wine\/513\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=99"
					},
					"PriceMax": 79.9900,
					"PriceMin": 37.9900,
					"PriceRetail": 75.0000,
					"ProductAttributes": [{
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 0,
							"Name": "Congratulations",
							"Url": "",
							"ImageUrl": ""
						}, {
							"Id": 0,
							"Name": "Wedding",
							"Url": "",
							"ImageUrl": ""
						}, {
							"Id": 0,
							"Name": "Birthday",
							"Url": "",
							"ImageUrl": ""
						}
					],
					"Ratings": {
						"HighestScore": 93,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 119568,
					"Name": "Louis Roederer Cristal Brut 2005",
					"Url": "http:\/\/www.wine.com\/V6\/Louis-Roederer-Cristal-Brut-2005\/wine\/119568\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "119568m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/119568m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 142,
						"Name": "Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Vintage\/wine\/list.aspx?N=7155+123+142",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8079,
						"Name": "Louis Roederer",
						"Url": "http:\/\/www.wine.com\/v6\/Louis-Roederer\/learnabout.aspx?winery=988",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/988.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=988"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Louis-Roederer-Cristal-Brut-2005\/wine\/119568\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Louis-Roederer-Cristal-Brut-2005\/wine\/119568\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=988"
					},
					"PriceMax": 219.9900,
					"PriceMin": 199.9900,
					"PriceRetail": 219.9900,
					"ProductAttributes": [{
							"Id": 36,
							"Name": "Collectible Wines",
							"Url": "http:\/\/www.wine.com\/v6\/Collectible-Wines\/wine\/list.aspx?N=7155+36",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_collectable_big.gif"
						}, {
							"Id": 15419,
							"Name": "Great Bottles to Give",
							"Url": "http:\/\/www.wine.com\/v6\/Great-Bottles-to-Give\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 0,
							"Name": "Congratulations",
							"Url": "",
							"ImageUrl": ""
						}
					],
					"Ratings": {
						"HighestScore": 97,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 89114,
					"Name": "Veuve Clicquot Rare Vintage 1988",
					"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-Rare-Vintage-1988\/wine\/89114\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "89114m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/89114m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 142,
						"Name": "Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Vintage\/wine\/list.aspx?N=7155+123+142",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8871,
						"Name": "Veuve Clicquot",
						"Url": "http:\/\/www.wine.com\/v6\/Veuve-Clicquot\/learnabout.aspx?winery=106",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/106.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=106"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-Rare-Vintage-1988\/wine\/89114\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-Rare-Vintage-1988\/wine\/89114\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=106"
					},
					"PriceMax": 209.9900,
					"PriceMin": 89.0000,
					"PriceRetail": 95.0000,
					"ProductAttributes": [{
							"Id": 36,
							"Name": "Collectible Wines",
							"Url": "http:\/\/www.wine.com\/v6\/Collectible-Wines\/wine\/list.aspx?N=7155+36",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_collectable_big.gif"
						}, {
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}
					],
					"Ratings": {
						"HighestScore": 95,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 20128,
					"Name": "Piper-Heidsieck Brut Cuvee",
					"Url": "http:\/\/www.wine.com\/V6\/Piper-Heidsieck-Brut-Cuvee\/wine\/20128\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "20128m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/20128m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 182,
						"Name": "Non-Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Non-Vintage\/wine\/list.aspx?N=7155+123+182",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 999999849,
						"Name": "Piper-Heidsieck",
						"Url": "http:\/\/www.wine.com\/v6\/Piper-Heidsieck\/learnabout.aspx?winery=2646",
						"ImageUrl": "",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=2646"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Piper-Heidsieck-Brut-Cuvee\/wine\/20128\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Piper-Heidsieck-Brut-Cuvee\/wine\/20128\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=2646"
					},
					"PriceMax": 4949.0000,
					"PriceMin": 28.9900,
					"PriceRetail": 39.9900,
					"ProductAttributes": [{
							"Id": 15419,
							"Name": "Great Bottles to Give",
							"Url": "http:\/\/www.wine.com\/v6\/Great-Bottles-to-Give\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}
					],
					"Ratings": {
						"HighestScore": 93,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 107629,
					"Name": "Dom Perignon Andy Warhol Yellow Label 2002",
					"Url": "http:\/\/www.wine.com\/V6\/Dom-Perignon-Andy-Warhol-Yellow-Label-2002\/wine\/107629\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "107629m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/107629m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 142,
						"Name": "Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Vintage\/wine\/list.aspx?N=7155+123+142",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8757,
						"Name": "Dom Perignon",
						"Url": "http:\/\/www.wine.com\/v6\/Dom-Perignon\/learnabout.aspx?winery=100",
						"ImageUrl": "",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=100"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 0,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Dom-Perignon-Andy-Warhol-Yellow-Label-2002\/wine\/107629\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Dom-Perignon-Andy-Warhol-Yellow-Label-2002\/wine\/107629\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=100"
					},
					"PriceMax": 159.0000,
					"PriceMin": 149.9900,
					"PriceRetail": 159.0000,
					"ProductAttributes": [{
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 15419,
							"Name": "Great Bottles to Give",
							"Url": "http:\/\/www.wine.com\/v6\/Great-Bottles-to-Give\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 36,
							"Name": "Collectible Wines",
							"Url": "http:\/\/www.wine.com\/v6\/Collectible-Wines\/wine\/list.aspx?N=7155+36",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_collectable_big.gif"
						}
					],
					"Ratings": {
						"HighestScore": 96,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 110659,
					"Name": "Canard-Duchene Authentic Brut Rose",
					"Url": "http:\/\/www.wine.com\/V6\/Canard-Duchene-Authentic-Brut-Rose\/wine\/110659\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "110659m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/110659m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": -2147483648,
						"Name": "Rosé",
						"Url": "http:\/\/www.wine.com\/v6\/Rose\/wine\/list.aspx?N=7155+123+-2147483648",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 5762,
						"Name": "Canard-Duchene",
						"Url": "http:\/\/www.wine.com\/v6\/Canard-Duchene\/learnabout.aspx?winery=18072",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/18072.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": ""
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Canard-Duchene-Authentic-Brut-Rose\/wine\/110659\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Canard-Duchene-Authentic-Brut-Rose\/wine\/110659\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": ""
					},
					"PriceMax": 44.9900,
					"PriceMin": 39.9900,
					"PriceRetail": 55.0000,
					"ProductAttributes": [{
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 15424,
							"Name": "Has Video",
							"Url": "http:\/\/www.wine.com\/v6\/Has-Video\/wine\/list.aspx?N=7155+15424",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_video.gif"
						}, {
							"Id": 0,
							"Name": "For Her",
							"Url": "",
							"ImageUrl": ""
						}
					],
					"Ratings": {
						"HighestScore": 91,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}, {
					"Id": 92241,
					"Name": "Veuve Clicquot La Grande Dame 1998",
					"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-La-Grande-Dame-1998\/wine\/92241\/detail.aspx",
					"Appellation": {
						"Id": 2331,
						"Name": "Champagne",
						"Url": "http:\/\/www.wine.com\/v6\/Champagne\/wine\/list.aspx?N=7155+102+2331",
						"Region": {
							"Id": 102,
							"Name": "France - Other regions",
							"Url": "http:\/\/www.wine.com\/v6\/France-Other-regions\/wine\/list.aspx?N=7155+102",
							"Area": null
						}
					},
					"Labels": [{
							"Id": "92241m",
							"Name": "thumbnail",
							"Url": "http:\/\/cache.wine.com\/labels\/92241m.jpg"
						}
					],
					"Type": "Wine",
					"Varietal": {
						"Id": 142,
						"Name": "Vintage",
						"Url": "http:\/\/www.wine.com\/v6\/Vintage\/wine\/list.aspx?N=7155+123+142",
						"WineType": {
							"Id": 123,
							"Name": "Champagne & Sparkling",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-and-Sparkling\/wine\/list.aspx?N=7155+123"
						}
					},
					"Vineyard": {
						"Id": 8871,
						"Name": "Veuve Clicquot",
						"Url": "http:\/\/www.wine.com\/v6\/Veuve-Clicquot\/learnabout.aspx?winery=106",
						"ImageUrl": "http:\/\/cache.wine.com\/aboutwine\/basics\/images\/winerypics\/106.jpg",
						"GeoLocation": {
							"Latitude": -360,
							"Longitude": -360,
							"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=106"
						}
					},
					"Vintage": "",
					"Community": {
						"Reviews": {
							"HighestScore": 5,
							"List": [],
							"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-La-Grande-Dame-1998\/wine\/92241\/detail.aspx?pageType=reviews"
						},
						"Url": "http:\/\/www.wine.com\/V6\/Veuve-Clicquot-La-Grande-Dame-1998\/wine\/92241\/detail.aspx"
					},
					"Description": "",
					"GeoLocation": {
						"Latitude": -360,
						"Longitude": -360,
						"Url": "http:\/\/www.wine.com\/v6\/aboutwine\/mapof.aspx?winery=106"
					},
					"PriceMax": 179.0000,
					"PriceMin": 115.0000,
					"PriceRetail": 149.9900,
					"ProductAttributes": [{
							"Id": 36,
							"Name": "Collectible Wines",
							"Url": "http:\/\/www.wine.com\/v6\/Collectible-Wines\/wine\/list.aspx?N=7155+36",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_collectable_big.gif"
						}, {
							"Id": 15419,
							"Name": "Champagne Gifts",
							"Url": "http:\/\/www.wine.com\/v6\/Champagne-Gifts\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 15419,
							"Name": "Great Bottles to Give",
							"Url": "http:\/\/www.wine.com\/v6\/Great-Bottles-to-Give\/gift\/list.aspx?N=7151+15419",
							"ImageUrl": "http:\/\/cache.wine.com\/images\/glo_icon_gift_big.gif"
						}, {
							"Id": 0,
							"Name": "Corporate Gifts",
							"Url": "",
							"ImageUrl": ""
						}
					],
					"Ratings": {
						"HighestScore": 97,
						"List": []
					},
					"Retail": null,
					"Vintages": {
						"List": []
					}
				}
			],
			"Offset": 0,
			"Total": 859,
			"Url": ""
		}
	};

	$(".json").append(buildList(json, true));
	$(".json > div").addClass("expanded");
	$(".json").on("click", "li.expand", function (event) {
		event.stopPropagation();
		$(this).toggleClass("expanded");
	});
	$(".json").on("click", "li", function (event) {
		event.stopPropagation();
	});
};

$(document).ready(window.init);