import googleapiclient

from backend.src.google_api_wrapper import GoogleBackendException


def search(ctx, query, num, safe, filetype, imagetype, imagesize,
           download_path, width, height, custom_file_name):

    if imagesize:
        imagesize = imagesize.upper()

    search_params = {
        'q': query,
        'num': num,
        'safe': safe,
        'fileType': filetype,
        'imgType': imagetype,
        'imgSize': imagesize
    }

    try:
        gis = ctx.obj['object']

        with gis:
            gis.search(search_params, download_path,
                       width, height, custom_file_name)

        results = ctx.obj['object'].results()

        if results:
            for image in results:
                print(image.url)
                if image.path:
                    print(image.path)
                    if not image.resized:
                        print('[image is not resized]')
                else:
                    print('[image is not downloaded]')
                print("39")
        else:
            print('No images found!')

    except GoogleBackendException:
        print('Error occurred trying to fetch '
                    'images from Google. Please try again.')

    except googleapiclient.errors.HttpError as e:
        print(f'Google reported an error: {str(e)}')
        return
