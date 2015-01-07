/**
 * @author Tomsik68
 */
function buildCategoryView(categories) {
	var html = "";
	for (category in categories) {
		html += "<li class='category'><a href='#' onclick='switchCategory(\"" + categories[category].name + "\")' class='linkToCategory'>" + categories[category].title + "</a></li>";
	}
	document.getElementById('categories').innerHTML = html;
	switchCategory('all');
}

function createFiltersView(filters) {
	var html = "";
	if (filters.length > 0) {
		html = "<ul id='filters'>";
		for (key in filters) {
			var filter = filters[key];
			html += "<li><div class='filter'><h3>" + filter.name + "<span class='filter-author'>by " + filter.author + "</span></h3>";
			html += filter.desc + "<span class='filter-actions'><a href='" + filter.dl + "'><img class='filter-action' src='http://icons.iconarchive.com/icons/gakuseisean/ivista-2/32/Network-Download-icon.png'/></a><a href='" + filter.src + "'><img class='filter-action' src='lib/GitHub-Mark-32px.png' /></a>";
			if (filter.vid != undefined && filter.vid.length > 0 && filter.vid != "https://youtube.com") {
				html += "<a onclick='play(\""+filter.vid+"\")' href='#'><img class='filter-action' src='lib/youtube.png' /></a>";
			}
			html += "</span></div></li>";
		}
		html += "</ul>";

	} else {
		html = "<h1 align='center'> No filters :(</h1>";
	}
	document.getElementById('content').innerHTML = html;
}

function switchCategory(dest) {
	var filters = getFiltersInCategory(dest);
	createFiltersView(filters);
	var category = getCategory(dest);
	var html = '<h1>' + category.title + '</h1>';
	if (category.desc != undefined) {
		html += "<BR>" + category.desc + "<HR width='80%'><BR>";
	}
	document.getElementById('category').innerHTML = html;
}
