Class {
	#name : #TestFromTeacher,
	#superclass : #TestCase,
	#category : #InriaTraining
}

{ #category : #tests }
TestFromTeacher >> average: list [
	list ifEmpty: [ ^ self ].
	^ list sum / list size
]

{ #category : #tests }
TestFromTeacher >> factorial: input [
	^ input factorial
]

{ #category : #tests }
TestFromTeacher >> meaning [
	^ 42
]

{ #category : #tests }
TestFromTeacher >> testAverageEmpty [
	| result value |
	value := #().
	result := self average: value.
	self assert: result equals: self
	
]

{ #category : #tests }
TestFromTeacher >> testAverageList [
	| result value |
	value := #(1 2 3 4 5).
	result := self average: value.
	self assert: result equals: 3
	
]

{ #category : #tests }
TestFromTeacher >> testAverageListNumbers [
	| result value |
	value := {
	#(1 2 3 4 5). 3.
	#(-1 -2 -3 -4 -5). -3
	}.
	value pairsDo: [ :input :output |
		result := self average: input.
		self assert: result equals: output
		 ].
	
	
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
