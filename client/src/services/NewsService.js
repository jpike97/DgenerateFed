import jQuery from "jquery";
let $ = jQuery;
//TODO: move this to python logic & put it in a CRON task probably
export default {
    fetchNews (id, callback) {
    var feedURL = "https://news.google.com/rss/search?q=" + id;
    $.ajax({
        type: 'GET',
        url: "https://api.rss2json.com/v1/api.json?rss_url=" + feedURL,
        dataType: 'jsonp',
        success: function(result) {
            console.log("in service");
            console.log(result);
            callback(true, result);
        }
      });
  }
}