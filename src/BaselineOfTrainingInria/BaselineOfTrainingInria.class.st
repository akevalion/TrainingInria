Class {
	#name : #BaselineOfTrainingInria,
	#superclass : #BaselineOf,
	#category : #BaselineOfTrainingInria
}

{ #category : #baselines }
BaselineOfTrainingInria >> baseline: spec [
	spec for: #common do: [
		spec package: 'InriaTraining'.
		spec group: 'default' with: #('InriaTraining')
	]
]
