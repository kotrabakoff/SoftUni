from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_matrix()


    # @property
    # def photos(self):
    #     photos = []
    #     for i in range(self.pages):
    #         line = [None] * self.PHOTOS_PER_PAGE
    #         photos.append(line)
    #     return photos


    def build_matrix(self):
        photos = []
        for _ in range(self.pages):
            photos.append([])
        return photos

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(page) + 1}"
        return "No more free slots"
        # for page in range(self.pages):
        #     for photo in range(PhotoAlbum.PHOTOS_PER_PAGE):
        #         if self.photos[page][photo] is None:
        #             self.photos[page][photo] = label
        #             return f"{label} photo added successfully on page {page+1} slot {photo+1}"
        # return "No more free slots"

    def display(self):
        delimiter = "-----------"
        result = f"{delimiter}\n"
        for page in self.photos:
            page_string = ' '.join(['[]' for _ in page])
            result += page_string + "\n" + delimiter + "\n"

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
