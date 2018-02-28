def flatten_dict(dictx, result_dict=None):
        dict_keys=dictx.keys()

        if result_dict is None:
                result_dict={}
        for elem_key in dict_keys:
                inner_dict=dictx[elem_key]
                if isinstance(inner_dict,dict):
			new={}


                        for z in inner_dict.keys():
                                new[str(elem_key)+'.'+str(z)]=inner_dict[z]
                        flatten_dict(new,result_dict)
                else:
                        result_dict[elem_key]=dictx[elem_key]
        return result_dict

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

