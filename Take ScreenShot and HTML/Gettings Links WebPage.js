var x = document.querySelectorAll("a");
var myarray = []
for (var i=0; i<x.length; i++){
var nametext = x[i].textContent;
var cleantext = nametext.replace(/\s+/g, ' ').trim();
var cleanlink = x[i].href;
myarray.push([cleantext,cleanlink]);
};
function make_table() {
    var table = '<table><tbody>';
   for (var i=0; i<myarray.length; i++) {
     if (myarray[i][1] !== "javascript:void(0);"){
if (myarray[i][1] !== "javascript:void(0)"){
            table += '<tr><td>'+myarray[i][1]+'</td></tr>';
}}
    };
 
    var w = window.open("");
w.document.write(table); 
}
make_table()