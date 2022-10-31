var runGame = function() {
    var game = new Game();
    game.start();
};

// Path: Game.js
Game.prototype.start = function() {
    this.init();
    this.run();
};
var Game = function() {
    this.player = new Player();
    this.enemy = new Enemy();
}
