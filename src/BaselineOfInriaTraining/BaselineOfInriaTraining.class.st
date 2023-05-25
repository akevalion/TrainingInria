Class {
	#name : #BaselineOfInriaTraining,
	#superclass : #BaselineOf,
	#category : #BaselineOfInriaTraining
}

{ #category : #baselines }
BaselineOfInriaTraining >> baseline: spec [
	spec for: #common do: [
		spec package: 'InriaTraining'.
		spec group: 'default' with: #('InriaTraining')
			
	]
]
