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
    $.ajax({
        type: 'GET',
        url: "/wine/search",
        data: serialData,
        success: function (response) {
            WineryResultsHeaderEl.classList.add('hidden');
            SearchResultsEl.innerHTML = "";
            // TODO add links
            response.forEach(function(wine){
                let link = document.createElement('a');
                link.href = "/wine/" + wine.id;
                let tr = document.createElement('tr');
                let name = document.createElement('td');
                name.textContent = wine.name;
                let grape = document.createElement('td');
                grape.textContent = wine.grape;
                let color = document.createElement('td');
                color.textContent = wine.color;
                let vintage = document.createElement('td');
                vintage.textContent = wine.vintage;
                tr.appendChild(name);
                tr.appendChild(grape);
                tr.appendChild(color);
                tr.appendChild(vintage);
                link.appendChild(tr);
                WineResultsHeaderEl.classList.remove('hidden');
                SearchResultsEl.appendChild(link);
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
             // TODO add links
            response.forEach(function(winery){
                let link = document.createElement('a');
                link.href = "/winery/" + winery.id;
                let tr = document.createElement('tr');
                let name = document.createElement('td');
                name.textContent = winery.name;
                let region = document.createElement('td');
                region.textContent = winery.region;
                let county = document.createElement('td');
                county.textContent = winery.county;
                let state = document.createElement('td');
                state.textContent = winery.state;
                tr.appendChild(name);
                tr.appendChild(region);
                tr.appendChild(county);
                tr.appendChild(state);
                link.appendChild(tr);
                WineryResultsHeaderEl.classList.remove('hidden');
                SearchResultsEl.appendChild(link);
            });
        },
        error: function (response) {
            SearchResultsEl.innerHTML = "";
        }
    });

});