import Endpoints from 'byteplug-endpoints'

var endpoints = new Endpoints("http://api.my-company.com")

var endpoint = endpoints.endpoint("hello")
endpoint.response = function(document) {
    // Root element of the JSON document is a string, therefore, it will print
    // a string.
    console.log(document)
}

// Will print "Hello you!" to the console.
endpoint.request("you")
