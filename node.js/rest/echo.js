var restify = require('restify');

function respond(request, result, next) {
	result.send('hello ' + request.params.name);
}

var server = restify.createServer();
server.get('/hello/:name', respond);
server.head('/hello/:name', respond);

server.listen(8080, function() {
	console.log('%s listening at %s', server.name, server.url);
});