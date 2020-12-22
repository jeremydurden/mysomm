// Search Function Home Page //
const WineryToggleBtnEl = document.getElementById('winery-toggle-btn');
const WineToggleBtnEl = document.getElementById('wine-toggle-btn');
const WinerySearchEl = document.getElementById('winery-search-form');
const WineSearchEl = document.getElementById('wine-search-form');
const SearchResultsEl = document.getElementById('search-results');
const WineResultsHeaderEl = document.getElementById('wine-results-header');
const WineryResultsHeaderEl = document.getElementById('winery-results-header');
const WineColorSelectEl = document.getElementById('id_color_wine');
const WineSearchBtnEl = document.getElementById('wine-search-btn');
const DropDownMenuEl = document.getElementById('wine-dropdown');

DropDownMenuEl.addEventListener('click', function(e) {
    e.stopPropagation();

})

WineSearchBtnEl.addEventListener('click', function(e){
    DropDownMenuEl.parentElement.classList.remove('show');
    WineToggleBtnEl.setAttribute('aria-expanded', 'false');
    DropDownMenuEl.classList.remove('show');
});


WineColorSelectEl.addEventListener('change', function(e){
    if(e.target.value === ""){
        e.target.classList.add('form-placeholder');
    } else {
        e.target.classList.remove('form-placeholder');
    }
})


WineSearchEl.addEventListener('submit', function(e){
    e.preventDefault();
    let serialData = $(this).serialize();
    $.ajax({
        type: 'GET',
        url: "/wine/search",
        data: serialData,
        success: function (response) {
            WineryResultsHeaderEl.classList.add('hidden');
            SearchResultsEl.innerHTML = "";
            response.forEach(function(wine){
                let tr = document.createElement('tr');
                let name = createLink(wine.name, wine.id);
                let grape = createLink(wine.grape, wine.id);
                let color = createLink(wine.color, wine.id);
                let vintage = createLink(wine.vintage, wine.id);
                tr.appendChild(name);
                tr.appendChild(grape);
                tr.appendChild(color);
                tr.appendChild(vintage);
                WineResultsHeaderEl.classList.remove('hidden');
                SearchResultsEl.appendChild(tr);
            });
        },
        error: function (response) {
            SearchResultsEl.innerHTML = "";
        }
    });
});

WinerySearchEl.addEventListener('submit', function(e){
    e.preventDefault();
    let serialData = $(this).serialize();
    $.ajax({
        type: 'GET',
        url: "/winery/search",
        data: serialData,
        success: function (response) {
            WineResultsHeaderEl.classList.add('hidden');
            SearchResultsEl.innerHTML = "";
            response.forEach(function(winery){
                let tr = document.createElement('tr');
                let name = createLink(winery.name, winery.id);
                let region = createLink(winery.region, winery.id);
                let county = createLink(winery.county, winery.id) ;
                let state = createLink(winery.state, winery.id);
                tr.appendChild(name);
                tr.appendChild(region);
                tr.appendChild(county);
                tr.appendChild(state);
                WineryResultsHeaderEl.classList.remove('hidden');
                SearchResultsEl.appendChild(tr);
            });
        },
        error: function (response) {
            SearchResultsEl.innerHTML = "";
        }
    });

});

// Clickable functionality for the map
var myPlot = document.getElementsByClassName('plotly-graph-div')[0];
myPlot.on('plotly_click', function(data){
    const token = document.getElementById('csrf').firstElementChild.value;
    let countyId = data.points[0].customdata;
    $.ajax({
        type: 'GET',
        url: "/wine/mapsearch",
        data: {
            token: token,
            county: countyId
        },
        success: function (response) {
            WineryResultsHeaderEl.classList.add('hidden');
            SearchResultsEl.innerHTML = "";
            response.forEach(function(wine){
                let tr = document.createElement('tr');
                let name = createLink(wine.name, wine.id);
                let grape = createLink(wine.grape, wine.id);
                let color = createLink(wine.color, wine.id);
                let vintage = createLink(wine.vintage, wine.id);
                tr.appendChild(name);
                tr.appendChild(grape);
                tr.appendChild(color);
                tr.appendChild(vintage);
                WineResultsHeaderEl.classList.remove('hidden');
                SearchResultsEl.appendChild(tr);
            });
        },
        error: function (response) {
            SearchResultsEl.innerHTML = "";
        }
    });

});
function createLink(content, wineId){
    let td = document.createElement('td');
    let link = document.createElement('a');
    link.textContent = content;
    link.href = "/wine/" + wineId;
    td.appendChild(link);
    return td;
}