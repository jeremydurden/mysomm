// Search Function Home Page //
const WineryToggleBtnEl = document.getElementById('winery-toggle-btn');
const WineToggleBtnEl = document.getElementById('wine-toggle-btn');
const WinerySearchEl = document.getElementById('winery-search-form');
const WineSearchEl = document.getElementById('wine-search-form');
const SearchResultsEl = document.getElementById('search-results');
const WineResultsHeaderEl = document.getElementById('wine-results-header');
const WineryResultsHeaderEl = document.getElementById('winery-results-header');
const WineColorEl = document.getElementById('id_color_wine');


WineryToggleBtnEl.addEventListener('click', function(e){
    WineSearchEl.classList.add('hidden');
    if(WinerySearchEl.classList.contains('hidden')){
        WinerySearchEl.classList.remove('hidden');
    } else {
        WinerySearchEl.classList.add('hidden');
    }
});

WineToggleBtnEl.addEventListener('click', function(e){
    WinerySearchEl.classList.add('hidden');
    if(WineSearchEl.classList.contains('hidden')){
        WineSearchEl.classList.remove('hidden');
    } else {
        WineSearchEl.classList.add('hidden');
    }
});

WineColorEl.addEventListener('change', function(e){
    if(e.target.value === ""){
        e.target.classList.add('form-placeholder');
    } else {
        e.target.classList.remove('form-placeholder');
    }
})


WineSearchEl.addEventListener('submit', function(e){
    e.preventDefault();
    let serialData = $(this).serialize();
    console.log(serialData);
    $.ajax({
        type: 'GET',
        url: "/wine/search",
        data: serialData,
        success: function (response) {
            WineryResultsHeaderEl.classList.add('hidden');
            SearchResultsEl.innerHTML = "";
            // TODO add links
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
    console.log('click');
    console.log(data)
    console.log(data.points[0].customdata)
    let token = document.getElementById('csrf').firstElementChild.value;
    console.log(token);
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