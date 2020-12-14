import jQuery from "jquery";
let $ = jQuery;

//TODO: move this to SERVER SIDE and CACHE -- see server.js (separate server.js too prob);
export default {
    fetchNews (id, callback) {
    console.log(id);
    id += "-ticker";
    var feedURL = "https://news.google.com/rss/search?q=" + id;
    $.ajax({
        type: 'GET',
        url: "https://api.rss2json.com/v1/api.json?rss_url=" + feedURL,
        dataType: 'jsonp',
        data:  { 
            api_key: "1"
        },
        success: function(result) {
            console.log("in service");
            console.log(result);
            callback(true, result);
        }
      });
  }
}