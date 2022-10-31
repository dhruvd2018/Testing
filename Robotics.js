//create machine learning model
const model = tf.sequential();
//add layers to model
model.add(tf.layers.dense({units: 1, inputShape: [1]}));
//compile model
model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});
//train model
model.fit(xs, ys, {epochs: 500}).then(() => {
    //predict output
    model.predict(tf.tensor2d([5], [1, 1])).print();
});
