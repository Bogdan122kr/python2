class registr:
    def vvod(self,v):
        self.v=v
    def vivod(self):
        print(str.upper(self.v))

st = registr()
st.vvod(input("введите слово: "))
st.vivod()
