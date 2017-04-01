request = require 'request'
noflo = require 'noflo'

exports.getComponent = ->
  c = new noflo.Component
  c.inPorts.add 'url',
    datatype: 'string'
  c.outPorts.add 'body',
    datatype: 'object'
  c.outPorts.add 'response',
    datatype: 'object'
  c.outPorts.add 'error',
    datatype: 'object'
    
  c.process (input, output) ->
    url = input.getData 'url'
    r = request url, (err, response, body) ->
      return output.done err if err
      output.sendDone
        body: body
        response: response