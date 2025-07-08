running the sandbox:

```
flytectl sandbox start

export FLYTECTL_CONFIG=$(pwd)/config-sandbox.yaml
```

What I am trying to do is to run all the basic functionalities of flytekit.



The process is as follows:
1. Write the tasks and workflow
2. Run the sandbox

3. ?? Register the workflow -> Do I need to register this along an image to run it?? How does imports happend here? is the workflow compiled and put together as a unit before being registered?
4. Do I have to create a launch plan to register the workflow??


5. Run the workflow -> Probably integration testing?

6. Does the regsitering and running happen through python or through the flytekit cli?? What is the best way to do this in a good team?