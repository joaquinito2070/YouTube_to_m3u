# Importar la biblioteca innertube
from innertube import InnerTube

# Crear un objeto de YouTube
youtube = InnerTube("WEB")

# Crear una lista vacía para almacenar los datos de los canales
channels = []

# Buscar los canales que tienen emisiones en directo
search_results = youtube.search(query="live", params={"sp":"EgJAAQ"})

# Iterar por los resultados de la búsqueda
for result in search_results["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]:
    # Comprobar si el resultado es un canal
    if "channelRenderer" in result:
        # Obtener el nombre, el grupo, el logo y el tvg-id del canal
        channel_name = result["channelRenderer"]["title"]["simpleText"]
        channel_group = result["channelRenderer"]["ownerBadges"][0]["metadataBadgeRenderer"]["label"]
        channel_logo = result["channelRenderer"]["thumbnail"]["thumbnails"][0]["url"]
        channel_tvg_id = result["channelRenderer"]["navigationEndpoint"]["browseEndpoint"]["browseId"]

        # Añadir los datos del canal a la lista
        channels.append(f"{channel_name} | {channel_group} | {channel_logo} | {channel_tvg_id}")

# Abrir el archivo youtube_channel_info.txt en modo escritura
with open("youtube_channel_info.txt", "w") as file:
    # Escribir las dos primeras líneas que no se deben editar
    file.write("~~ DO NOT EDIT THE FIRST 2 LINES\n")
    file.write("~~ FORMAT: <channel name> | <group name> | <logo> | <tvg-id>\n")

    # Escribir los datos de los canales en el archivo, separados por saltos de línea
    for channel in channels:
        file.write(channel + "\n")
