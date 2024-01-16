rovidites = input("Add meg a rövidítést: ")

engedelyek = {
    'LAPL': 'Light Aircraft Pilot Licence \nKönnyű Repülőgép Pilóta Szakszolgálati Engedély',
    'ATPL': 'Airline Transport Pilot Licence \nLégitársasági Pilóta Szakszolgálati Engedély',
    'PPL': 'Private Pilot Licence \nMagánpilóta Szakszolgálati Engedély',
    'CPL': 'Commercial Pilot Licence \nKereskedelmi Pilóta Szakszolgálati Engedély'
}

if rovidites in engedelyek:
    print(f"{rovidites} {engedelyek[rovidites]}")
else:
    print("halo, valamit elirtal.")
