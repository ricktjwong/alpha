module.exports = {
  apps : [
  {
    name       : "alpha-client",
    script     : "sudo npx serve -l 3001 client/build"
  },
  {
    name        : "alpha-server",
    script      : "sudo make -C backend server.start"
  }]
}