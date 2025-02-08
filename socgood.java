import org.deeplearning4j.datasets.iterator.impl.IrisDataSetIterator;
import org.deeplearning4j.nn.api.OptimizationAlgorithm;
import org.deeplearning4j.nn.conf.MultiLayerConfiguration;
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.dataset.api.iterator.DataSetIterator;
import org.nd4j.linalg.learning.config.Adam;
import org.nd4j.linalg.lossfunctions.LossFunctions;

public class SimpleAIModel {
    public static void main(String[] args) {
        int numInputs = 4;
        int numOutputs = 3;
        int numHiddenNodes = 10;

        MultiLayerConfiguration config = new NeuralNetConfiguration.Builder()
            .optimizationAlgo(OptimizationAlgorithm.STOCHASTIC_GRADIENT_DESCENT)
            .updater(new Adam(0.01))
            .list()
            .layer(new DenseLayer.Builder().nIn(numInputs).nOut(numHiddenNodes)
                .activation(Activation.RELU)
                .build())
            .layer(new OutputLayer.Builder(LossFunctions.LossFunction.NEGATIVELOGLIKELIHOOD)
                .activation(Activation.SOFTMAX)
                .nIn(numHiddenNodes).nOut(numOutputs)
                .build())
            .build();

        MultiLayerNetwork model = new MultiLayerNetwork(config);
        model.init();

        DataSetIterator irisData = new IrisDataSetIterator(150, 150);
        model.fit(irisData);

        System.out.println("AI model training complete!");
    }
}