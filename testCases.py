# these are the test cases to be used when testing the actual code.
# (the actual code is not here and thus this code will give an error when ran.)
colName = 'collection'
docName = 'document'

# put in data first before testing modifications to it.
firestoreStorage.updateField(colName, docName, [('field', 'value')])

def testCase_1():
  firestoreStorage.updateField(colName, docName, [])
  assert firestoreStorage.getFieldValue(colName, docName, 'field') = 'value'
  
def testCase_2():
  firestoreStorage.updateField(colName, docName, [('field', 'newVal')])
  assert firestoreStorage.getFieldValue(colName, docName, 'field') = 'newVal'

def testCase_3():
  try:
    firestoreStorage.updateField(colName, docName, [('field', '?#$')])
  except Exception:
    return True
  
def testCase_4():
  try:
    firestoreStorage.updateField(colName, docName, [('field', '')])
  except Exception:
    return True

def testCase_5():
  firestoreStorage.updateField(colName, docName, [('field', ['val1', 'val2'])])
  assert firestoreStorage.getFieldValue(colName, docName, 'field') == ['val1', 'val2']

def testCase_6():
  try:
    firestoreStorage.updateField(colName, docName, [('field', ['??', '$$'])])
  except Exception:
    return True

def testCase_7():
  try:
    firestoreStorage.updateField(colName, docName, [('field', ['', ''])])
  except Exception:
    return True
  