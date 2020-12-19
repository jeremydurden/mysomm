// Search Function Home Page //
const WineryToggleBtnEl = document.getElementById('winery-toggle-btn');
const WineToggleBtnEl = document.getElementById('wine-toggle-btn');
const WinerySearchEl = document.getElementById('winery-search-form');
const WineSearchEl = document.getElementById('wine-search-form');


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