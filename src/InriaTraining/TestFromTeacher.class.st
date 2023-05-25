Class {
	#name : #TestFromTeacher,
	#superclass : #TestCase,
	#category : #InriaTraining
}

{ #category : #tests }
TestFromTeacher >> meaning [
	^ 42
]

{ #category : #tests }
TestFromTeacher >> testMeaningIs42 [
	| result |
	result := self meaning.
	self assert: result equals: 42
]
