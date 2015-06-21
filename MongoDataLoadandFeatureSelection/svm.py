import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, SingleClassifierEnhancer, MultipleClassifiersCombiner, FilteredClassifier, \
    PredictionOutput, Kernel, KernelClassifier
from weka.classifiers import Evaluation
from weka.filters import Filter
# convert csv into arff format (weka compatable)
# use convertcsvtoarff.py file

# load arff file

loader = Loader("weka.core.converters.ArffLoader")
iris_data = loader.load_file("reviewsinformation_task2.arff")
iris_data.class_is_last()
loader = Loader("weka.core.converters.ArffLoader")
iris_data = loader.load_file(iris_file)
iris_data.class_is_last()

# kernel classifier
helper.print_title("Creating SMO as KernelClassifier")
kernel = Kernel(classname="weka.classifiers.functions.supportVector.RBFKernel", options=["-G", "0.001"])
classifier = KernelClassifier(classname="weka.classifiers.functions.SMO", options=["-M"])
classifier.kernel = kernel
classifier.build_classifier(iris_data)
print("classifier: " + classifier.to_commandline())
print("model:\n" + str(classifier))

#print("model:\n" + str(classifier))


evaluation = Evaluation('test_data.arff')
evaluation.crossvalidate_model(classifier, diabetes_data, 10, Random(42), output=pred_output)
print(evaluation.summary())
print(evaluation.class_details())
print(evaluation.matrix())
