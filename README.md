# Design Patterns in Python

The Design Patterns illustrated and implemented in this repository come from the [*Design Patterns: Elements of Reusable
Object Oriented Software*](https://en.wikipedia.org/wiki/Design_Patterns) book, written by written by Erich Gamma,
Richard Helm, Ralph Johnson, and John Vlissides, a.k.a. The Gang of Four (GoF).

I hope the implementations are clear enough to be re-implemented in any other programming language.

As a side note: this is still work in progress. I will start implementing the patterns I either like most or have used
more often throughout my career.

# Preparing the Environment

The repository comes with a [Conda](https://docs.conda.io/en/latest/) environment file with the dependencies you need to
run everything. If you don't have Conda installed please proceed to the link above and install it. Once it's installed,
you can create the environment by simply typing the command below:

```shell script
conda env create -f environment.yml
```

Once the environment has been created, you can activate it by typing the command below:

```shell script
conda activate python-dp
```

Explanations about how to run the sample code can be found inside the dedicated packages.

# Implementations

## Creational Design Patterns

* Abstract
* Builder
* Factory
* Prototype
* [Singleton](patterns/singleton/README.md)

## Structural Design Patterns

* Adapter
* Bridge
* Composite
* Decorator
* Facade
* Flyweight
* Proxy

## Behavioural Design Patterns

* Chain of responsibility
* [Command](patterns/command/README.md)
* Interpreter
* Iterator
* Mediator
* Memento
* Observer
* State
* Strategy
* Template
* Visitor
