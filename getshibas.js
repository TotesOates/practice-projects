function httpGetAsync('http://shibe.online/api/shibes?count=[1]&urls=[true]&httpsUrls=[true]', callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", 'http://shibe.online/api/shibes?count=[1]&urls=[true]&httpsUrls=[true]', true); // true for asynchronous 
    xmlHttp.send(null);
}