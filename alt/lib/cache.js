/**
 * @author Tomsik68
 */

var dataObject = null;
var jsonFile = 'lib/filters.json';

function loadData(){
	$.ajax(jsonFile).done(onJSONFileRetrieved);
}
function onJSONFileRetrieved(json) {
	dataObject = eval(json);
	dataObject.categories.splice(0,0,{"name":"all","title":"All Filters"});
	buildCategoryView(getCategories());
}

function getCategories() {
	return dataObject.categories;
}

function getFilters() {
	return dataObject.filters;
}
