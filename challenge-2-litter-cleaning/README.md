# Litter Cleaning App - Analysis and Design Challenge

## What do you need to do for this challenge

This is NOT a code challenge. You only must make UML models to analyze the problem, and to design the possible solution.

To solve the challenge you must make the next models:
* Analysis (Problem):
** Domain model diagram: Entities and relationships of the "problem domain". Entities must contain the needed fields and relantionships' multiplicity must be specified.
** Use case diagram: Actors and their use cases related.
* Design (Solution):
** Database entity-relationship diagram: Diagram of tables, fields and dependencies for the possible system's database.

## Definition of the problem

We are CleanForest, a NGO who helps keeping the forests free of litter. We want you to develop an app that help us to localize and register litter in the forest, and to verify when any litter has been cleaned. Also we would like to be able to plan litters cleaning on the app, being able to pick which litters we would plan to clean some specific date.
Every user on the app must be able to register litters or litter cleanings, as well as to verify litters and cleanings registered by other users. The admin user and moderators must be able to ban users and litter/cleaning registrations that are wrong.
About litter, the system should register the location, a description, when it was discovered, some pictures and what kind of litter is. When a litter is cleaned, we want register the date of the cleaning and some pictures. When someone verify a litter or a cleaning the system must save when the verification happends.
One of the users must be the organization itself, who can do the same actions that every user can.
