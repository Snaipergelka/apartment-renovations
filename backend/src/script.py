from backend.src.download_and_resize import FetchResizeSave

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = FetchResizeSave('AIzaSyD3g0-WF4kTVFeBHJEHM8mckEWZ98NiCv4', 'b2830d42ed6cb4bc3')

# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value
_search_params = {
    'q': 'бабушкин ремонт',
    'num': 1,
    'fileType': 'jpg',
    # 'safe': 'active|high|medium|off|safeUndefined',  ##
    # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined',  ##
    # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined',  ##
    # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined',
    ##
    # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined'  ##
}

# this will search and download:
gis.search(search_params=_search_params, aws=True)

# # this will search, download and resize:
# gis.search(search_params=_search_params, path_to_dir='C:\Users\Angelina\workspace\google_pics_download', width=500, height=500)
#
# # search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
#     image.url  # image direct url
#     image.referrer_url  # image referrer url (source)
#
#     image.download('C:\Users\Angelina\workspace\google_pics_download')  # download image
#     image.resize(500, 500)  # resize downloaded image
#
#     image.path  # downloaded local file path
