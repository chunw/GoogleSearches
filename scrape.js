var xpath = '//div[@aria-label="Card showing an activity from Search"]//div[contains(text(),"Searched for")]//a/text()'
var entries = $x(xpath);
console.log('You searched for ' + entries.length + ' entries');
entries.forEach(entry => console.log(entry));
