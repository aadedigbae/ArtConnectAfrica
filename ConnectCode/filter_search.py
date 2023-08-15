#!/usr/bin/python3
#Filter artworks based on country and other filters

def filter_artworks(artworks, filters):
  #Filters a list of arts

  filtered_artworks = []
  for illustrations in artworks:
    is_valid = True
    for key, value in filters.items():
      if not illustrations.get(key) == value:
        is_valid = False
        break

    if is_valid:
      filtered_artworks.append(illustrations)

  return filtered_artworks


if __name__ == "__main__":
  artworks = [
      {
          "country": "Rwanda",
          "artworks_type": "illustrations",
          "url": "https://www.example.com/images/rwanda-illustrations.jpg"
      },
      {
          "country": "Nigeria",
          "artworks_type": "animations",
          "url": "https://www.example.com/images/nigeria-animations.jpg"
      },
      {
          "country": "Kenya",
          "artworks_type": "illustrations",
          "url": "https://www.example.com/images/kenya-illustrations.jpg"
      }
  ]

  filters = {
      "country": "Rwanda",
      "artworks_type": "illustrations"
  }

  filtered_artworks = filter_artworks(artworks, filters)

  for illustrations in filtered_artworks:
    print(illustrations["url"]
    pass
  for animations in filtered_artworks:
    print(animations["url"])
