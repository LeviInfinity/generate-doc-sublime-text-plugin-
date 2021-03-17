import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def getBlankCount():
			curPos = self.view.sel()[0].b
			t = curPos-1
			while t>=0:
				if self.view.substr(sublime.Region(t,t+1))=="\n":
					break
				t-=1
			blankCount = curPos-t
			return blankCount
		def inertFunction():
			curPos = self.view.sel()[0].b
			#print(curPos)
			i = 0
			start = 0
			end = 0
			blankCount = getBlankCount()
			#print("blankCount",blankCount)
			while i<1000:
				#print(self.view.substr(sublime.Region(curPos,curPos)))
				curChar = self.view.substr(sublime.Region(curPos,curPos+1))
				if curChar == "(":
					start = curPos
				if curChar == ")":
					end = curPos
					break
				curPos+=1
				i+=1
			if i>=1000:
				return
			params = self.view.substr(sublime.Region(start+1,end))
			#print(self.view.substr(sublime.Region(start+1,end)))
			params = params.replace("\n","")
			paramList = params.split(",")
			#print("paramList",paramList)
			paramNameList = []
			for ele in paramList:
				ele = ele.strip()
				equalIndex = ele.find("=")
				if equalIndex!=-1:
					ele = ele[:equalIndex-1] #去除默认参数
				ele = ele.strip()
				type_name  = ele.split(' ')

				if len(type_name)<2:
					continue
				paramNameList.append(type_name[-1])
			paramFmtStr = """/** @brief \n"""
			for name in paramNameList:
				paramFmtStr+=" "*blankCount + """* @param {0} \n""".format(name)
			paramFmtStr+=" "*blankCount +"*/"
			#print(paramFmtStr)
			#print(self.view.substr(sublime.Region(100,200)))
			self.view.insert(edit, self.view.sel()[0].b, paramFmtStr)

		def nextLineTye():
			curPos = self.view.sel()[0].b+1
			nextLine = ""
			while True:
				curChar = self.view.substr(sublime.Region(curPos,curPos+1))
				if curChar=="\n":
					break
				else:
					nextLine += curChar
				curPos+=1
			strs = nextLine.split(" ")
			
			if  "class" in strs:
				return ["class",strs[strs.index("class")+1]]
			if "struct" in strs:
				return ["struct",strs[strs.index("struct")+1]]
			if "enum" in strs:
				return ["enum",strs[strs.index("enum")+1]]
			if "interface" in strs:
				return ["interface",strs[strs.index("interface")+1]]
			return ["",""]

		curPos = self.view.sel()[0].b
		type_name = nextLineTye()
		if len(type_name[0])!=0: #insert enum/class/struct/interface
			#print("insert enum/class/struct")
			blankCount = getBlankCount()
			paramFmtStr = """/** @{0} {1} \n""".format(type_name[0],type_name[1])
			paramFmtStr+=" "*blankCount + """* @brief \n"""
			paramFmtStr+=" "*blankCount +"*/"
			self.view.insert(edit, self.view.sel()[0].b, paramFmtStr)
		elif self.view.substr(sublime.Region(curPos-1,curPos))==";":  #insert member
			self.view.insert(edit, self.view.sel()[0].b, "///< ")
		else:#insert func
			#print("insert func")
			inertFunction()
	
