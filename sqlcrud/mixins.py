from django.core.serializers import serialize
import json

class FilterFields(object):
    def filtered(self,data):
        json_data = serialize('json',data)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        return json.dumps(final_list)