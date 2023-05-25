Class {
	#name : #BaselineOfTrainingInria,
	#superclass : #BaselineOf,
	#category : #BaselineOfTrainingInria
}

{ #category : #baselines }
BaselineOfTrainingInria >> baseline: spec [
	<baseline>
	spec for: #common do: [
		spec package: 'InriaTraining'.
		spec group: 'default' with: #('InriaTraining')
	]
]
