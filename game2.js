var runGame = fundction()
    showSplashScreen();
    loadAllAssets;
    if (multiplayer) {
        connectToServer();
    }
    initialzePlayfield();
    hideSplashScreen();
    setInterval(gameLoop, 16 * millisecond);

var gameLoop = function() {
    getUserInput();
    if (multiplayer) {
        getPlayfieldfromServer();
            sendUserInputToServer();

else{
    moveAllObjectsAndPlayers();
}    }
renderPlayfield;
};
//
