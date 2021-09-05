import json
import matplotlib.pyplot as plt

def get_average_list(lst, items):
	average = []
	index = []
	start_average = min(lst)
	while start_average <= max(lst):
		total = 0
		count = 0
		for tmp in items:
			if start_average == tmp["exp"]:
				total += tmp["salary"]
				count += 1
				index.append(start_average)
		start_average += 1
		if (count > 0): average.append( round(total/count, 2) )
	return list(set(index)), average

def show_graph_exp_salary(lst):
	exp = []
	salary = []
	for tmp in lst:
		print(tmp)
		exp.append(tmp['exp'])
		salary.append(tmp['salary'])
	plt.scatter(exp, salary, c="b")
	index, average = get_average_list(exp, lst)
	plt.plot(index, average)
	print(index, average)
	plt.show()

def get_data_and_type():
	with open("data.json", "r") as f:
		data = json.loads(f.read())

	back = []
	fs = []
	po = []
	pm = []
	product = []
	lead = []
	code = []

	for item in data:
		if item["type"] == "back":
			back.append(item)
			code.append(item)
		elif item["type"] == "full stack":
			fs.append(item)
			code.append(item)
		elif item["type"] == "lead":
			lead.append(item)
			code.append(item)
		elif item["type"] == "product owner":
			po.append(item)
			product.append(item)
		elif item["type"] == "product manager":
			pm.append(item)
			product.append(item)
		else:
			print(item)
	return data, back, fs, po, pm, product, lead, code