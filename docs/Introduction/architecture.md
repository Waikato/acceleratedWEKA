The building blocks of Accelerated WEKA are packages like [WekaDeeplearning4j](https://deeplearning.cms.waikato.ac.nz) and [wekaRAPIDS](https://github.com/Waikato/wekaRAPIDS) (inspired by [wekaPython](https://weka.sourceforge.io/packageMetaData/wekaPython/index.html)). 

WekaDeeplearning4j (WDL4J) already supports GPU processing but has very specific needs in terms of libraries and environment configuration. WDL4J provides WEKA wrappers for the Deeplearning4j library.

On the other hand, wekaPython originally provided Python integration by creating a server and communicating with it through sockets, enabling the user to execute scikit-learn ML algorithms (or even XGBoost) inside the WEKA workbench. Furthermore, wekaRAPIDS provide integration with RAPIDS cuML library using a similar technique to wekaPython.

Together, both packages provide enhanced functionality and performance inside the user-friendly WEKA workbench. In fact, Accelerated WEKA goes a step further in the direction of performance by improving the communication between the JVM and Python interpreter. It does so by using alternatives like Apache Arrow and GPU memory sharing. This enables efficient data transfer between the two languages.

Furthermore, Accelerated WEKA provides integration with the RAPIDS cuML library, which implements machine learning algorithms that are accelerated on NVIDIA GPUs. Some cuML algorithms can even support multi-GPU solutions.


<!-- wekaPython Class/Sequence diagram here -->