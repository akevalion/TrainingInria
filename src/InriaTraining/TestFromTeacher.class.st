Class {
	#name : #TestFromTeacher,
	#superclass : #TestCase,
	#category : #InriaTraining
}

{ #category : #tests }
TestFromTeacher >> factorial: input [
	^ input factorial
]

{ #category : #tests }
TestFromTeacher >> meaning [
	^ 42
]

{ #category : #tests }
TestFromTeacher >> testFactorial [
	| expected |
	expected := #( 0 1 1 1 5 120 720).
	expected pairsDo: [ :input :ouput | | result |
		result := self factorial: input.
		self assert: result equals: result.
	].
]

{ #category : #tests }
TestFromTeacher >> testFactorialFive [
	| result |
	result := self factorial: 5.
	self assert: result equals: 120.
]

{ #category : #tests }
TestFromTeacher >> testFactorialZero [
	| result |
	result := self factorial: 0.
	self assert: result equals: 1.
]

{ #category : #tests }
TestFromTeacher >> testMeaningIs42 [
	| result |
	result := self meaning.
	self assert: result equals: 42
]
