from fpdf import FPDF
from PIL import Image
import os, glob

thisPath = os.path.dirname(os.path.abspath(__file__))
devPath = thisPath + "\\dev";
releasePath = thisPath + "\\release";
mm = 0.35

#all dir
for dirname, dirnames, filenames in os.walk(devPath):
	w = 0
	h = 0
	namePdf = ''
	images = list()
	namePdf = os.path.split(dirname)[1]
	# print(dirname)
	# print(dirnames)
	# print(filenames)
	# aaa = input()
	if filenames:
		if filenames[0].endswith('.jpg'):
		#pass on the files
			for filename in filenames:
				if filename.endswith('.jpg'):
					img = Image.open(os.path.join(dirname, filename))
					img.thumbnail((1200,1200), Image.ANTIALIAS)
					img.save(os.path.join(dirname, filename), "JPEG")
					w, h = img.size
					print(os.path.join(dirname, filename))
					images.append(os.path.join(dirname, filename))

		#create pdf
			pdf = FPDF('P', 'mm', (w*mm, h*mm))

		#add image to pdf
			for image in images:
				pdf.add_page()
				pdf.image(image, 0, 0, 0, 0)

		#create folder
			if not os.path.exists(releasePath):
				os.makedirs(releasePath)

		#save pdf
			if (releasePath + "\\" + namePdf + ".pdf") != 'C:\\Users\\ivan\\Desktop\\p\\release\\.pdf':
				print(releasePath + "\\" + namePdf + ".pdf")
				pdf.output(releasePath + "\\" + namePdf + ".pdf", "F")









#-----------------------------------------------------
# thisPath = os.path.dirname(os.path.abspath(__file__))
# devPath = thisPath + "/dev";
# releasePath = thisPath + "\\release";

# os.chdir(devPath)

# for file in glob.glob("*.jpg"):
# 	img = Image.open(file)
# 	img.thumbnail((500,500), Image.ANTIALIAS)
# 	print(releasePath + file)
# 	img.save(releasePath + "\\" + file, "JPEG")

# pdf = FPDF()

# imagelist = ['1.jpg', '2.jpg']

# for image in imagelist:
# 	img = Image.open(image)
# 	w, h = img.size
# 	img.thumbnail((500,500), Image.ANTIALIAS)
# 	img.save("2"+image, "JPEG")
# 	print(w, h)
# 	pdf.add_page()
# 	pdf.image(image,0,0,w,h)
# pdf.output("yourfile1.pdf", "F")