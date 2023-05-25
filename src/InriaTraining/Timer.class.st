Class {
	#name : #Timer,
	#superclass : #Object,
	#instVars : [
		'count'
	],
	#category : #InriaTraining
}

{ #category : #'instance creation' }
Timer class >> new: value [
	^ self new
		count: value;
		yourself
]

{ #category : #accessing }
Timer >> count: aNumber [
	count := aNumber
]

{ #category : #accessing }
Timer >> current [
	^ count
]

{ #category : #initialization }
Timer >> initialize [
	super initialize.
	self count: 0
]

{ #category : #accessing }
Timer >> next [
	count < 1 ifTrue: [ ^ self ].
	count := count - 1
]
