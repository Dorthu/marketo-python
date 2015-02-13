import xml.etree.ElementTree as ET
import lead_record, sync_lead, result_record

def wrap(leads=None, create_duplicates=False):

	ret = (
		'<mkt:paramsSyncMultipleLeads>' +
		'<leadRecordList>'
	)

	for lead in leads:
		wrapped_lead = sync_lead.wrap(email=lead[0], attributes=lead[1])
		ret += wrapped_lead[wrapped_lead.index('<leadRecord>'):wrapped_lead.index('</leadRecord')+13]


	ret += (
		'</leadRecordList>' +
		'<dedupEnabled>' + ('false' if create_duplicates else 'true') + '</dedupEnabled>' +
		'</mkt:paramsSyncMultipleLeads>'
	)

	return ret

def unwrap(response):
	root = ET.fromstring(response.text)
	resultList = root.find('.//result')

	unwrappedList = []

	for result in resultList.findall('.//syncStatus'):
		unwrappedList.append(result_record.unwrap(result))

	return unwrappedList
