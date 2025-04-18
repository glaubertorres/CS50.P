filename = input('File name: ').strip().lower().replace('jpg', 'jpeg')

if not (filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.gif')):
    if (filename.endswith('.pdf') or filename.endswith('.zip')):
        filename = filename.split('.')

        print('application/' + filename[-1])

    elif filename.endswith('txt'):
        filename = filename.split('.')
        plain = str(filename[1]).replace('txt', 'plain')
        print('text/'+plain)

    else:
        print('application/octet-stream')

else:
    filename = filename.split('.')
    print('image/' + filename[-1])