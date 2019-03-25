import matplotlib.pyplot as plt
import numpy as np
import os
import pdb
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--subquestion', '-q')

args = parser.parse_args()


res_path = 'final_res'
def filter_paths(keeps=[""]):
	# keeps=["SGD"]
	files = os.listdir(res_path)
	paths=[]
	for name in files:
		if name==".DS_Store":continue
		arch = name.split("_")[0]
		optim = name.split("model")[0].split(arch)[1][1:-1]
		exp = name.split("_")[-1]

		for keep in keeps:
			if keep==arch or keep==optim or  keep =="all":
				paths.append([name,arch,optim,exp])
	return paths



if args.subquestion == '1':

	# pdb.set_trace()
	paths = filter_paths(["TRANSFORMER"])
	for path in paths:
		curves = np.load("{}/{}/learning_curves.npy".format(res_path,path[0])).item()
		train_ppls,val_ppls = curves['train_ppls'],curves['val_ppls']


		fig,ax = plt.subplots(1)
		ax.set_title("{}-{}-Experiment ".format(path[1],path[2],path[-1]))
		ax.plot(train_ppls[1:],label="Train PPL") #Start from 1 as the first PPL is too high
		ax.plot(val_ppls[1:],label="Validation PPL") #Start from 1 as the first PPL is too high
		ax.legend()
		ax.set_xlabel("Epochs")
		ax.set_ylabel("PPL")	
		plt.savefig("plots/4.1/{}_{}_exp{}.jpg".format(path[1],path[2],path[-1]))
		plt.close()


		x = np.arange(0, len(train_ppls)*30, 30)[1:]
		fig,ax = plt.subplots(1)
		ax.set_title("{}-{}-Experiment ".format(path[1],path[2],path[-1]))
		ax.plot(x,train_ppls[1:],label="Train PPL") #Start from 1 as the first PPL is too high
		ax.plot(x,val_ppls[1:],label="Validation PPL") #Start from 1 as the first PPL is too high
		ax.legend()
		ax.set_xlabel("Time (seconds)")
		ax.set_ylabel("PPL")	
		plt.savefig("plots/4.1/{}_{}_exp{}_seconds.jpg".format(path[1],path[2],path[-1]))
		plt.close()


# # 4.4 # Missing RNN and GRU



elif args.subquestion == '5':

	paths = filter_paths(["TRANSFORMER"])
	fig,ax = plt.subplots(1)
	ax.set_title("Optimizers comparison for {}".format(paths[0][1]))
	for path in paths:
		curves = np.load("{}/{}/learning_curves.npy".format(res_path,path[0])).item()
		train_ppls,val_ppls = curves['train_ppls'],curves['val_ppls']


		ax.plot(val_ppls[1:],label="Experiment {} Validation PPL".format(path[-1])) #Start from 1 as the first PPL is too high
	ax.legend()
	ax.set_xlabel("Epochs")
	ax.set_ylabel("PPL")
	plt.savefig("plots/4.5/{}_comparison_optim.jpg".format(path[1]))
	plt.close()	

	fig,ax = plt.subplots(1)
	ax.set_title("Optimizers comparison for {}".format(paths[0][1]))

	for path in paths:
		if path[-1]=='13':
			t = 30
		elif path[-1]=='14':
			t = 60
		else:
			t=25		
		curves = np.load("{}/{}/learning_curves.npy".format(res_path,path[0])).item()
		train_ppls,val_ppls = curves['train_ppls'],curves['val_ppls']
		x = np.arange(0, len(train_ppls)*t, t)[1:]

		ax.plot(x,val_ppls[1:],label="Experiment {} Validation PPL".format(path[-1])) #Start from 1 as the first PPL is too high
	ax.legend()
	ax.set_xlabel("Time (seconds)")
	ax.set_ylabel("PPL")	
	plt.savefig("plots/4.5/{}_comparison_optim_seconds.jpg".format(path[1]))
	plt.close()	


