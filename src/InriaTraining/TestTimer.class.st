Class {
	#name : #TestTimer,
	#superclass : #TestCase,
	#category : #InriaTraining
}

{ #category : #tests }
TestTimer >> testTimerCanBeInitialized [
	| timer |
	timer := Timer new: 10.
	self assert: timer current equals: 10
]

{ #category : #tests }
TestTimer >> testTimerIsZeroByDefault [
	| timer |
	timer := Timer new.
	self assert: timer current isZero
]

{ #category : #tests }
TestTimer >> testTimerNextDecresesOnlyToZero [
	| timer |
	timer := Timer new: 0.
	timer next.
	self assert: timer current equals: 0
]

{ #category : #tests }
TestTimer >> testTimerNextDecresesTimerState [
	| timer |
	timer := Timer new: 10.
	timer next.
	self assert: timer current equals: 9
]
