module.exports = class AppController {
  static getHomepage(req, res) {
    return res.send('Hello Holberton School!');
  }
};
