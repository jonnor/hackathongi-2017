noflo = require 'noflo'

exports.getComponent = ->
  c = new noflo.Component
  c.inPorts.add 'gateway',
    datatype: 'string'
  c.inPorts.add 'params',
    datatype: 'object'
  c.inPorts.add 'device',
    datatype: 'string'
  c.inPorts.add 'command',
    datatype: 'string'

  c.outPorts.add 'out',
    datatype: 'object'
  c.outPorts.add 'error',
    datatype: 'object'
    
  c.process (input, output) ->
    return if not input.hasData ['gateway', 'command', 'params', 'device']
    gateway = input.getData 'gateway'
    command = input.getData 'command'
    params = input.getData 'params'
    device = input.getData 'device'
    url = "#{gateway}/device/#{device}/cmds/#{command}"
    o =
      url: url
      qs: params
    output.sendDone o