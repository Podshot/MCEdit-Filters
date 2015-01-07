/**
 * @author Tomsik68
 */
function search() {
	var query = document.getElementById('search').value;
	if (query.length <= 2)
		return;
	document.getElementById('category').innerHTML = query;
	query = query.toLowerCase();
	var filters = getFilters();
	var result = new Array();
	for (f in filters) {
		var filter = filters[f];
		if (filter.name.toLowerCase() == query || filter.name.toLowerCase().indexOf(query) != -1 || query.indexOf(filter.name.toLowerCase()) != -1 || filter.desc.toLowerCase().indexOf(query) != -1) {
			result.push(filter);
		}
	}
	createFiltersView(result);
}

function getCategory(cat_name) {
	var cats = getCategories();
	for (cat in cats) {
		if (cats[cat].name == cat_name) {
			return cats[cat];
		}
	}
}

function getFiltersInCategory(cat_name) {
	var cat = getCategory(cat_name);
	var filters = getFilters();
	var result = new Array();
	for (f in filters) {
		var filter = filters[f];
		if (filter.categories.indexOf(cat.name) != -1 || cat_name == 'all') {
			result.push(filter);
		}
	}
	return result;
}
