# Redis Data Generator for Performance Testing and Debugging Training

Generates random key-value pairs between char lenght 100 and 1000, then feeds redis instance.

You can use it to learn debugging Redis itself by working large keys and values.

When pod starts to run, it sends 10000 key-value pairs to redis. Then crashes and openshift restarts the pod. And **the cycle goes on** until you set replica count to 0 from deployment config.