Runscripts
==========

Why runscripts?
---------------

There exist workflows common to many stages of many scientific projects, where **automation** is useful. An almost universal example in has to do with the generation of data at various sets of parameters. Typically, one would write a code to calculate some \(f(x,a)\), with \(x\) and \(a\) being parameters or inputs. One might want to plot \(f(x,a_0)\) at a constant \(a=a_0\) by calculating it at some set of grid points \(\{x_i\}\); then maybe repeat this exercise for a few different values of \(a_0\), and later increase the grid's resolution. As a project grows more complicated and the number of parameters and cuts through the parameter space increases, managing the necessary set of runs manually becomes a chore, and scripting becomes important.

This is by no means complicated, and it is generally educational. However, if you spend some time thinking about how to best automate your data generation, you will quickly find that you want some increasingly complex features. These might include running Cartesian products of parameters; maintaining a consistent and possibly tiered directory structure where jobs at specific parameters are easy to find and aggregation is simple; handling dependencies between jobs; automatically running only new jobs, or finding and rerunning only crashed jobs; and limiting the number of jobs you queue to comply with the regulations on some cluster, or throttling the submission rate to avoid crashing the queue manager. Designing a good workflow then becomes less trivial.

I've seen and / or tried [various approaches](https://en.wikipedia.org/wiki/Scientific_workflow_system) over the years, from minimal shell scripts to complex frameworks (most of which seem to be specialized to certain fields). The scripts provided here lean towards the minimal and are a good fit for quite a few projects of different sizes. They're simple enough for anyone to read through and understand completely, and require no special setup procedures. However, they're also flexible enough to scale from the first thing you'll want to do as a student - using those extra cores on your laptop to shorten the waiting time on a completely serial code - to managing big workloads on a cluster or supercomputer. At some point others started asking me for these scripts, and since it seems that many people now like and use them, I decided to share them publicly. I encourage my own students to use them as a starting point.

Usage
-----

I've provided a few examples, in increasing order of complexity. The best way to get started is by cloning the repository and playing around! Go into the `01_example_local_serial_run` subdirectory, and run:
~~~
python ../prepare.py
~~~

There are three parameter files in each directory: `runs.param`,  `general.param` and `execution.param`. The separation is designed to maximize reuse:

* `runs.param` is specific to a particular set of runs: for instance, you might have a file called `runs.dynamics.param` for the time dependence of an observable's expectation value, and another called `runs.steady_state.param` for its temperature dependence at the long time limit. 
* `general.param` is specific to a project, and might be shared between different run files and on different machines.
* `execution.param` has to do with a particular method of executing the jobs, and might be shared between different projects on the same cluster, or differ between machines on the same project.

By default, this queues up the parameters in the file `runs.param` on your local machine. You can give another file name as a command line parameter - try copying runs.param to runs.other.param, for instance, and running that. Open the file and look at the parameters: in particular, `numConcurrentProcesses = 4` will have your (serial!) jobs running simultaneously on four cores, such that each core is executing a different parameter.

The assumption is that your applications will receive a text-based parameter file in some format of your choice, as defined in the `template` in `general.param`. In the example, for simplicity, it's actually a python file which gets executed. However, there are reasonable and standardized cross-platform choices, e.g. YAML. If your parameters are hardcoded, rethink that choice. If they're given on the command line for anything but a small interactive shell application, rethink that choice (though it's easily supported). If you use some binary format so that parameters and data can exist in the same file, rethink both choices.

See the remaining directories for examples of parallel (MPI) jobs and cluster (PBS / Slurm) jobs.


TODO
----

This is a work in progress. If anyone wants to make improvements, add examples or clarify the documentation, feel free to open an issue or send me a pull request!

Some things that have been done before and could be useful:
* Support for job arrays (on some clusters this is allows you to submit more jobs simultaneously).
* An example using SLURM rather than PBS directives (on some clusters PBS directives are disabled).
