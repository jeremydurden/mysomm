// Search Function Home Page //
const WineryToggleBtnEl = document.getElementById('winery-toggle-btn');
const WineToggleBtnEl = document.getElementById('wine-toggle-btn');
const WinerySearchEl = document.getElementById('winery-search-form');
const WineSearchEl = document.getElementById('wine-search-form');
const SearchResultsEl = document.getElementById('search-results');
const WineResultsHeaderEl = document.getElementById('wine-results-header');
const WineryResultsHeaderEl = document.getElementById('winery-results-header');


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
                WineResultsHeaderEl.classList.remove('hidden');
                SearchResultsEl.appendChild(tr);
            });
        },
        error: function (response) {
            SearchResultsEl.innerHTML = "";
        }
    });
});