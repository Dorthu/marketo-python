
class ResultRecord:
	def __init__(self):
		self.leadId = ''
		self.status = ''
		self.error = ''

	def __str__(self):
		return "Lead %s -  Result: %s (error: %s)" % (self.leadId, self.status, self.error)

	def __repr__(self):
		return self.__str__()

def unwrap(xml):
	result = ResultRecord()
	result.leadId = xml.find('leadId').text
	result.status = xml.find('status').text
	result.error = xml.find('error').text

	return result
