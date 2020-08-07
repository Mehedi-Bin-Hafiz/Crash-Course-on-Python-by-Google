filename=('grace','m','hopper')
#the position of the elements inside the tuple have meaning.
def convert_seconds(seconds):
    hours= seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remain_seconds = seconds - hours * 3600 - minutes * 60
    return hours , minutes, remain_seconds

print(convert_seconds(5000))

# unpack tuples

hours, minutes , seconds = convert_seconds(5000)
print(hours)
print(minutes)
print(seconds)







def file_size(file_info):
    Assignment, docx, size= file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
