#Use gpt-3 API to generate video game
def generateVideoGameGPT3():
    #generate title
    title = generateTitleGPT3()
    #generate description
    description = generateDescriptionGPT3()
    #generate genre
    genre = generateGenreGPT3()
    #generate release date
    releaseDate = generateReleaseDateGPT3()
    #generate developer
    developer = generateDeveloperGPT3()
    #generate publisher
    publisher = generatePublisherGPT3()
    #generate rating
    rating = generateRatingGPT3()
    #generate platform
    platform = generatePlatformGPT3()
    #generate price
    price = generatePriceGPT3()
    #generate game
    game = {
        "title": title,
        "description": description,
        "genre": genre,
        "releaseDate": releaseDate,
        "developer": developer,
        "publisher": publisher,
        "rating": rating,
        "platform": platform,
        "price": price
    }
    return game
