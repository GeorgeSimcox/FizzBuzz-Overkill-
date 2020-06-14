def writecsvSETTINGS(newline):
    with open("Setting.txt","w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(newline)
        csvFile.close()

def writecsvDEFAULTSETTINGS(newline):
    with open("SettingDefault.txt","w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(newline)
        csvFile.close()