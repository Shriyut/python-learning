# Airflow

Apache Airflow is a tool that helps you create, organize, and keep track of your data tasks automatically.


## DAG - Directed Acyclic Graph

A DAG is a collection of all the tasks you want to run, organized in a way that reflects their dependencies.
It helps define the structure of a workflow, showing which tasks need to happen before others.

## Operator

An operator defines a single, ideally idempotent, task in DAG. Operators allow you to break down workflow into discrete, manageable pieces of work.

## Task

A task is a specific instance of an operator. When an operator is assigned to a DAG, it becomes a task.
Tasks are the actual units of work that get executed when DAG runs.

## Workflow

A workflow is the entire process defined by DAG, including all tasks and their dependencies.

## What Airflow is not:

- Data processing framework
- Real time streaming solution
- Data storage system

## Use-cases where Airflow isn't the best fit

- High-frequency, sub-minute scheduling
- Processing large datasets directly
- Real-time data streaming
- Simple linear workflow with few dependencies

## Architecture

- Single Node Architecture
  - All components of airflow are running on one machine
- Multi-node Architecture
  - Airflow runs across multiple compute servers

### Component 1: Metadata Database

A database that stores information about tasks and their status. It keeps track of details related to workflow.

### Component 2: The Scheduler

The scheduler is responsible for determining when tasks should run, it ensures tasks run at the right time and in correct order.

### Component 3: The DAG file processor

THe DAG file processor parses DAG files and serializes them into the metadata database.

### Component 4: The Executor

The executor determines how tasks will be run, it manages the execution of your tasks, deciding whether to run them in sequence or in parallel and on which system.

### Component 5: The API server

THe API server provides endpoints for task operations and serving the UI.

### Component 6: The worker

Workers are the processes that actually perform the tasks.

### Component 7: The Queue

The queue is a list of tasks waiting to be executed.

### Component 8: The Triggerer

The triggerer is responsible for managing deferrable tasks - tasks that wait for external events



